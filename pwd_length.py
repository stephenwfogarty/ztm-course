#!/usr/bin/env python

name = input("What is your name? ")
pwd = input("Please enter your password: ")
pwd_length = len(pwd)
pwd_scrubbed = "*" * pwd_length

print(f"{name}, your password {pwd_scrubbed} is {pwd_length} characters long")
