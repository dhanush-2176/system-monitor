import os
import platform
from datetime import datetime

print("---- SYSTEM INFO ----")

now = datetime.now()
print("Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

hostname = platform.node()
print("Hostname:", hostname)

print("Python Version:", platform.python_version())

user = os.getenv("USER")
print("Current User:", user)

files = os.listdir(".")
print("\nFiles in Directory:")
for f in files:
    print("-", f)

print("\nTotal Files:", len(files))

name = input("\nEnter your name: ")
print("Hello,", name, "! Welcome to DevOps Project 🚀")
