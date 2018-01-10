# -*- coding: utf-8 -*-
# @Time    : 2018/1/9
# @Author  : Rocky

import numpy as np

import tensorflow as tf

# x_data 2行100列
x_data = np.float32(np.random.rand(2, 100))
# dot(a1,a2):a1与a2点积
y_data = np.dot([0.1, 0.2], x_data) + 0.300

# y=Wx+b 构造线性模型
b = tf.constant(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1, 1))
y = tf.matmul(W, x_data)

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()

# 启动图
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
