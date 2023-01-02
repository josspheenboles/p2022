'''
import webbrowser
blockwebsites=['http://www.facebook3.com','http://www.twitter.com']
#ftp server
file=open('ahmed.log','w')
for webs in blockwebsites:
    res= webbrowser.open(webs,new=2)
    file.write(res)
file.close()

from sys import *
from socket import *
#ip='127.0.0.1'
ip=argv[1]
tagrethostname=gethostbyname(ip)
try:
    for port in range(1,65535):
        socketobject=socket(AF_INET,SOCK_STREAM)
        setdefaulttimeout(1)
        result=socketobject.connect_ex((tagrethostname,port))
        if result==0:
            print('port',port,'is opened')
        socketobject.close()
        print(port)
except KeyboardInterrupt:
    print('existting program')
except gaierror:
    print('hostnam could not resolved')
except error:
    print('server not responding')
except:
    print(exc_info()[1])
'''