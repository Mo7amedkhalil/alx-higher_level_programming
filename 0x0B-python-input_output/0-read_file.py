#!/bin/usr/python3
"""function reading a text file. """
def read_file(filename=""):
	"""prints UTF8 text file contents to stdout"""
	with open(filename, encoding="ytf-8") as f:
			print(f.read(), end="")
