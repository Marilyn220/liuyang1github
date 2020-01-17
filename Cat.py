# -*- coding:utf8 -*-
class Cat:
    # 属性
    def __init__(self,new_name,new_age):
        self.name=new_name
        self.age = new_age
    def __str__(self):
        return "%s的年龄是:%d" % (self.name, self.age)"
    # 方法
    def eat(self):
        print("猫吃饭")

    def drink(self):
        print("猫喝水")

    def introduce(self):
        print("%s的年龄是:%d" % (self.name, self.age))


# 创建对象
tom = Cat("tom",40)
tom.eat()
tom.drink()
#om.name = tom
#om.age = 20
tom.introduce()

lanmao = Cat("lanmao",10)
lanmao.eat()
lanmao.drink()
#anmao.name = lanmao
#anmao.age = 10
lanmao.introduce()