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


# Muestras
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

conjunto_y = []
# lineal
conjunto_y.append(np.array([2, 4, 5, 4, 5, 7, 8, 7, 9, 10]))

# no lineal
conjunto_y.append(np.array([16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]))

# aleatoria
conjunto_y.append(np.random.rand(10) * 30)


# Conjunto de prueba
X_test = np.array([11, 12, 13, 14])


# Visualización de los tres conjuntos
titles = ['Conjunto 1: Lineal', 'Conjunto 2: No Lineal', 'Conjunto 3: Aleatorio']
plt.figure(figsize=(15, 5))

for i, y in enumerate(conjunto_y):
    beta0, beta1 = simple_linear_regression(X, y)
    predictions = predict(X, beta0, beta1)
    test_predictions = predict(X_test, beta0, beta1)

    plt.subplot(1, 3, i+1)
    plt.scatter(X, y, label='Datos Originales')
    plt.plot(X, predictions, color='red', label=f'Línea de ajuste: y = {beta1:.2f}x + {beta0:.2f}')
    plt.scatter(X_test, test_predictions, color='orange', marker='x', label='Conjunto de Prueba')
    plt.title(titles[i])
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', borderaxespad=0, ncol=1)

plt.tight_layout()
plt.show()