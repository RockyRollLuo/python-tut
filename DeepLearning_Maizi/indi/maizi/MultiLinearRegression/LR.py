from numpy import genfromtxt
from sklearn import linear_model

dataPath = r"Delivery.csv"
deliveryData = genfromtxt(dataPath,delimiter=',')

print("data：")
print(deliveryData)

# 所有行，去掉最后一列
x= deliveryData[:,:-1]

# 所有行，最后一列
y = deliveryData[:,-1]

print("输入数据：")
print(x)

print("输出数据：")
print(y)

lr = linear_model.LinearRegression()
lr.fit(x, y)

print(lr)

# 计算出来的参数
print("coefficients:")
print(lr.coef_)

# 计算出来的截距
print("intercept:")
print(lr.intercept_)

xPredict = [[102,6]]
yPredict = lr.predict(xPredict)
print("predict:")
print(yPredict)
