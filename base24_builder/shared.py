"""Shared utils used by the other builder components
"""
import os
import sys
import asyncio
from contextlib import contextmanager
import yaml
from metprint import LogType, Logger, FHFormatter

printf = Logger(FHFormatter())

class JobOptions:
	"""Container for options related to job processing"""

	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)


CWD = os.path.realpath(os.getcwd())

@contextmanager
def compat_event_loop():
	"""OS agnostic context manager for an event loop."""
	if sys.platform.startswith("win"):
		asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

	event_loop = asyncio.get_event_loop()

	if event_loop.is_closed():
		event_loop = asyncio.new_event_loop()
		asyncio.set_event_loop(event_loop)

	yield event_loop

	event_loop.close()


def rel_to_cwd(*args):
	"""Get absolute real path of $path with $CWD as base."""
	return os.path.join(CWD, *args)


def get_yaml_dict(yaml_file):
	"""Return a yaml_dict from reading yaml_file. If yaml_file is empty or
	doesn't exist, return an empty dict instead."""
	try:
		with open(yaml_file, "r") as file_:
			yaml_dict = yaml.safe_load(file_.read()) or {}
		return yaml_dict
	except FileNotFoundError:
		return {}


def err_print(msg, exit_code=1):
	"""Print $msg and exit with $exit_code."""
	print(msg, file=sys.stderr)
	sys.exit(exit_code)


def verb_msg(msg, lvl=1):
	"""Print a warning ($lvl=1) or an error ($lvl=2) message."""
	if lvl == 1:
		print(printf.logString(msg, LogType.WARNING), file=sys.stderr)
	elif lvl == 2:
		print(printf.logString(msg, LogType.ERROR), file=sys.stderr)
