import numpy as np


def tanh(x):
    return np.tanh(x)


# tanh的导数
def tanh_deriv(x):
    return 1.0 - np.tanh(x) * np.tanh(x)


def logistic(x):
    return 1 / (1 + np.exp(-x))


# logistic 的导数
def logistic_deriv(x):
    return logistic(x) * (1 - logistic(x))


class NeuralNetwork:
    # 构造函数
    def __init__(self, layers, activation="tanh"):
        '''
        :param layers: A list containing the number if units in each layer should be at least two values
        :param activation: The activation function to be used. Can be "logistic" or "tanh"
        '''
        if activation == "logistic":
            self.activation = logistic
            self.activation_deriv = logistic_deriv
        elif activation == "tanh":
            self.activation = tanh
            self.activation_deriv = tanh_deriv

        self.weights = []
        # 为所有 w 赋值
        for i in range(1, len(layers) - 1):
            self.weights.append((2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1) * 0.25)
            self.weights.append((2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1) * 0.25)
            print(str(self.weights))

    def fit(self, x, y, learning_rate=0.2, epochs=10000):
        x = np.atleast_2d(x)
        temp = np.ones([x.shape[0], x.shape[1] + 1])
        temp[:, 0:-1] = x
        x = temp
        y = np.array(y)

        for k in range(epochs):
            i = np.random.randint(x.shape[0])  # x.shape[0] is the number of the trainingset samples
            a = [x[i]]  # choose a sample randomly to train the model
            print(str(a))
            for l in range(len(self.weights)):
                # print("a["+str(l)+"]; "+str(a[l])+"  WEIGHT "+str(self.weights[l])+str(len(self.weights)))
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            error = y[i] - a[-1]
            deltas = [error * self.activation_deriv(a[-1])]

            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_deriv(a[l]))
            deltas.reverse()

            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        print("start")
        x = np.array(x)
        temp = np.ones((x.shape[0] + 1,x.shape[1]))
        print(temp.shape)
        temp[0:-1] = x
        a = temp
        for l in range(len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


