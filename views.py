# -*- coding:utf-8 -*-
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self):
        return self.name

    def __str__(self):
        return "哈哈{}".format(self.name)



person = Person('long', 19, 'M')

