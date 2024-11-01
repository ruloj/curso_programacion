import numpy as np
import matplotlib.pyplot as plt     # graficar


def simple_linear_regression(X, y):

    # promedios
    mean_x = np.mean(X)
    mean_y = np.mean(y)

    # Formula ocupada en explicacion de código
    # numerator = sum((X - mean_x) * (y - mean_y))
    # denominator = sum((X - mean_x) ** 2)

    # Formula ocupada en explicacion en parte teorica
    n = len (X)
    numerator = (n * sum(X * y)) - (sum(X) * sum(y))
    denominator = n * sum(X ** 2) - (sum(X) ** 2)

    # calculos
    beta1 = numerator / denominator
    beta0 = mean_y - beta1 * mean_x

    return beta0, beta1

def predict(X, beta0, beta1):
    return beta0 + beta1 * X


# Muestra
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Regresion lineal
intercepcion, pendiente = simple_linear_regression (X, y)

# Resultados de la regresion lineal
print("coeficiente intercepcion (beta0):", intercepcion)
print("pendiente (beta1):", pendiente)

# Conjunto de prueba
X_new = np. array([6, 7, 8, 4,5])
predictions = predict(X_new, intercepcion, pendiente)
print("predicciones para:", predictions)
