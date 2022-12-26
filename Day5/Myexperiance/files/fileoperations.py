#definations function,variable,class
#nocall to function,no print out scope function
defaultpath='c:\\'
modes=('r','w','a','r+')

def read(path):
    files=open(path,'r')
    content =files.read()
    files.close()
    return content

def write(path,content):
    print('written')

def update(path,content):
    print('updated')

