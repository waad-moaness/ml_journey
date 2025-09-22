import numpy as np
from collections import Counter

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)** 2))

class KNN :
    def __init__(self,k):
        self.k =k
    
    def fit(self,x,y):
        self.x= x
        self.y = y

    def predict(self,x):
        predictions = [self._predict(i) for i in x]
        return np.array(predictions)

    def _predict(self,x):
        knn_distance= [euclidean_distance(x,i) for i in self.x]
        knn_indexes= np.argsort(knn_distance)[:self.k]
        knn_lable = [self.y[i] for i in knn_indexes]
        most_common= Counter(knn_lable).most_common(1)[0][0]
        return most_common
