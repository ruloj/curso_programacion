from pydataset import data
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Get the data
titanic = data('titanic')
# print(titanic.sample(5))

# Feature engineering (one hot encoding)
titanic = pd.get_dummies(titanic, drop_first=True)#.astype(int)
# print(titanic.sample(5))

# Test train split
X_train, X_test, y_train, y_test = train_test_split(titanic.drop('survived_yes', axis=1), titanic['survived_yes'])

# Train the model using the training data
LogReg = LogisticRegression(solver='lbfgs')
LogReg.fit(X_train, y_train)

# Prediciting if a class-1 child-age girl survided
print(LogReg.predict(np.array([[0,0,1,1]]))[0])

# Prediciting if a class-3 adult-age man survided
print(LogReg.predict(np.array([[1,1,0,1]]))[0])

# Scoring the model
print("score:", LogReg.score(X_test, y_test))