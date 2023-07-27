#!/usr/bin/env python3

data=input("This will come from STDIN : ")
print("This will come from STDOUT : "+data)

print("This will come from STDERR : "+ data+1)






""" 
Most operating systems supply three different I/O streams by default each 
with a different purpose. The standard input stream commonly referred to 
as STDIN is a channel between a program and a source of input. Usually in 
the form of text data from the keyboard. When we use the input function to 
accept user input in a Python script we're using the STDIN stream. The 
standard output stream or STDOUT is a pathway between a program and a 
target of output, like a display. STDOUT generally takes the form of text 
displayed in a terminal. As that play when we use the print function to 
write information to the screen. The last type of pre-made I/O stream is 
called standard error, or STDERR. Standard error displays output like 
standard out, but is used specifically as a channel to show error messages 
and diagnostics from the program. It's usually printed to the screen. If 
you've ever run some Python code and receive an error, then that error 
message was probably printed using standard error stream.

"""
