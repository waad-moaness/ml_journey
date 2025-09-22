import numpy as np 

class MyLinearRegression:
    def __init__(self,learning_rate=0.001,n_iter= 1000):
        self.learning_rate= learning_rate
        self.n_iter = n_iter
        self.weights = None
        self.bias = None
    
    def fit(self,X,y):
        self.X_train = X
        self.y_train = y
        self.weights = np.zeros(self.X_train.shape[1])
        self.bias = 0
        self.gradient(self.X_train , self.y_train)

    def predict(self,X):
        predictions = np.dot(X,self.weights)+ self.bias
        return np.array(predictions)

    def gradient(self,X,y):
        n_samples = X.shape[0]
        for i in range(self.n_iter):
            y_hat= np.dot(X,self.weights) + self.bias
            j_w =(1/(n_samples*2))* np.dot(X.T,(y_hat - y ))
            j_b= (1/(n_samples*2))* np.sum(y_hat - y ) 
            self.weights -= self.learning_rate * j_w
            self.bias -= self.learning_rate * j_b

