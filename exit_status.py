#!/usr/bin/env python3

import sys
import os

filename=sys.argv[1]


if not os.path.exists(filename):
	with open(filename,'w') as f:
		f.write("Hello World")
else:
	print("File already exists ..")
	sys.exit(1)


"""
wc - it print the values of lines, words and characters of a given file

echo $? -  will print the process status code (0 for execution succesfull)

"""

