#definations of variables or functions or classs
readmode='r'
modes=('r','a','w','r+')

def readfromtextfile(pathfile,flag,count=0):
    content=''
    f=open(pathfile,'r')
    if(flag=='read' and count>0):
        content=f.read(count)
    elif(flag=='read'):
        content=f.read()
    elif(flag=='line'):
        content=f.readline()
    elif(flag=='lines'):
        content=f.readlines()
    else:
        print('invalid operation')
        content=None
    f.close()
    return content

def writetotextfile(pathfile,content):#content -->string,list of string
    f=open(pathfile,'w')
    if(isinstance(content,str)):
        f.write(content)
    elif(isinstance(content,list)):
        f.writelines(content)
    f.close()

def read():
    print('read from textfileoperation')

