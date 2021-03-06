#!/usr/bin/env python3

# au - A platform independent package management tool
# Copyright (C) 2012-2014 Berat Alp Erbil
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


import sys, os, getpass, modules
import warnings

warnings.filterwarnings("ignore")

if getpass.getuser() == "root":
    pass
else:
    print("This program must run with root privileges. If you're using 'su' for getting root privileges, use 'su -' instead of 'su'.")
    sys.exit()

try:
    arg1 = sys.argv[1]
except:
    print("Please input valid parameters. For help try using 'au help' as root.")
    sys.exit()

if arg1 == "help":
    print("""
Au: A platform independent package management tool.
Version: 0.11
2012 - 2014 Alp Erbil
Valid parameters:
build - Build new package providing build.py
help - Show this message
ccache - Clears autmp directory
brepo - Creates a repo.py database.
    """)

elif arg1 == "build":
    try:
        arg2 = sys.argv[2]
    except:
        print("Package not found.")
        sys.exit()
    modules.builder(arg2)
    sys.exit()
elif arg1 == "ccache": #Will remove, just a temporary solution.
    os.system("rm -rf /tmp/autmp")
elif arg1 == "install":
    try:
        arg2 = sys.argv[2]
    except:
        print("Package not found.")
        sys.exit()
    modules.install(arg2)
    sys.exit()
else:
     print("Please input valid parameters. For help try using 'au help' as root.")
     sys.exit()
