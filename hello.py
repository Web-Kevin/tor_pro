#!/usr/bin/env python
#! coding: utf-8
import tornado.ioloop
import tornado.web
import os
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write(self.get_argument('strTest' ,default = None, strip=True))

SETTINGS = dict(
template_path=os.path.join(os.path.dirname(__file__), "templates"),
static_path=os.path.join(os.path.dirname(__file__), "static"),
debug=True
)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8285)
    tornado.ioloop.IOLoop.instance().start()