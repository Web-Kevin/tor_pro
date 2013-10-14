#coding:utf-8

import tornado.web
import torndb
from model.entity import Entity
from model.student import Student
from Jinja2 import Template

db=torndb.Connection('192.168.116.128','test',user='root',password='111')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
#         string = 'wawuee'
        exe = "insert into mytable (name,sex) values ('kevin','1')"
        db.execute(exe)
        entity = Entity.get('the5fire\'s blog')
        self.render('index.html', entity = entity)
    def post(self):
        self.set_header("Content-Type", "text/plain")
        print('into it')
        self.write(self.get_argument('strTest' ,default = None, strip=True))
        
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        student = Student.get('name')
        self.render('user.html', student = student)
        
class StoryHandler(tornado.web.RequestHandler):
    def get(self,story_id):
        self.write('your story' + story_id)
        
class StrtestHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("charset", "utf-8")
        test = self.get_argument('strTest' ,default = None, strip=True)
        self.write('hello'+ '我' + test)
        
class JinjaHandler(tornado.web.RequestHandler):
    def get(self):
        template = Template('Hello {{name}}!')
        template.render(name='world')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        