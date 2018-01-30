# -*- coding:utf-8 -*- 
# Created by Rocky on 2018-01-30

import math
import numpy as np

def computeCorrelation(X,Y):
    '''计算相关系数
    :param X:
    :param Y:
    :return:
    '''
    E_X=np.mean(X)
    E_Y=np.mean(Y)

    SSR=0
    D_X=0
    D_Y=0

    for i in range(len(X)):
        diff_X_EX=X[i]-E_X
        diff_Y_EY=Y[i]-E_Y
        SSR+=diff_X_EX*diff_Y_EY
        D_X+=diff_X_EX**2
        D_Y+=diff_Y_EY**2

    SST=math.sqrt(D_X*D_Y)
    return SSR/SST