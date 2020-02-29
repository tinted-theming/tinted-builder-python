#!/usr/bin/env python3

# First, check modules exist
from importlib.util import find_spec as module_exists
#import importlib.util.find_spec as module_exists
import sys
if not module_exists("aiofiles") or not module_exists("pystache" or not module_exists("yaml")):
	print("Missing Modules! Do: pip3 install --upgrade aiofiles pystache PyYAML")
	sys.exit(1)

import base24_builder

if __name__ == '__main__':
    base24_builder.run()
