from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from Logistic_regression import MyLogisticRegression
import warnings
warnings.filterwarnings('ignore')

canser = load_breast_cancer()
X,y = canser.data , canser.target 

X_train ,X_test , y_train , y_test = train_test_split(X,y, test_size=0.2, random_state=42)
lr = LogisticRegression()
lr.fit(X_train,y_train)
y_pred= lr.predict(X_test)
acc= accuracy_score(y_test,y_pred)
print(f'built in model = {acc:.2f}')


my_lr = MyLogisticRegression()
my_lr.fit(X_train,y_train)
my_y_pred = my_lr.predict(X_test)
my_acc= accuracy_score(y_test,my_y_pred)
print(f'my model = {my_acc:.2f}')