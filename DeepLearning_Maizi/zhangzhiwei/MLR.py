# -*- coding:utf-8 -*-
from numpy import genfromtxt
from sklearn import linear_model
import math

datapath = r"data.csv"
data = genfromtxt(datapath, delimiter=",")

# 第一行（CF,STD,NWC,Expendit,SIZE,TobinsQ,FIN,FINCF,CASH）
x = data[1:, :-1]
y = data[1:, -1]

# 80%作为训练集，20%作为测试集  这么做不太好，最好的是做交叉验证
# 交叉验证：把数据集分成k等分，依次把其中一份作为测试集，其余k-1份作为训练集，求出k个准确率的平均值
data_size = len(x)
train_size = int(data_size * 0.8)
test_size = data_size - train_size

train_x=x[:train_size,:]
train_y=y[:train_size]

test_x=x[train_size:,:]
test_y=y[train_size:]


MLRModel = linear_model.LinearRegression()

MLRModel.fit(train_x, train_y)

# print(mlr)
# print("coef:")
# print(mlr.coef_)
# print("intercept")
# print(mlr.intercept_)

predict_y = MLRModel.predict(test_x)

print("predict_y")
print(predict_y)
print("test_y")
print(test_y)


correct_count=0
for i in range(test_size):
    # y的值都为小数，预测结果不可能小数点后面那么多位全一模一样，大约近似就可认为准确
    # 当设为 误差设为0.1时，准确率可达90%
    if math.fabs(predict_y[i]-test_y[i])<=0.1 :
        correct_count+=1

correct_precent=float(correct_count)/test_size
print("准确率："+str(correct_precent))

