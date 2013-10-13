'''
Created on 2013-10-8

@author: kevin
'''
#coding:utf-8

import tornado.ioloop
import sys

from application import application

PORT = '8000'

if __name__ == "__main__":
    print('method into main') 
    if len(sys.argv) > 1:
        PORT = sys.argv[1]
        print('method into if else') 
    print('method app') 
    try:
        application.listen(PORT)
    except:
        pass
    print ('Development server is running at http://127.0.0.1:%s/' % PORT)
    print ('Quit the server with CONTROL-C')
    tornado.ioloop.IOLoop.instance().start()
