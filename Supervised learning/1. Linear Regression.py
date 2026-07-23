# import packages and modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error, r2_score 

# split data into x and y from iris
iris_x, iris_y = datasets.load_iris(return_X_y=True)

#split dependent variables into train and test sets 67/33 split 
iris_x_train = iris_x[:-50]
iris_x_test = iris_x[-50:]

# Split the targets into training/testing sets
iris_y_train = iris_y[:-50]
iris_y_test = iris_y[-50:]

# load the linear regression model and fit the training data
linreg = linear_model.LinearRegression()
linreg.fit(iris_x_train, iris_y_train)

# predict the test set from the model
iris_y_pred = linreg.predict(iris_x_test)

# print out the linear regression model coefficients, mean squared error, and coefficient of determination
print("Coefficients: \n", linreg.coef_)
print("Mean squared error: %.2f" % mean_squared_error(iris_y_test, iris_y_pred))
print("Coefficient of determination: %.2f" % r2_score(iris_y_test, iris_y_pred))

# plot the test set and the predicted values from the model
plt.scatter(iris_x_test, iris_y_test, color='black')
plt.plot(iris_x_test, iris_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

# load the breast cancer dataset and split into x and y
x, y = datasets.load_breast_cancer(return_X_y=True)

# Split the data into training/testing sets
x_train = x[:-50]
x_test = x[-50:]

# Split the targets into training/testing sets
y_train = y[:-50]
y_test = y[-50:]

linreg = linear_model.LinearRegression()
linreg.fit(x_train, y_train)

y_pred = linreg.predict(x_test)

print("Coefficients: \n", linreg.coef_)
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))
plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

