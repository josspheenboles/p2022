#data types ,controls
x=1
y=2
print(x,y)
x,y=y,x
print(x,y)
'''
print(x,y)
temp=y#2
y=x#1
x=temp
print(x,y)

#list,tuple,dict
# tuple same list
t=1,3
print(type(t),t)
x,y=t
print(x,y)

t=(1,)
print(t,type(t))

l=[1,2]
l[0]='one'
print(l)
t=(1,1.1,True,{},(),[],'dfkdkfl')
#t[0]='fjldkjflkdsfj'
print(t.count(1))

print(t,type(t))
print(t[2:4])
print(len(t))
print(t[7])

#[value iteration condition]
print([month for month in range(1,13) if(month%2==0)])

l=[]
for month in range(1,13):
    if(month%2==0):
        l.append(month)
print(l)

for month in range(1,13):
    l.append(month)
print(l)
#print([value iteration])
print([month for month in range(1,13)])

#collection of values different data types
oldserver=['server1','server2',[1,'d',True],(),{}]
newserver=['ser2','ser4']
#array list
[[1,2],[2,5]]

#oldserver.extend(newserver)
newserver.extend(oldserver)
print(oldserver)
print(newserver)

print(oldserver+newserver)#concat
print(oldserver)
print(newserver)
print(newserver*3)#repeat

l=[1,1.1,True,[2,3],'one']
print(l.count(1))
print(l.index(True))
print(1==True)
print(True==int(1))
print(l)

#l.remove('True')
print(1==True)
l.pop()
l.pop(2)
l.append((1,2))
l.insert(2,'test')
print(type(l))
for x in enumerate(l):
    print(x,type(x))

l[0]='2'
#l[11]='sdjsdlk'
print(l,len(l))

print(l[1],type(l[1]))
print(l[1:3])
print(l[1:])
print(l[:4])
print(l[4:1:-1])

print(l,type(l))
print(len(l))
#single line comment
"""
kfdslk;lf
k;kdf;dsf
"""




#loop
#while(condtiion):
#
count=0
while(count>3):
    input('enter num')
    count-=1


flag='y'
while(flag.lower()=='y'):
    input('enter num')
    flag=input('enter y to cont. else enter n')




for i in range(0,3):
    input('enter num')
x,y=(1,3)
print(x,y)
enumerate('ai')#[(0,'a'),(1,'i')]
for x in enumerate('ai'):
    print(x)

for num in range(5):
    if(num==2):
        #break
        continue
    print(num, end=' ')
else:
    #for all done
    print('end for ')

for index,val in enumerate('ali ahmed'):
    print(type(index),type(val))

#range([start=0],end,[step=1])
range(0,5,1)#[0,1,2,3,4]
range(0,5)#[0,1,2,3,4]
range(5)#[0,1,2,3,4]
print(range(0,5,2))#[0,2,4]
range(1,5,2)#[1,3]
for month in range(1,13):
    print(type(month))
    print('monthe ',month)


name ='ali ahmed'
for x,y in enumerate(name):#[(0,'a'),(1,'l').....,(8,'d')]
    print(x,y)


x,y=1,3
print(x,y)

print(len(name))
#for(count to loop)
#enumerate(collection) #str,list,tuple,dic
#[(0,'a'),(1,'l')......,(8,'d')]
#unpacking
x,y,z=(1,'on',True)
print(x,y,z)
index,ch=(0,'a')
print(index,ch)
print(enumerate(name))
for index,ch in enumerate(name):#(index,value)
    #print(item,item[0],item[1])
    print(index,ch)
#while (stop looping condition)

index=0
for ch in name:#count length str
    print(ch,index)
    index+=1
#debug
#str  isnumeric,isdigit if
x=input('enter number')
if(x.isdigit()):
    num=int(x)
    if(num==0):
        print('is zero not even or odd')
    elif(num%2==0):
        print(num,'is even')
    else:
        print(num,'is odd')
else:
    print('number must be digit')

name='ali ahmed'
x=6
#if (condition) :
if(x==0):
    print('zero')
    print('close')
elif(x>5):
    print(x, 'more than 5')
elif(x<5):
    print(x, 'less than 5')
else:
    print('cont.')

name='ali ahmed'
print(name.replace('a','@'))
name=name.replace('a','@')
print(name)

print('ali','ahmed',sep='&',end=' ')#sep=' ',end='\n'
print('aswan')
'''