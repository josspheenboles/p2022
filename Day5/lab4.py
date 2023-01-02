from myexperiacn.files import fileoperationmodule
from myexperiacn.files.excelfileoperation import *#read(path,cell)
"""
def read():
    print('lab4')
"""
read('dsd','A1')#fire exception
print(fileoperationmodule.read('asd.txt'))#
print(fileoperationmodule.binarymodes)


import myexperiacn.network.networksecu
myexperiacn.network.networksecu.ping()
from myexperiacn.network.networksecu import ping as networkmoduleping
def ping():
    print('lab4 ping')
ping()
networkmoduleping()

