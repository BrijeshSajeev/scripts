#!/usr/bin/env python3

import re

def rearrange_name(name):
	result= re.search( r"^([\w.]*), ([\w.]*)$",name)
	if not result:
		return name
	return "{} {}".format(result[2],result[1])

#print(rearrange_name("Brijesh, Sajeev"))
#print(rearrange_name("Sherbin, Silas"))

