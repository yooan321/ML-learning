import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay as DBD
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
x = iris.data[:, :2] 
y = iris.target


logi = LogisticRegression(C=1e5)
logi.fit(x, y)

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