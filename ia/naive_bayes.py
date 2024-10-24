import pandas as pd
import numpy as np

# Función para calcular las probabilidades a priori
def prior_prob(df, label_column):
    return df[label_column].value_counts(normalize=True)

# Función para calcular las probabilidades condicionales
def conditional_prob(df, feature_column, feature_value, label_column, label_value):
    # Subconjunto donde la clase es igual a `label_value`
    subset = df[df[label_column] == label_value]
    # Aplicamos suavizado de Laplace
    return (subset[feature_column].value_counts().get(feature_value, 0) + 1) / (len(subset) + df[feature_column].nunique())

# Función para predecir la clase de una instancia
def predict(instance, df, label_column):
    classes = df[label_column].unique()
    class_probs = {}

    for label in classes:
        # Inicializamos la probabilidad con la a priori
        class_probs[label] = np.log(prior_prob(df, label_column).get(label))

        # Multiplicamos por las probabilidades condicionales de cada característica
        for feature_column, feature_value in instance.items():
            class_probs[label] += np.log(conditional_prob(df, feature_column, feature_value, label_column, label))

    # Retornamos la clase con la mayor probabilidad
    return max(class_probs, key=class_probs.get)


# Muestra 'Play golf' dataset
data = pd.DataFrame({
    'panorama': ['soleado', 'soleado', 'nublado', 'lluvioso', 'lluvioso', 'lluvioso', 'nublado', 'soleado', 'soleado', 'lluvioso', 'soleado', 'nublado', 'nublado', 'lluvioso'],
    'temperatura': ['caliente', 'caliente', 'caliente', 'templada', 'fria', 'Fria', 'fria', 'templada', 'fria', 'templada', 'templada', 'templada', 'caliente', 'templada'],
    'humedad': ['alta', 'alta', 'alta', 'alta', 'normal', 'normal', 'normal', 'alta', 'normal', 'normal', 'normal', 'alta', 'normal', 'alta'],
    'viento': ['no', 'si', 'no', 'no', 'no', 'si', 'si', 'no', 'no', 'no', 'si', 'si', 'no', 'si'],
    'jugar': ['no', 'no', 'si', 'si', 'si', 'no', 'si', 'no', 'si', 'si', 'si', 'si', 'si', 'no']
})

# Extraer caracteristicas y clases esperadas
features = ['panorama', 'temperatura', 'humedad', 'viento']
target_col = 'jugar'

# Test de predicción para un conjunto de características
test = {'panorama': 'soleado', 'temperatura': 'caliente', 'humedad': 'alta', 'viento': 'no'}

# Realizamos la predicción con Naive Bayes
prediction = predict(test, data, target_col)

print("Para los parámetros:", test, "se recomienda", prediction.upper(), "jugar.")