
import numpy as np
import pandas as pd

# Cargar datos
who = pd.read_csv('LifeExpectancyData.csv')

# Show a simple statistical description
who.describe()

# Show the number of rows and columns/features
who.shape

# Show the low-level type description of the frame
who.info()

# Drop all rows with NaNs
who.dropna(axis=0, inplace=True)

# Show the new number of rows after removing all NaNs
who.shape

# Encode the entire dataset (all features with object type) using one-hot encoding
who_encoded = pd.get_dummies(who)

# Show the keys of the encoded dataset. Note that the target feature has an extra space at the end
who_encoded.keys()

# Separate features from target
X = who_encoded.drop('Life expectancy ', axis=1)
y = who_encoded['Life expectancy ']

# Show the first features (encoded)
X.head()

from sklearn.model_selection import train_test_split

# Split the data into train and test (0.75/0.25 train/test). Shuffle the data
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Create a pipeline with mean scaling and a Multilayer Perceptron with default
# parameters. The normalization is essential for the regressor to work
mlp = make_pipeline(StandardScaler(),MLPRegressor(max_iter=500, learning_rate_init=0.01))
mlp.fit(X_train, y_train)

# Show the R Squared (Coefficient of determination) on both train and test data
mlp.score(X_test, y_test)
from sklearn.metrics import mean_squared_error as mse
#y_pred = mlp.predict(X_test)
print('MLP:', mse(y_test, mlp.predict(X_test), squared = False))

from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor()
dt = DecisionTreeRegressor(max_depth=5)
dt.fit(X_train, y_train)

dt.score(X_test, y_test)
#y_pred = dt.predict(X_test)
print('DT: ',mse(y_test, dt.predict(X_test), squared = False))

import matplotlib.pyplot as plt
from sklearn import tree

fig = plt.figure(figsize=(30,15))
plt.rcParams.update({'font.size': 14})

_ = tree.plot_tree(dt, filled=True)
plt.show()
