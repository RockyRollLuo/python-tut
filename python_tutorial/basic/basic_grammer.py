# -*- coding: utf-8 -*-
# @Time    : 2018/1/6
# @Author  : luoqi

import keyword
import sys

# python保留字
print("-----python保留的关键字")
print(keyword.kwlist)

x = 'runoob'
sys.stdout.write(x + '\n')

x = "first line"
y = "second line"
# 输出换行
print(x)
print(y)

# 输出不换行
print(x, end='')
print(y)

# instance 与 type
a = 111
print(isinstance(a, int))
print(type(a))

# 除法，得到一个浮点数
print(2 / 4)

# 除法，得到一个整数
print(2 // 4)

# 取余数
print(17 & 3)

# 乘方
print(2 ** 5)

# String 元素不可修改
str = 'Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

# List 元素可以修改
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

# Tuple 元素不可修改
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号


# 想要函数返回多个值的时候可以利用元组
def examplefunc(a, b):
    return (a, b)


outcome = examplefunc(3, 4)
print("outcome:", outcome)

# Set
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉

a = set('abracadabra')
b = set('alacazam')
print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素,即ab的并集与ab交集的差

# Dictionary
dict_demo = {}
dict_demo['one'] = "1 - 菜鸟教程"
dict_demo[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict_demo['one'])  # 输出键为 'one' 的值
print(dict_demo[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])  # 从序列对中构建字典
dict2 = {x: x ** 2 for x in (2, 4, 6)}
print(dict1)
print(dict2)

# 遍历字典
dict1 = {'abc':1,"cde":2,"d":4,"c":567,"d":"key1"}
for k,v in dict1.items():
    print(k,":",v)