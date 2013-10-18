#coding:utf-8


from urls import urls
from jinja2 import Environment , PackageLoader

import tornado.web
import os

env = Environment(loader=PackageLoader(os.path.join(os.path.dirname(__file__), 'templates'))

SETTINGS = dict(
template_path=os.path.join(os.path.dirname(__file__), "templates"),
static_path=os.path.join(os.path.dirname(__file__), "static"),
debug=True
)

application = tornado.web.Application(
                handlers = urls,
                **SETTINGS
)