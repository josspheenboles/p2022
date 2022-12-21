#data types ,controls
#loop
for num in range(5):
    if(num==2):
        #break
        continue
    print(num, end=' ')
else:
    #for all done
    print('end for ')
'''
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