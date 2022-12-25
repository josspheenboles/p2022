import os
if(os.name!='nt'):
    if (os.getlogin() == 'root'):
        os.system('ls -l')
else:
    if(os.getlogin()=='admini.'):
        os.chdir(r'H:\aswansysadmin122022\Day1')
        os.system('dir')
"""
import sys
print(sys.argv)
print(sys.argv[1]+sys.argv[2])
print(type(sys.argv[0]))
print(type(sys.argv[1]))
print(sys.exc_info())

import math
print(math.pi)
print(math.floor(4.4))
from math import pi,floor#django
print(pi)
print(floor(4.6))
#import packag1.packag2.packg3
#packag1.packag2.packg3.funname
#from packag1.packag2.packg3 import funame
#funame



file=open('asd.txt','rb+')
file.write(b'sdsdsd')
file.close()

#a w r r+
#r'/etc/ifcongi_eth0'
file=open('asd.txt','w')
#openfile in read & write  mode
file=open('asd.txt','r+')
file.write('aswan\n')
file.write('louxer\n')
file.write('alex\n')
file.write('mansoura\n')
file.seek(0)
print(file.read())
print('-------------')
file.close()

file.seek(6)
file.write('in')
print(file.read())
#file.seek(0)
#file.seek(len(file.read()))
#file.readlines()
file.write('\ntestappend')
#openfile in read mode
file=open('asd.txt','r')
lines=file.readlines()
print(type(lines))
file.close()

#for line in file.readlines():
#    print(line)
for line in file:
    print(line)
file.seek(0)
file.read(5)
if(file.writable()):
    file.write('sss')
#openfile in read mode
file=open('asd.txt','r')
#content=file.read()
#print(content,type(content))
print('=',file.read(5),'=')
print('=',file.read(10),'=')
print(file.readline())
file.seek(0)
print(file.read(5))
print(file.readlines())
#close file
file.close()

#openfile in append mode
file=open('asd','a')
file.write('test append')
file.writelines(['\n','after writelines'])

#close
file.close()

#openfile
f=open(r'H:\aswansysadmin122022\Day4\asd.txt','w')
f.write('aswan')
f.writelines(['\nline1','line2'])
if(f.readable()):
    f.read()
#f.write('''aswan sys admin''')
#close file
f.close()

print(type(f))
num1=input('enter num1')
num2=input('enter num2')
try:
    print('the sum', int(num2) + int(num1))  # if str + will concat
    print(int(num1) / int(num2))
except ZeroDivisionError:
    print('zero exceptoin')
except:
    print('error general except')
else:
    print('else block')
finally:
    print('finally block')

if(num1.isdigit() and num2.isdigit() and num2!='0'):
    print('the sum', int(num2) + int(num1))  # if str + will concat
    print(int(num1) / int(num2))
else:
    print('check numbers must be digit and num2 not equal zero')

import sys
#input --->exception
#logical error--->debug
num1=input('enter num1')
num2=input('enter num2')
try:
    #lines may be fire execption
    print('the sum',int(num2)+int(num1))#if str + will concat
    print(int(num1)/int(num2))
#except ValueError:
#    print('number must be digit')
#except ZeroDivisionError:
#    print('cannt divid by zero')
except:#carch exception
    #when fire exception
    print('call admin')
    #print(sys.exc_info()[1])
    #Expection

#syntax error --->docum.
name='asd'
name =1
print(name)

name='global'
def final():
    #name='final'
    def outer():
        #name='outer'
        def inner():
            #name = 'inner'#local var
            #nonlocal name#change & access first local variabl
            print(name)#nonelocal not found/global
            #name = 'inner'  # local var


        inner()
    outer()
final()
print(name)#

num=1
num='one'



def calaarea(shape,dim1,dim2=0):
    pass


#['ahmed','ali',"fatma"]
#input  from user
inputlist=input('''enter ['ahmed','ali',"fatma"]''')#.replace('[','').replace(']','').replace('"','').replace("'",'').split(',')
#clean str remove [],',"
inputlist=inputlist.replace('[','').replace(']','').replace('"','').replace("'",'')
#split , [name1,name2]
names=inputlist.split(',')
#declare dict of names
dictnames={}
#loop list of names
for name in names:
    if(name[0] in dictnames):
        #append name in dict
        dictnames[name[0]+'1']=[name]
    else:
        dictnames[name[0]]=[name]
    #print(dictnames)
#print dict
print(dictnames)


print({name[0]:[name] for name in names })
"""