statment=input('enter statment')
lett=input('enter letter')
l=[]
for x in enumerate(statment):
    if(x[1]==lett):
        l.append(x[0])
print(l)

name='rafaat'

for ch in name:#i=012 name[1]
    print(ch)








'''

#structure list,tuple,dict
#list collection of values has differernt data types
opensource=['python','shell',1,True,'python']
for val in opensource:
    if(val==True):
        break
#del (opensource[0])
opensource.remove(True)
#opensource.pop(0)
print(opensource)
print(1==True)



opensource.pop(3)
opensource.remove('python')
commercial=['C#','C','c++']
#opensource.extend(commercial)
print(opensource+commercial)
print(opensource)
print(commercial)

print(opensource+commercial)
print(opensource*2)
smalll=[1,1.1,True,'one',[3,4],(),{}]
xl=[3,4]
print(smalll+xl)
print(smalll)
print(xl)
print(xl*3)

for val in xl:
    smalll.append(val)
print(smalll)
print(xl)

xl.extend(smalll)
print(smalll)
print(xl)
#print(l.pop(3))
x=l.remove('one')

print(x)
print(l)

x=l.pop(0)
l.insert(4,'test')
l.append(100)
l.append('test')
l[0]=10
#l[7]=100
print(l)

print(l[::-1])
print(len(l))

print(l[0])
print(l[1:3])
print(l[1:])
print(l[:4])#l[0:4]
print(l[-1])
print(l)

for value in l:
    print(value,type(value))

print(type(l),l)
#if elif else
#for ,while
if(True):
    pass

#while(condition):dont know count of loops but i know event
#    body
flag='y'
while(flag.lower()=='y'):
    n1=float(input('enter number1'))
    n2=float(input('enter number2'))
    print(n1+n2)
    flag=input('enter to cont press y else press n')
for x  in range(5):
    if(x==3):
        break
    print(x,end='')
else:
    print('all loops done')

#loops for /while
for x in range(3):
    if(x==1):
        continue
    print(x,end=' ')
else:
    print('everthing is ok')

for x in 'mobile':
    if(x=='i'):
        #continue
        break
    print(x,end=' ')

#range([start=0],end,[step=1]) generate collections of numbers
for x in range(1,5,2):
    print(x)

range(0,5,1)
range(0,5)
range(5)#start=0 end=5 step=1
print(range(5),type(range(5)))
sum=0
for value in range(5):#5 times
    sum=sum+value
print(sum)

print(range(0,12,1),type(range(0,12,1)))#[0,1,2,3,....,11]
for month in range(1,13,1):
    print(month,type(month),end=' ')


print('ahmed','mohamed','sayed',sep='$',end=' ')#sep=' ' end=\n
#ahmed&mohamed
print('ali','test')#sep=' ',end=\n
print('test2')

#simple datatype float int str bool
#controls
x=1
x=1.1
x='one'
x=True
print('')
print('ahmed',end=' ')
print('ali')
print('test')


statment='mobile'#6 letters for
#for varname in collection:
count=0
for x in 'mobile':
    print(x,count,end=' ')c
    count+=1




#if statment

#if condition ---> do block of code-->1 time
#elif cndition---> do block of code---> many time
#else--->1 tim
x='1' #as digit ---> as letter
if(x=='1'):
    print('one')
    print('----')

elif(x=='2'):
    print('two')
elif(x=='3'):
    print('three')
else:
    print('other number')

#sys admin
#centos9 file--->open file add 200 usercc
#run command add user 200 time
#apache problem ---->logs --->date time msg user-->file -->string
error='error number {num} ,msg {msg},user {user},date {date} {user}'
print(error.format(date='10-1-2023',num=1,user='apache',msg='service cannt start'))
error='error number {} ,msg {},user {},date {} {}'
print(error.format(1,'apache cant start','apache','10-1-2023','apache'))

error='error number {} ,msg {},user {},date {} {}'
print(error.format(1,'apache cant start','apache','10-1-2023'))
print(error.format(10,'access denied','apache','11-1-2023'))
print(error.format('access denied',10,'apache','11-1-2023'))

#comment single line
#take string from user
statement=input('enter statment to remove vowels from it')
#remove 'a' ,'','e',i,o,u
statement=statement.replace('a','').replace('e','').replace('i','').replace('u','').replace('0','')
print((statement))
#print neww str without vowels
print(statement)
'''