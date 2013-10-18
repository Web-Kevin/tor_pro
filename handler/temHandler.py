#coding:utf-8

import tornado.web
from model.entity import Entity
from model.student import Student
from application import env

class TempHandler(tornado.web.RequestHandler):
    def get(self):
        template = env.get_template('mytemplate.html')
        print (template.render())
        
        