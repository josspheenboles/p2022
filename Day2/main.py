l=[]
for x in range(1,5):
    if (x != 1):
        l.append(x)
print(l)
#[value loop [condition]]
print([x for x in range(1,5) if(x!=1)])
print( [letter for letter in 'mohame magdy' if(letter!=' ' and letter!='m')])
l=[]
for letter in 'mohame magdy':
    if(letter not in l and letter!=' '):
        l.append(letter)
print(l)
'''
opens=['python','php','ruby',1,1.1,[],()]
for x in opens:
    print(x)

#collection str list tuple
opens=('python','php','ruby',1,1.1,[],())
enumerate(opens)#[(0,'python'),.....(2,'ruby')]
for item in enumerate(opens):
    print(item)

name='ali ahmed'
count=0
print(enumerate(name))#[(0,'a'),....(8,'d')]
index,leterr=(0,'a')
for index,leterr in enumerate(name):
    #print(item,type(item))
    #print('letter',item[1],'has index',item[0])
    print('letter',leterr,'has index',index)

for n in name:
    print(n,count,end=' ')
    count+=1
x,*y,z=(1,'one',30)
#*   before varaible in decalte ----> list
#*   before varaible in argument to function ----> tuple
print(x,y,z)#[1,'one],'asd',30


x,*y,z=(1,'one',23,4,65,'asd',30)
#*   before varaible in decalte ----> list
#*   before varaible in argument to function ----> tuple
print(x,y,z)#[1,'one],'asd',30

t=(1,'one')
x,y=t
print(x,y)

t='one',1,1.1,True,[],(),{}
t=1,2
print(t)

print(t[2::-1])
print(t,type(t))
opens=['python','php','ruby']
comm=['c#','c','c++',1,True,1.1,[]]
for val in comm:
    print(val,type(val))

x=opens.copy()
x[0]='asd'
print(opens)
print(x)

print(opens+comm)
#opens.extend(comm)
comm.extend(opens[0])
comm.append(opens[0])
print(opens)
print(comm)

print(opens+comm)
print(opens)
print(comm*2)

#list #collection of values different data type
l=[1,1.1,True,'one',1+2j,[3,4],(),{}]

print(l[5],type(l[5]))
print(l[5][0])
l=[
    [1,2],
    [3,4]
]
print(l[1][0])

l.pop(0)
l.append(4)
l.insert(2,'insert')
l.remove(True)
print(len(l),l)
print(True==1)

l[0]=1.2
print(l)

print(l[::-1])
print(l[-1])

print(l[0])
#print(l[8])
print(len(l))

print(l,type(l))
num=1+2j
num2=2#2+0j
print(num2-num)
print(num,type(num))
#struct class

#while
flag='y'
while(flag.upper()=='y'):
    n1=float(input('enter num1'))
    n2=float(input('enter num2'))
    operarion=input('enter operation + - * /')
    if(operarion=='+'):
        print(n1+n2)
    flag=input('enter to cont. press y else press n')

#loop in 'ahmed'
#loop input from user until stop

for num in range(5):
    pass
if(1==1):
    pass

#for else
for num in range(5):#[0.....4]
    if(num==2):
       continue
    print(num)
else:
    print(5)
    #print('all database backuped')
#[0,1]

#for varname in collection(str,range)
for ch in 'ali ahmed':
    print(ch,type(ch))
for num in range(5):
    print(num,type(num))
print(range(5),type(range(5)))


#range([start=0],end,[step=1])
print(range(1,12,1),type(range(1,12,1))) #1,2,3,.....,11
for number in range(1,13,1):
    print(number)
range(0,12,1)#[0,.....11]
range(0,12)#[0,.....,11]
range(12)#[0,....,11]

str1='mobile'
vowel='aoieu'
for ch in str1:#ch--->m o b i l e
    if(ch in vowel):
        str1=str1.replace(ch,'')


str1=str1.replace('a','')
str1=str1.replace('o','')
str1=str1.replace('i','')
str1=str1.replace('e','')
str1=str1.replace('u','')

num1=input('enter num1')
num2=(input('enter num2'))
#check values then do operation
if(not num1.isdigit()):
    print('number1 must be digit')
elif(not num2.isdigit()):
    print('number2 must be digit')
else:
    print(int(num2)+int(num1))

#double check,indet & levels
if(num1.isdigit() and num2.isdigit()):# no body
    num1=int(num1)
    num2=int(num2)
    print(num2 + num1)
else:
    if(not num1.isdigit()):
        print('num1 must be digit')
    else:
        print('num2 must be digit')
'''