import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np

# Cargar datos
X, y = fetch_openml("mnist_784", version=1, return_X_y=True)

# Para visualizar un dígito
# Elige la imágen (instancia) 38,000
some_digit = X.iloc[[38000]].to_numpy() 
some_digit_image = some_digit.reshape(28, 28)
plt.imshow(some_digit_image, cmap = matplotlib.cm.binary, interpolation="nearest")
plt.axis("off")
plt.show()

# Normaliza la intensidad de las imágenes para que queden en el rango [0,1]
X = X / 255.0

# Divide los datos en conjuntos de entrenamiento y evaluación
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

# Construir el clasificador
classifier = MLPClassifier(
    hidden_layer_sizes=(50,20,10),
    max_iter=100,
    alpha=1e-4,
    solver="sgd",
    verbose=False,
    random_state=1,
    learning_rate_init=0.1,
)
# Ajusta el modelo sobre los datos de entrenamiento
classifier.fit(X_train, y_train)


# Predicción
predicted = classifier.predict(X_test)

# Evaluación
from sklearn.metrics import ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Matriz de confusión")
print(f"Matriz de confusión:\n{disp.confusion_matrix}")
plt.show()


print("Training set score: %f" % classifier.score(X_train, y_train))
print("Test set score: %f" % classifier.score(X_test, y_test))


