import argparse
import asyncio
import glob

import os

from typing import Any

from builder import build


def run() -> None:

	parser = argparse.ArgumentParser(description="Base16 builder in Python")
	parser.add_argument(
		"--schemes-dir",
		default=".",
		help="Target directory for scheme data",
	)
	parser.add_argument(
		"--template-dir",
		default=".",
		help="Target template directory to build",
	)
	parser.add_argument(
		"--verbose",
		action="store_true",
		help="Log all debug messages",
	)
	parser.add_argument(
		"--online",
		action="store_true",
		help="Run in online mode and pull schemes directly from GitHub",
	)

	args = parser.parse_args()


	schemes_dir = args.schemes_dir
	if args.online:
		schemes_dir = asyncio.run(get_schemes_from_github()) + "/base24"


	scheme_files = set(glob.glob(f"{schemes_dir}/**/*.yaml"))
	template_files = set(glob.glob(f"{args.template_dir}/**/*.mustache"))


	build(template_files=template_files, scheme_files=scheme_files, base_output_dir=".", verbose=args.verbose)



async def get_schemes_from_github() -> str:
	print("Attempting to load schemes from GitHub")

	proc_env = os.environ.copy()
	proc_env["GIT_TERMINAL_PROMPT"] = "0"

	url = "https://github.com/tinted-theming/schemes/archive/refs/heads/jamy/feature/base24.tar.gz"
	clone_path = "schemes"
	await asyncio.create_subprocess_exec(
		"git", "clone", url, clone_path, stderr=asyncio.subprocess.PIPE, env=proc_env
	)

	return clone_path





if __name__ == "__main__":
	run()
