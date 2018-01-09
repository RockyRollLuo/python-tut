# -*- coding:utf-8 -*- 
# @date: 2018-01-09
# @Author: rocky

# 写文件
some_sentences = '''\
I love python
because python is fun
and python is easy to use
'''
f = open('basic_file_test.txt', 'w')
f.write(some_sentences)
f.close()

# 读文件
f = open('basic_file_test.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end="")
f.close()
