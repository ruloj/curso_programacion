import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score

diabetes = datasets.load_diabetes()

diabetes.feature_names
df = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)
df['measure'] = diabetes.target
df.head()

# Graficar dos variables
x = df['bmi']
y = df['measure']
plt.scatter(x, y, marker='o') 
plt.xlabel('bmi')
plt.ylabel('measure')
plt.show()

sns.regplot(x="bmi", y="measure", data=df)

# Preparar datos
X = df.iloc[:,0:10]
y = df.iloc[:,10]

from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=0)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)


dict_coef =  dict(zip(diabetes.feature_names,lr.coef_.round(3))) 
dict_coef['Intercept'] = lr.intercept_.round(3)  
print(dict_coef)

# Evaluación
from sklearn.metrics import root_mean_squared_error
print(root_mean_squared_error(y_test, y_pred))
