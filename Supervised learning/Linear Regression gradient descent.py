# import packages and modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error, r2_score 
import accuracy_score

# split data into x and y from iris
x, y = datasets.load_diabetes(return_X_y=True)

w = np.random.rand(x.shape[1], 1)  # Initialize weights randomly
b = np.random.rand(1)  # Initialize bias randomly

for i in range(100):
    y_hat = np.dot(x, w) + b
    J = (1/np.shape(y)[0]) * np.sum((y_hat - y.reshape(-1, 1)) ** 2)  # Compute cost
    w = w - 0.05 * (2/np.shape(y)[0]) * np.dot(x.T, (y_hat - y.reshape(-1, 1)))
    b = b - 0.05 * (2/np.shape(y)[0]) * np.sum(y_hat - y.reshape(-1, 1))
    # Update weights and bias
    
