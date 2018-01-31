# -*- coding:utf-8 -*- 
# Created by Rocky on 2018-01-31
import numpy as np


def kmeans(X, k, maxInt):
    '''
    :param X:数据集
    :param k:
    :param maxInt:允许循环的次数
    :return:
    '''
    numPoints, numDim = X.shape

    dataSet = np.zeros((numPoints, numDim + 1)) #增加标签列
    dataSet[:, :-1] = X

    #中心点
    centroids = dataSet[np.random.randint(numPoints, size=k)]
    centroids = dataSet[0:2, :]

    #biaoquianduan
    centroids[:, -1] = range(1, k + 1)

    iterations=0
    oldCentroids=None


