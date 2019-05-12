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


def login(request):
    if request.method.GET = 'get':
        return render(request, 'login.html')
    elif request.method.GET = 'post':
        name = request.GET.get('uname')
        pwd = request.GET.get('pwd')
        if name == 'long' and pwd == 'pythonvip':
            return HttpResponse('登录成功')
        else:
            return render(request, 'login.html')


person = Person('long', 19, 'M')

