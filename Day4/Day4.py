#files fullpath.ext
#define mode
#r ---> file exsit,read only
#w====>create,files exisit clear ,write only
#a===>crate,file exsit append,write only
#r+===>read & write,file exsit,read from index 0
#seek(count of letters)
#read--->read file ----> laste letter
#read ----> (numbers of letter)
#write---->dosnt place any line break except you put it \n
f=open('asd.txt','w')#----->creat / clear
f.write('dskdkjd')
x=['line','line']
for l in x:
    f.write(l)
f.writelines(x)
f.close()
'''

f=open('asd.txt','r')
content=f.read()

f.close()
t=(1,)
t2=(2,)
t+=t2
print(t)

#open('path fiel.extention',mode)
#mode r--->read,w===>write,a===>append,r+
#read path of exisitng file
f=open('asd.txt','r+')#path exsit
if(f.writable()):
    f.seek(25)
    f.write('line1')
    f.seek(0)
    print(f.read())
f.close()

f=open('asd.txt','a')#creat,append
if(f.writable()):
    #f.seek(5)
    f.write('line1')
f.close()
f=open('asd.txt','w')#creat,clear
if(f.writable()):
    #f.write('line1 \n line2')
    #f.write("""line2
    #line2""")
    #f.writelines(['line3','lin4'])
    pass
f.close()
f=open('asd.txt','w')
if(f.readable()):
    for line in f:
        print(line)
f.close()
#===>read & write
f=open('asd.txt','r')
lines=f.readlines()
error='in date {date} by user {user} message {msg}'
#print(lines)
for line in lines:
    splittedvalues=line.split(' ')
    listlen=len(splittedvalues)
    print('in date',splittedvalues[0],'by user',splittedvalues[listlen-1],'msg:',line.replace(splittedvalues[0],'').replace(splittedvalues[listlen-1],''))
    print(error.format(
        date=splittedvalues[0],
        msg=line.replace(splittedvalues[0],'').replace(splittedvalues[listlen-1],''),
        user=splittedvalues[listlen-1]
    ))
f.close()#realease file
f=open('asd.txt','r')
content=f.read(2)
print(content,type(content))
print(f.read())
print('===',f.read(),'---')

f.close()#realease file

#runtime error cann't handel it by if statment
n1=input('enter num1')
if(n1.isdigit()):
    n1=float(n1)
else:
    print('n1 must be digit')
try:
    n1=input('enter num1')
    n2=float(input('enter num2'))
    print(float(n1)+n2)
    print(float(n1)/n2)
except ValueError:
    print('number must be digit')
except ZeroDivisionError:
    print('cannt divid by zero')
except:
    print('call admin')

#logical error
n1=input('enter num1')
n2=float(input('enter num2'))
print(float(n1)+n2)
#syntax error
#print(asd)
print('asd')
if(True):
    print('jjd')

#lexical scope
name='ahmed'#global
def fun1():
    global name
    name='fun1'
    def fun2():
        nonlocal name
        print(name)

    fun2()
    print(name)
fun1()
print(name)










def calcarea(shapename,dim1,dim2):
    if(shapename=='r'):

        return (dim1*dim2)
    elif(shapename=='s'):
        dim = float(input('enter dim'))
        print(dim*dim)

area=calcarea('r')


def dosum (n1,n2):
    return n1+n2

def dosum():
    return 10+20

#dosum(1,2)#call dosum line1
dosum()#call dosum line4

print(dosum)
x=1
x=1.1
print(type(x))
'''