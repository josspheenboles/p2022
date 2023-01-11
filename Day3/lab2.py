#function
error='{ahmed},{date}'
print(error.format(ahmed='psldpspld',date='sdd'))
def mysum(**xx):
    print(type(xx))
    s=0
    for x in xx.values():
        s+=x
    print(s)
mysum(xx=1,y=4)
mysum(ali=1,ahmed=4,x=1000)
d={'id':1,'name':'ali'}
print(d.values())
print(d.keys())

'''
def mysum(*values):#as tuple
    print(type(values))
    print(values)
    s=0

    for val in values:
        s+=val
    print(s)

mysum(1,2)
*x,y,z=1,2,3,45,67
print(x,type(x))
x=1,2,1001,303,506,3030

mysum(1,2,1001,303,506,3030)



def mysum(n1,n2=-1,n3=0):
    print(n1+n2+n3)
mysum(1,2,3)
mysum(1,2)
mysum(1)

range(1,4,1)
range(1,4)
range(4)
def mysum(n2,n1=0,n3=1):
    return n1+n2+n3
mysum(1,2,3)#n2,n1,n3
mysum(1,2)#n2,n1,n3=1
mysum(2)#n2,n1=0,n3=1

#defination
def mysum(n1,n2,n3,n4):
    return n1+n2
#calling
print(mysum(1,2,1,1))
print(mysum(10,20,3,4))

n1=(input('enter num1'))
if(n1.isdigit()):
    n1=float(n1)
else:
    print('number must be digit')

#defination function
def convertstrtofloat(n1):
    if (n1.isdigit()):
        return float(n1)
    else:
        print('number  must be digit')
        return None
#calling
print(convertstrtofloat('10A'))

n1=input('enter num1')
n1=convertstrtofloat(n1)
n2=input('enter num1')
n2=convertstrtofloat(n2)
if(n1 is not None and n2 is not None):
    print(n1+n2)
else:
    print('number is not correct')



#handel error
#dict collection of values different data type key unique:value
d1={'1':'python','2':'ruby'}
d2={'name':'ali','1':'C#'}
d1.update(d2)
print(d1)
print(d2)
#print(d1+d2)
print(d1*2)

d={
    'id':12,
    'name':'ahmed',
    'track':'sys admin',
    'q':4,
    'branch':'qena',
    'courses':['python','admin1','admin2'],
    'grades':(100,20,50),
    'grades2':
        {
            'python':100,
            'admin1':50,
            'admin2':20
        }
}

traineee={
  '1':d,
  '1':{'id':2,'name':'ali'}
}
traineee['2']='plpp|'
traineee['2']='test'
print(traineee)
opensoucrlang={
    '1':  {
            'python':100,
            'admin1':50,
            'admin2':20
        },
    '2':'ruby',

}
opensoucrlang['1']['python']=11
print(opensoucrlang['2'][1])
print(opensoucrlang)

print(opensoucrlang.items())
for x in opensoucrlang.items():
    print(x)
    print(opensoucrlang)
print(opensoucrlang.pop('1'))
print(opensoucrlang)
print(d.pop('courses'))
print(d)
d['id']=1
d['name']='ahmed ali'
d['courses']=''
d['plpalp']='plplplpa'
print(d)
print(d['grades'],type(d['grades']))

print(type(d),d)

trainee=[
    [1,'ahmed','sys admin','q4','qena'],
    [2,'ali','sys admin','q4','smart'],


]
print(trainee[0])
l=[]
for x in range(0,21):
    if(x%2==0):
        l.append(x)
print(l)
#print([value loop condition])
l=[ x for x in range(0,21) if(x%2==0)]
print(l)
#list ,tuple,dict
x,y,*z=1,1.1,'one',True
print(x,y,z)
z,m=1,2
print(z,m)
m,z=z,m
print(z,m)
opensource='python','ruby'
x,y=opensource
print(x,y)
n1,n2=(1,2)
print(n1,n2)
opensource=opensource+('sss',)
commer=('sql','C#')
print(opensource+commer)
print(opensource)
print(commer)
severs=('server1','server2')
print(severs)
severs=('server4','server3')
print(severs)
t=('192.168.5.1','333')
for x in range(1000):
    print(x)
t='one',#tuple of one value ---> value,
print(type(t),t)

t=1,1.1,True,[3,4],('test','asd'),{},'sdsdsd'
#t[0]=100#tuple immutible list
print(type(t),t)
print(t[1:4])
print(t[1:])
print(t[:4])
print(t[-1])
print(t[::-1])
print(t[0],type(t[0]))
print(t[4],type(t[4]))
print(type(t),t)
#input from user statment
statment=input('enter statment')
#input from user letter
letter =input('enter letter')
index=0
l=[]
for ch in statment:
    if(ch==letter):
        #l.append(index)
        l.insert(0,index)
    index+=1
print(l)

#input from user statment
statment=input('enter statment')
#input from user letter
letter =input('enter letter')
#get index
count=0
l=[]
for ch in statment:
    if(ch==letter):
       l.append(count)
       #l.insert(0,count)
    count+=1
print(l)




flag='y'
while(flag=='y'):
    n1 = input('enter number1')
    if(n1.isdigit()):
        n1 = float(n1)
    else:
        print('n1 must be digit ')
        break
    n2 = float(input('enter number2'))
    operation = (input('enter operation + - / *'))
    if(operation=='+'):
        print(n1+n2)
    flag=input('enter y to cont.')
'''