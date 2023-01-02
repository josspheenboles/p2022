str_list = input()
lis = []
ind = []
for index, character in enumerate(str_list):
    if character == "'" or character == '"':
        ind.append(index)
        if str_list[index + 1] == ",":
            if str_list[index + 2] == " " or str_list[index + 2] == "'" or str_list[index + 2] == '"':
                lis.append(str_list[ind[0] + 1:index])
                ind = []
        elif str_list[index + 1] == " ":
            if str_list[index + 2] == ",":
                if str_list[index + 3] == " " or str_list[index + 2] == "'" or str_list[index + 2] == '"':
                    lis.append(str_list[ind[0] + 1:index])
                    ind = []

sorte = {}

for name in lis:
    ch1 = name[0]
    if ch1 not in sorte:
        sorte[ch1] = []
    sorte[ch1].append(name)

print(sorte)

'''
import os
import subprocess
os.popen('dir').read()
subprocess('dir')
import math
print(math.pi)
math.pow(2,2)#2**2

import os
print(os.error)

os.mkdir('test')
os.chdir('H:\\aswansysadmin122022')
os.system('dir')

if(os.getlogin()=='root' or os.getlogin()=='administartor'):
    if(os.name=='nt'):
        if(os.system('dir')==1):
            print('invalid command')
    else:
        os.system('ls -l')
else:
    print('invalid user permision')

file=open('asd2.txt','r')
lines=file.readlines()
print(float(lines[0])+float(lines[1]))
file.close()

import sys
n1=float(sys.argv[1])
n2=float(sys.argv[2])
print(n1+n2)
print(sys.argv)
print(type(sys.argv))
print()

print(sys.path)
print(sys.exc_info())
print(sys.builtin_module_names)

#files simple
#open('path',mode)
#mode r--->read,w---->write,a----->apppend,r+--->read&write
# rb===>read binary file,rb+====> write /read from binary file
file=open(r'H:\Qena_cyber_2022\asd.txt','r+')
if(file.readable()):
    print(file.read())
    file.seek(5)
if(file.writable()):
    file.write('li')
file.close()

file=open('asd2.txt','a')
file.write('line1')
file.seek(0)
file.write('as')
file.close()

file=open('asd2.txt','r')#file exsit clear,not ex create fiel
lines=file.read().split('\n')
for line in lines:
    if(line.isdigit()):
        print(int(line))
file.close()

file=open('asd2.txt','a')#file exsit clear,not ex create fiel
"""
file.write('\nplpla3')

file.write('\nplpla2')

file.writelines(['line1','\nline2'])
"""
file.write("""
line1
line2
lin3
""")
file.close()


#read
file=open('asd.txt','r')
print(file.readline())
file.seek(0)
print(file.readline())
file.close()

file=open('asd.txt','r')
print(file.read(5))
file.seek(0)
print(file.read(3))
print(file.readlines())
file.close()

file=open('asd.txt','r')
#print(file.read().split('\n'))
content=file.readlines()
print(type(content))
print(content)
for line in content:
    print(line)
file.close()

file=open('asd.txt','r')
content=file.read(5)
for line in content:
    print(line)
print(type(content))
print(content)
file.close()


#define mode
#open file
file=open('asd.txt','r')
"""
for line in file:
    print(line)
"""
#close file
file.close()

print(type(file))
print(file)
#errors
#syntax,logical,exception--->runtime error
#exception--->runtime error
#value error,zero divid
import sys
try:
    n1=float(input('enter number2'))
    n2=float(input('enter number2'))
    print(n1+n2)
    print(n1/n2)
except ValueError:
    print('numbers must be digit')
except ZeroDivisionError:
    print('/0')
except:
    #(exception data type,msg error,address)
    print(sys.exc_info()[1])
else:
    print('usa server tested')
finally:
    print('thanx for using')

n1=(input('enter number2'))
if(n1.isdigit()):
    n1=float(n1)
else:
    print('number 1 must be digit not letter')

#logical===>debuge
#add break point,debug
n1=float(input('enter number2'))
n2=float(input('enter number2'))
print(n1+n2)
#syntax function inputs data types,return data type
#datatype limit
print('val1','val2',1,1.1,True,sep='\n',end=' ')
print('line')
print ('assa')


l=input('enter names')
l=l.replace('"','').replace("'",'').replace('[','').replace(']','').split(',')
names={}
for name in l:
    names[name[0]]=[name]
print(names)

def calacarea(shapename,dim1,dim2=0):#square,circle
    if(shapename=='rect'):
        return dim1*dim2
    elif(shapename=='circel'):
        return .5*dim1*3.14
    else:
        print('invalid shape name')
        return None

#dim1,dim2,shape
shapename=input('enter shape')
dim1=float(input('enter dim1'))
if(shapename=='r' or shapename=='t' ):
    dim2 = float(input('enter dim2'))
    print(calacarea(shapename,dim1,dim2))
else:
    print(calacarea(shapename,dim1))
'''
