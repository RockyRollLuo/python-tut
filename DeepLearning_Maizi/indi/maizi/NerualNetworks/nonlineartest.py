import sklearn.neural_network as nn
import numpy as np

nn_model = nn([2, 2, 1], 'tanh')
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
nn_model.fit(X, y)

predict_in=[[0, 0], [0, 1], [1, 0], [1, 1]]
predict_out=nn_model.predict(predict_in)

print(predict_out)