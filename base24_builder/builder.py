"""Combine schemes and templates to generate user-ready themes """

from __future__ import annotations

import asyncio
import os
from glob import glob
from pathlib import Path

import aiofiles
import pystache

from .utils import compat_event_loop, get_yaml_dict, rel_to_cwd, verb_msg





def get_parent_dir(base_dir: str, level: int=1):
	"Get the directory $level levels above $base_dir."
	while level > 0:
		base_dir = os.path.dirname(base_dir)
		level -= 1
	return base_dir


def get_pystache_parsed(mustache_file: str):
	"""Return a ParsedTemplate instance based on the contents of
	$mustache_file."""
	with open(mustache_file, encoding="utf-8") as file_:
		parsed = pystache.parse(file_.read())
	return parsed




def reverse_hex(hex_str: str):
	"""Reverse a hex foreground string into its background version."""
	hex_str = "".join([hex_str[i : i + 2] for i in range(0, len(hex_str), 2)][::-1])
	return hex_str


def format_scheme(scheme: dict, slug: str):
	"""Change $scheme so it can be applied to a template."""
	scheme["scheme-type"] = "16"
	# Base16 here:
	scheme["scheme-name"] = scheme.pop("name")
	scheme["scheme-author"] = scheme.pop("author")
	scheme["scheme-slug"] = slug
	bases = [f"base{x:02X}" for x in range(0, 16)]
	for base in bases:
		scheme[f"{base}-hex"] = scheme["palette"].pop(base)
	# Base24 (with fallbacks)
	extended_bases = [f"base{x:02X}" for x in range(16, 24)]
	base_map = {
		"base10": "base00",
		"base11": "base00",
		"base12": "base08",
		"base13": "base0A",
		"base14": "base0B",
		"base15": "base0C",
		"base16": "base0D",
		"base17": "base0E",
	}
	for extended_base in extended_bases:
		if extended_base in scheme:
			scheme[f"{extended_base}-hex"] = scheme["palette"].pop(extended_base)
			scheme["scheme-type"] = "24"
		else:
			scheme[f"{extended_base}-hex"] = scheme[f"{base_map[extended_base]}-hex"]

	all_bases = [f"base{x:02X}" for x in range(0, 24)]
	for all_base in all_bases:
		# HEX and Reverse HEX
		scheme[f"{all_base}-hex-r"] = scheme[f"{all_base}-hex"][0:2]
		scheme[f"{all_base}-hex-g"] = scheme[f"{all_base}-hex"][2:4]
		scheme[f"{all_base}-hex-b"] = scheme[f"{all_base}-hex"][4:6]
		scheme[f"{all_base}-hex-bgr"] = reverse_hex(scheme[f"{all_base}-hex"])
		# RGB 0-255
		scheme[f"{all_base}-rgb-r"] = str(int(scheme[f"{all_base}-hex-r"], 16))
		scheme[f"{all_base}-rgb-g"] = str(int(scheme[f"{all_base}-hex-g"], 16))
		scheme[f"{all_base}-rgb-b"] = str(int(scheme[f"{all_base}-hex-b"], 16))
		# RGB 0.0-1.0
		scheme[f"{all_base}-dec-r"] = str(int(scheme[f"{all_base}-rgb-r"]) / 255)
		scheme[f"{all_base}-dec-g"] = str(int(scheme[f"{all_base}-rgb-g"]) / 255)
		scheme[f"{all_base}-dec-b"] = str(int(scheme[f"{all_base}-rgb-b"]) / 255)


def slugify(scheme_file: str):
	"""Format $scheme_file_name to be used as a slug variable."""
	scheme_file_name = os.path.basename(scheme_file)
	if scheme_file_name.endswith(".yaml"):
		scheme_file_name = scheme_file_name[:-5]
	return scheme_file_name.lower().replace(" ", "-")


async def build_single(template_file: str, scheme_file: str, base_output_dir: str, verbose:bool):
	"""Build colorscheme from $scheme_file using $job_options. Return True if
	completed without warnings. Otherwise false."""
	scheme = get_yaml_dict(scheme_file)
	scheme_slug = slugify(scheme_file)
	format_scheme(scheme, scheme_slug)
	scheme_name = scheme["scheme-name"]
	scheme_type = scheme["scheme-type"]
	warn = False  # set this for feedback to the caller

	if verbose:
		print(f'Building colorschemes for scheme "{scheme_name}"...')


	output_dir = os.path.join(base_output_dir, Path(template_file).name)
	try:
		os.makedirs(output_dir)
	except FileExistsError:
		pass

	filename = f"base{scheme_type}-{scheme_slug}"

	build_path = os.path.join(output_dir, filename)

	# include a warning for files being overwritten to comply with base16 0.9.1
	if os.path.isfile(build_path):
		verb_msg(f"File {build_path} exists and will be overwritten.")
		warn = True

	async with aiofiles.open(build_path, "w") as file_:
		file_content = pystache.render(get_pystache_parsed(template_file), scheme)
		await file_.write(file_content)

	if verbose:
		print(f'Built colorschemes for scheme "{scheme_name}".')

	return not (warn)


async def build_single_task(template_file: str, scheme_file: str, base_output_dir: str, verbose:bool):
	"""Worker thread for picking up scheme files from $queue and building b16
	templates using $templates until it receives None."""
	try:
		return await build_single(template_file, scheme_file, base_output_dir, verbose)
	except Exception as e:
		verb_msg(f"{scheme_file}: {repr(e)}", lvl=2)
		return False


async def build_scheduler(scheme_files: set[str], template_files: set[str], base_output_dir: str, verbose:bool):
	"""Create a task list from scheme_files and run tasks asynchronously."""
	task_list =	[
		build_single_task(template_file, scheme_file, base_output_dir, verbose)
		for scheme_file in scheme_files
		for template_file in template_files
  	]
	return await asyncio.gather(*task_list)



def build(template_files: set[str], scheme_files: set[str], base_output_dir: str, verbose: bool):

	# raise PermissionError if user has no write access for $base_output_dir
	try:
		os.makedirs(base_output_dir)
	except FileExistsError:
		pass

	if not os.access(base_output_dir, os.W_OK | os.X_OK):
		raise PermissionError

	with compat_event_loop() as event_loop:
		results = event_loop.run_until_complete(build_scheduler(scheme_files, template_files, base_output_dir, verbose))

	print("Finished building process.")
	return all(results)
