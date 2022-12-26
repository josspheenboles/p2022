import sys
import socket

#input from user ip
#args=sys.argv#['script name',ip]--> 2items
path="log.txt"
if(len(['',''])==2):
    targetserver='127.0.0.1'#args[1]

    try:
        target = socket.gethostbyname(targetserver)
        for port in range(1,65535):#range of ports
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(.5)
            result=s.connect_ex((target,port))
            if(result==0):
                f=open(path,'a')
                f.write('port '+str(port)+ ' is open')
                f.close()
            s.close()
            print(port)
    except KeyboardInterrupt:
        print('exitting program!!!')
        sys.exit()
    except socket.gaierror:
        print('hostname not resolved')
        #sys.exit()
    except socket.error:
        print('server not responding')
        sys.exit()
    except:
        print('exception')
        sys.exit()
else:
    print('invalid argument')
'''
import Myexperiance.network.network
Myexperiance.network.network.configurestaticip('192.168.5.12')
from Myexperiance.network.network import configurestaticip
configurestaticip('192.168.2.1')


from  ciscomodule import *
ciscoconfiureswitch()#module
def ciscoconfiureswitch():
    print('main ciscoconfiureswitch')
ciscoconfiureswitch()#main
import ciscomodule
ciscomodule.ciscoconfiurerouter()
ciscomodule.ciscoconfiureswitch()
'''
