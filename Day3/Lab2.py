#input number as int
n=int(input('enter number '))
#loop on list multiplication table numbers
largelist=[]
for tablenumber in range(1,n+1):
    tablelist=[]
    #loop on 1 to 12
    for x in range(1,tablenumber+1):
        #multiply table number * [1:12]
        tablelist.append(tablenumber*x)
    largelist.append(tablelist)
print(largelist)
print([[tablenumber*x for x in range(1,tablenumber+1)] for tablenumber in range(1,n+1)])
'''
#input statment
statment='this is'#input('enter statement')
indexs=[]
#input letter
letter='i'#input('enter letter')
#loop on statment
for index,x in enumerate(statment):
    #if lettet == x
    if letter==x:
        #get index
        indexs.append(index)
print(indexs)
print([index for index,x in enumerate(statment) if letter==x])


print(statment,statment.index('i'))
print(statment[3:],3+statment[3:].index('i'))
'''