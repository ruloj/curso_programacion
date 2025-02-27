import pandas as pd
from sklearn.datasets import fetch_california_housing
california_housing = fetch_california_housing(as_frame=True)

# Vistazo a los datos
print(california_housing.frame.head())
print(california_housing.data.head())

# Histogramas
import matplotlib.pyplot as plt

california_housing.frame.hist(figsize=(12, 10), bins=30, color="orange", edgecolor="black")
plt.subplots_adjust(hspace=0.7, wspace=0.4)
plt.show()

# ¿Datos atípicos?
atipicos = ["AveRooms", "AveBedrms", "AveOccup", "Population"]
california_housing.frame[atipicos].describe()

# Dividir conjunto de datos
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(california_housing.data, california_housing.target, test_size=0.3, random_state=4)


from sklearn.ensemble import RandomForestRegressor
regresion = RandomForestRegressor()
regresion = RandomForestRegressor(n_estimators=1000, criterion='squared_error', random_state=4, n_jobs=-1)
regresion.fit(X_train, y_train)

# Evaluación
from sklearn.metrics import mean_squared_error as mse
y_pred = regresion.predict(X_test)
mse(y_test, y_pred)

# Importancia de atributos
from matplotlib import pyplot as plt
plt.rcParams.update({'figure.figsize': (6.0, 4.0)})
plt.rcParams.update({'font.size': 12})

plt.barh(california_housing.feature_names, regresion.feature_importances_)
plt.xlabel("Importancia de atributos Random Forest")
plt.show()
