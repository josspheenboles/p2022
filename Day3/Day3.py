l=input('enter list in formate ["name1","name2",.....,"name2"]')
print(l)
'''
name='global'#global var
def outer():
    name='outer'
    def inner():
        #nonlocal name
        global name
        print(name)
        name = 'inner'
    inner()
    print(name)
outer()
print(name)

def mysum(n1,n2):
    print(n1+n2)
n1=float(input('enter numb1'))
n2=float(input('enter numb2'))
mysum(n1,n2)

x,*y,z,m=1,'one',1.3,True,4,'sdd'
print(x,y,z,m)


name='farouk'
l=[]
for ch in name:
    l.append(ch.capitalize())
print(l)
print([ch.capitalize() for ch in name])

l=[]
for x in range(10):
    if(x%2==0):
        l.append(x)
print(l)
#[output loop conditionoptionsl]
print([x for x in range(10) if(x%2==0)])

print(type(x))


"""
'sdf{key}'.format(key='val')
"""
#unlimited key ,generate random key
print('i love {lang} {lang2}'.format(lang='python',lang2='java'))
#** before --->dict
def mysum(**dic):
    #print(type(dic),dic)
    s=0
    for key in dic.values():
       #s+=dic[key]
        s+=key
    print(s)
mysum(x=1,y=3,z=10,asd=10)

mysum(jj=1,num2=3,asd=10)
mysum(x=1,y=3)

#tuple or list place befor it *
#place * before variable as function arg---->tuple
#place * before variable --->list

"""
min(1.....10)
max(1......10)
"""
def mysum(*t):# t as tuple
    s=0
    for x in t:
        s+=x
    print(s)
mysum(1,2,3,4,5)
mysum(1,2)


"""
range(5)
range(1,5)
range(1,5,1)
"""
def mysum(y,z,x=10,m=40):
    print(x+y+z+m)
mysum(y=60,x=100,z=1000)


def convertstrtofloat(num):
    if (num.isdigit()):
        return  float(num)
    else:
        print('invalid numbers')
        return None
#functions
num1=convertstrtofloat(input('enter num1'))
num2=convertstrtofloat(input('enter num2'))
operation=input('enter operation + - *')
if(num1 is not None and num2 is not None):
    if(operation=='+'):
            print((num1)+(num2))
    elif(operation=='-'):
            print((num1)-(num2))
    elif(operation=='*'):
            print((num1)*(num2))
    else:
        print('invalid operation')


#no input no output
def mysum():
    print(1+2)

print(mysum)
#call
mysum()
#input arg no out
def mysum(num1,num2):
    print(num1+num2)
print(mysum)
#call
mysum(1,3)
#input arg  out
def mysum(num1,num2):
    return (num1+num2)

print(mysum)
#call
res=mysum(1,3)
print(res,res+10)
#no input  output
def mysum():
    return (1+2)

print(mysum)
#call
res=mysum()
print(mysum())




d1={'id':1}
d2={'id':3,'name':'sara'}
d2.update(d1)
print(d2)

l=['ahmed','sara']
l2=[1,2]
d={}
for index,k in enumerate(l2):
    #d.update({str(k):l[index]})
    d[str(k)]=l[index]
print(d)

trainee={'id':1}
d={'name':'ali','id':2}
merg={'name':'aya'}
merg.update(d)
print(merg)

print(trainee+d) # + & * unsupported

trainee={
    'id':1, 'name':'ali',
    'courses':['python','admin1','shell sc'],
    'grades':(100,2,3,4,100),
    'isgraduate':False,

}
print(trainee*2)

trainee['a']='ahmed'
print(trainee)
trainee['a']='ali'
print(trainee)

for key ,val in trainee.items():
    print(key,val)


for val in trainee.values():#list of values
    print(val)
for key in trainee.keys():#list of key
    print(key,trainee[key])

trainee['courses'][0]='PYTHON'
trainee['grades'][4]=50
print(trainee['grades'][4])
print(trainee['courses'][0],type(trainee['courses']))

trainees={
    '1':trainee,
    '2':{'id':2,'name':'ahmed'}
}
print(trainees)
trainees['2']['name']='asd'
print(trainees['2'])

d['courses']='python'
d['nationalnumber']=1234567891234
print(d,type(d))
print(d['courses'])
'''