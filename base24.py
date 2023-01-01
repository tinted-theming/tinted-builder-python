#!/usr/bin/env python3
import sys
from importlib.util import find_spec as module_exists

if not all([module_exists(x)] for x in ["aiofiles", "pystache", "yaml"]):
	print("Missing Modules! Do: pip3 install --upgrade aiofiles pystache pyyaml")
	sys.exit(1)

import base24_builder

if __name__ == "__main__":
	base24_builder.run()
