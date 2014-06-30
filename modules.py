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


import os, sys, bmodules, shutil

def builder(pak):
    if os.access(pak,0) == True:
        pass
    else:
        print("Package not found.")
        sys.exit()
    print("Parsing build.py...")
    try:
        import build
    except:
        print("build.py not found.")
        sys.exit()
    try:
        if build.isaPakBuild == "True":
            pass
        else:
            print("This isn't a valid build.py.")
            sys.exit()
    except:
        print("This isn't a valid build.py.")

    print("Building %s"%build.AppName)
    if build.SFileT == "url":
        bmodules.download(build.SUrlP,build.PakName)
    elif build.SFileT == "file":
        bmodules.copy(build.SFileP,build.PakName)
    else:
        print('The file type that stated in build.py not yet supported.')
    if build.BType == "deb":
        bmodules.debbuild(build.PakName)
    else:
        print("The build type that stated in build.py not yet supported.")
        sys.exit()
    bmodules.cpak(build.PakName,build.PakV,build.PakB)
    bmodules.cp()
def install(pak):
    os.makedirs("/tmp/autmp/install")
    shutil.copy(pak, "/tmp/autmp/install")
    os.chdir("/tmp/autmp/install")
    os.system("tar xf %s"%pak)
    os.remove(pak)
    os.system("cp -rf * /")
    print("Install success.")


