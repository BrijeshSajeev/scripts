#!/usr/bin/env python3

#env - commad to list the envronment variables
#export - set new env variable ex : >export FRUIT=Pineapple
import os

print("HOME : "+os.environ.get("HOME",""))
print("SHELL : "+os.environ.get("SHELL",""))

