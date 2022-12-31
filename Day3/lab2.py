#dict ,functions,scope
def mysum():
    print(1+2)
print(mysum)
mysum()
def mysum(n1,n2):
    print(n1+n2)
print(mysum)
(mysum(1,3))
isinstance(1,float)

'''
name='global'
def final ():
    name='final'

def outer():
    #name='outer'
    def inner():
        #nonlocal name
        print(name)#global
        #name='inner'
    inner()
    print('outer fun finished')
    print(name)#inner
outer()
final()
print(name)#

def musym(n2):
    #local
    print(n1+n2)
n1=10 #global
musym(4)

def mysum(n1,n2):
    #n1 local
    print(n1+n2)
n1='one' #global 
mysum(1,2)
print(n1)

def mysum(**values):
    """
    sum=0
    for key in values:
        sum+=values[key]
    print(sum)
    """
    print(values)




#formate key :value,min (.....),scope
str1='i love {lang} since {year}'
#key=value
print(str1.format(lang='python',year='2022'))
mysum(x1=1,x2=100,x5=3.3)
#mysum({'a':1,'b':3})
#mysum(a=1,b=3)

min(1,2,3.3,44,5,7,8)#tuple,list
def mysum(*values):
    print(type(values),values)
    sum=0
    for val in values:
        sum+=val
    print(sum)

mysum(1,2,3.3,44,5,7,8)
mysum(1,2)
mysum((3,))

#default argument value
def mysum(n2,n1=0,n3=1):
    return n1+n2
mysum(10)
mysum(4)
mysum(4,6)#4---> n2  , 6---->n1(3)

x=print('dkkkd')
print(type(x))
range(5)
range(1,5)
range(1,5,1)
['1',2,4.5].pop()
['1',2,4.5].pop(1)

#no input has out
def mysum():
    return (1+2)
print(mysum())
x=mysum()
print(x,x+6)


#has input has out
def mysum(num1,num2):
    return (num1+num2)
print(mysum(1,2))
x=mysum(5,2)
print(x,x+6)
#has input no out
def mysum(num1,num2):
    print(num1+num2)
mysum(1,2)
x=mysum(5,2)
print(x)
#no input no out
def mysum():
    print(1+2)
mysum()
def mysum():
    print('mysum function')
#calling
mysum()
print(['1',2,3].pop())
[].copy()
#range
#format
#min
num1=input('enter num1')
num2=input('enter num2')
if(num1.isdigit()):
    num1=int(num1)
else:
    print('num1 must be digit')
if(num2.isdigit()):
    num2=int(num2)
else:
    print('num2 must be digit')

['ahmed',"ali","may"]
x=input('enter list')

#dict collection of values ,diff data type ,key :value
d={
    'id':'1',
    'name':'alaaa',
    'track':'cyber',
    'courses':['linux1','network','python','shell'],
    'gpa':3.9,
    'grade':(100,90,95,80),
    'grade2':{
        'linux':100,
        'python':95
    }
}
d.pop('id')
d1=d# same address
d1=d.copy()#seperated address
print(d.get('grade2'))
d.popitem()
print(d)

for key,value in d.items():
    print(key,value)

for key in d:
    print(key,d[key])
    print(type(key),type(d[key]))



recoredqena={
    'id':'1',
    'name':'alaaa',
    'track':'cyber',
    'courses':['linux1','network','python','shell'],
    'gpa':2.9,
}


recoredqena.update(d)
#+ *

d['plpla']='plpla'
d['grade']=0
d['id']=100
d['grade2']['python']=105
#print(d['grade'][0])


print(d,type(d))
trainees=[
    ['alaaa','2022','cyber','shoag'],
    ['abdel','2020','sys admin','smart'],
    ['pula',2021,'ios','qena']
    
]
print(trainees[0])
print(trainees[1])
print(trainees[2])

#input from user
tables=int(input('enter number'))
#all tables list
largerlist=[]
#generate numbers of tables
for table in range(1,tables+1):
    tablelist=[]
    for num in range(1,table+1):
            tablelist.append(table*num)
    largerlist.append(tablelist)
print(largerlist)
print([[table*num for num in range(1,table+1)] for table in range(1,tables+1)])


#ask user to enter statment
statment=input('enter statment')
#ask user to enter letter
letter =input('enter letter')
l=[]
#loop in statment
for index,ch in enumerate(statment):
    #if current char ==letter
    if(ch==letter):
        l.append(index)
print(l)
#print([value loop get value condition on valaue])
print([index for index,ch in enumerate(statment) if(ch==letter)])

#get index of letter
print([statment.index(letter),statment[statment.index(letter)+1:].index(letter)+statment.index(letter)+1])
'''