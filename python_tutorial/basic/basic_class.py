# -*- coding: utf-8 -*-
# @Time    : 2018/1/6
# @Author  : Rocky

# 类定义
class people:
    # 定义基本属性    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问 两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。
    __weight = 0

    # 定义构造方法 ,在生成对象使调用
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def __del__(self):
        print(self.__class__,"对象消失了！")

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()


# 单继承示例 student继承people，多继承用逗号隔开
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    def __foo(self):  # 私有方法,两个下划线开头，声明该方法为私有方法，只能在类的内部调用
        print('这是私有方法')

    # 覆写父类的方法
    def speak(self):
        self.__foo()
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()
