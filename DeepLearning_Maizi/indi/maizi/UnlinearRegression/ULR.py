import numpy as np
import random


def genData(numPoints, bias, variance):
    '''生成数据
    :param numPoints: 样本个数，行数
    :param bias: 偏差
    :param variance: 方差
    :return:输入x,输出y
    '''
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=(numPoints))
    for i in range(0, numPoints):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0, 1)*variance
    return x, y

def gradientDescent(x, y, theta, alpha, m, numIterations):
    '''梯度下降
    :param x: 输入
    :param y: 输出
    :param theta: 参数
    :param alpha: 学习率
    :param m: 实例数
    :param numIterations: 迭代次数
    :return:
    '''
    xTran = np.transpose(x) #转置矩阵
    for i in range(numIterations):
        hypothesis = np.dot(x, theta) #x和thera点积得假定值
        loss = hypothesis - y #损失值
        cost = np.sum(loss ** 2) / (2 * m) #损失函数
        gradient = np.dot(xTran, loss) / m #梯度
        theta = theta - alpha * gradient
        print("Iteration %d | cost :%f" % (i, cost))
    return theta


x, y = genData(100, 25, 10)
print("x:")
print(x)
print("y:")
print(y)

m, n = np.shape(x) # X的行数和列数
m_y = np.shape(y)  #y的行数

print("m:" + str(m) + " n:" + str(n) + " n_y:" + str(m_y))

numIterations = 100000 #迭代次数
alpha = 0.0005 #学习率
theta = np.ones(n)
theta = gradientDescent(x, y, theta, alpha, m, numIterations)
print(theta)
