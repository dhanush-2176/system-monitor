#!/usr/bin/env python3
import os
import sys
import platform
from datetime import datetime
import getpass

def main():
    print("---- SYSTEM INFO ----")
    print("Date & Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Hostname:", platform.node())
    print("Python Version:", sys.version.split()[0])
    print("Current User:", getpass.getuser())
    files = os.listdir('.')
    print("Files in Directory:")
    for f in files:
        print("-", f)
    print("Number of Files:", len(files))
    user_input = input("Enter your name: ")
    print(f"Hello, {user_input}! Welcome to the system monitoring tool.")

if __name__ == "__main__":
    main()
