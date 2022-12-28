#date msg user
str1='{date} msg {user} {date}'
print(str1.format(user='ali',date='28-12-2022'))
print(str1.format(user='ali',date='29-12-2022'))
'''
print(str1.format('28-12-2022','ali'))
print(str1.format('ali','28-12-2022'))

x,y=1,2
print(x,y)
x,y=y,x
print(x,y)

x,y=1,2
print(x,y)
temp=x
x=y
y=temp
print(x,y)
#string

name='ahmed Ali'
print(name.capitalize())
print(name.lower())
print(name.upper())


print(name[name.index('a')+1:].index('a')+1)
print(name.index('a'))#first index of occurance
print(name.count('a'))

print(name+' asd')
print(name*2)

#name[startindex=0:stopindex=len of str:step=1]
print(name[::-1])

print(name[0:4:1])
print(name[-1:4:-1])
print(name[::-1])

print(name[-1])

print(name)
print(name[0])
print(name[9])

print(name.replace('a','@',1))
print(name.isdigit())   
print(name.count('ahl'))
print(len(name))
print(name)


print(name.split(' '))
print(type(name))
#'',"" single line of string
#''' '''',""" """ multiline of string
name="""x
name

y
"""
print(name)

num='11'
print(int(num))
print(float(num))
print(complex(num))

print(min(-1,1.1, 1000,1000.1))
print(max(-1,1.1, 1000,1000.1))
print(round(1.5))
print(round(1.1))


#float int complex
num=1.4
print(type(num))
num=int(num)
print(type(num))
num=1+1j
print(type(num))

print(True and False and True)
print(2 and 0 and 1)#true and false
print(2 and 5)#true and true
print(2 or 5)#true 2
print(0  or 0 or 5)#false or false or true

print(False or False or False)

num=input('Enter number ')
num=float(num)
print(type(num))
print(num+1)

num=1.1
print(type(num))
num=1
print(type(num))
num='one'
print(type(num))
num=True
print(type(num))
_7num=1
print(_7num)
'''
