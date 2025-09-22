from sklearn import datasets 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from knn import KNN
import numpy as np 
iris = datasets.load_iris()
X,y = iris.data , iris.target
X_train , X_test , y_train , y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#sklearn KNN
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train,y_train)
y_pred =clf.predict(X_test)
acc= accuracy_score(y_test,y_pred)
print(f'Built in sklearn KNN: {acc}')

#my KNN 
clf2= KNN(k=3)
clf2.fit(X_train,y_train)
y_pred_2 = clf2.predict(X_test)
acc2= accuracy_score(y_test,y_pred_2)
print(f'My KNN: {acc2}')
