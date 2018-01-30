# -*- coding:utf-8 -*- 
# Created by Rocky on 2018-01-29

from sklearn import datasets
from sklearn import neighbors

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

# print(iris)

knn.fit(iris.data, iris.target)

predictendLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])

print(iris.target_names)

print(predictendLabel)

print(iris.target_names[predictendLabel[0]])
