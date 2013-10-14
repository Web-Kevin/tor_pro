#coding:utf-8

class Student(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get(name):
        return Student(name)