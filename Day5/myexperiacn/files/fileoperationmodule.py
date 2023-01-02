#defination variables functions class
#no call functio in globalscope,no print var in global scope
modes=['r','w','a','r+']
binarymodes=('rb','rb+')

def read(path):
    file=open(path,modes[0])
    content=file.read()
    file.close()
    return content

def write(path,content):
    print('content written')

def update(path,content):
    print('content updated')