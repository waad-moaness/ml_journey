from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
X,y = make_regression(n_samples= 100 , n_features=1 ,noise=20 , random_state=4)

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=1234)

lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)
MSE = mean_squared_error(y_test,y_pred)

print(f'Built in Linear Regression: \n MSE = {MSE:.2f}     ')

from linear_regression import MyLinearRegression
my_lr = MyLinearRegression(learning_rate=0.01)
my_lr.fit(X_train,y_train)
my_y_pred = my_lr.predict(X_test)
MSE2 = mean_squared_error(y_test,my_y_pred)
print(f'My Linear Regression: \n MSE = {MSE2:.2f}     ')

plt.scatter(X,y,c='r')
plt.plot(X_test,my_y_pred,c='g')
plt.plot(X_test,y_pred,c='b')
plt.show()