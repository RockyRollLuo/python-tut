# -*- coding:utf-8 -*- 
# @date: 2018-01-09
# @author: rocky

try:
    f = open('basic_file_test.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error is {}".format(err))
except ValueError:
    print("Could not convert data to an integer")
print(i)