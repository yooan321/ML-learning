# import packages and modules
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay as DBD
from sklearn.linear_model import LogisticRegression

# load the iris dataset and split into x and y
iris = datasets.load_iris()
x = iris.data[:, :2] 
y = iris.target

# load the logistic regression model and fit the data
logi = LogisticRegression(C=1e5)
logi.fit(x, y)

# plot the decision boundary of the logistic regression model
_, ax = plt.subplots(figsize=(4, 3))
DBD.from_estimator(
    logi,
    x,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
    xlabel="Sepal length",
    ylabel="Sepal width",
    eps=0.5,
)

# Plot also the training points
plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors="k", cmap=plt.cm.Paired)


plt.xticks(())
plt.yticks(())

plt.show()


from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load the breast cancer dataset and split into x and y
x, y= load_breast_cancer(return_X_y=True)

# Split the data into training/testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state=42)

# load the logistic regression model and fit the training data
classif = LogisticRegression(max_iter=10000, random_state = 0)
classif.fit(x_train,y_train)

# predict the test set from the model
acc = accuracy_score(y_test, classif.predict(x_test))
print(f"Logistic Regression model accuracy: {acc:.2f}%")


## Multiclass classification with logistic regression
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics

digits = datasets.load_digits()
x = digits.data
y = digits.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)
multi_reg = linear_model.LogisticRegression(max_iter=10000, random_state=3)
multi_reg.fit(x_train, y_train)

y_pred = multi_reg.predict(x_test)

print(f"Logistic Regression model accuracy: {metrics.accuracy_score(y_test, y_pred) * 100:.2f}%")

