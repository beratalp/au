# au - A platform independent package management tool
# Copyright (C) 2012-2013 Berat Alp Erbil
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

import os, shutil, sys

import warnings
warnings.filterwarnings("ignore")

def download(url, pname):
    os.chdir("/tmp")
    os.mkdir("autmp")
    os.chdir("autmp")
    os.mkdir(pname)
    os.chdir(pname)
    os.system("wget %s"%url)
def copy(file, pname):
    os.chdir("/tmp")
    os.mkdir("autmp")
    os.chdir("autmp")
    os.mkdir(pname)
    os.chdir(pname)
    try:
        shutil.copy(file,os.curdir)
    except:
        print("Source not valid.")
        sys.exit()

def debbuild(pname):
    os.chdir("/tmp/autmp/%s"%pname)
    DPakList = os.listdir(os.curdir)
    DPak = DPakList[0]
    print(DPak)
    os.system("ar xv %s"%DPak)
    DPakList = os.listdir(os.curdir)
    if "data.tar.lzma" in DPakList:
        pass
    else:
        print("This is not a valid 'deb' package.")
        sys.exit()
    os.system("unlzma data.tar.lzma")
    os.mkdir("copy")
    shutil.copy("data.tar","/tmp/autmp/%s/copy"%pname)
    os.chdir("copy")
    os.system("tar xf data.tar")
    os.remove("data.tar")
def ccontrol(pname):
    os.chdir("/tmp/autmp/%s/copy"%pname)


def cpak(pname,pver,pbuild):
    os.chdir("/tmp/autmp/%s/copy"%pname)
    pakname = "%s-%s_b%s.tar.pak"%(pname,pver,pbuild)
    os.system("tar cf %s ."%pakname)
    os.system("chmod 777 %s"%pakname)
    global pakname
def cp():
    try:
        os.mkdir("/au")
    except:
        pass
    shutil.copy(pakname,"/au")






