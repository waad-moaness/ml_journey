import numpy as np 
class MyLogisticRegression :
    def __init__(self, lr= 0.001 , n_iter = 1000):
        self.wieghts = None
        self.bias = None
        self.n_iter = n_iter
        self.lr = lr


    def fit(self,X,y):
        self.wieghts = np.zeros(X.shape[1])   
        self.bias = 0 
        n_samples = X.shape[0]

        for i in range(self.n_iter): 
            z= np.dot(X, self.wieghts) + self.bias 
            y_predict = self._segmoid(z)

            dw=  (1/n_samples) * np.dot(X.T,(y_predict- y))
            db=  (1/n_samples) * np.sum(y_predict- y)

            self.wieghts -= self.lr * dw
            self.bias -= self.lr *db

    def predict(self,X):
        z= np.dot(X, self.wieghts) + self.bias 
        y_predict = self._segmoid(z)
        y_hat = [1 if y_predict[i] >= 0.5 else 0 for i in range(X.shape[0])]
        return y_hat

    def _segmoid(self,z):
        return 1/(1+ np.exp(-z))
