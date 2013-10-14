#coding:utf-8

from handler.index import MainHandler 
from handler.index import TestHandler
from handler.index import StoryHandler
from handler.index import StrtestHandler


urls = [
        
        (r'/', MainHandler),
        
        (r'/student', TestHandler),
        
        (r'/story/([0-9]+)', StoryHandler),
        
        (r'/strTest', StrtestHandler),

        ]

