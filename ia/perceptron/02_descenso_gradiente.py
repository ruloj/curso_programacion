import numpy as np

# Función para predecir con el perceptrón
def predict(inputs, weights):
    # Producto punto entre las entradas y los pesos + el bias (weights[0])
    summation = np.dot(inputs, weights[1:]) + weights[0]
    return 1 if summation > 0 else 0

# Función de entrenamiento utilizando descenso de gradiente
def train_perceptron(training_data, labels, learning_rate=0.01, epochs=100):
    input_size = training_data.shape[1]
    # Inicializamos los pesos aleatoriamente (incluyendo el bias como weights[0])
    weights = np.random.rand(input_size + 1)  # +1 para el término de bias
    for epoch in range(epochs):
        total_error = 0
        for inputs, label in zip(training_data, labels):
            prediction = predict(inputs, weights)
            error = label - prediction
            # Actualizamos los pesos usando el error y el learning_rate
            weights[1:] += learning_rate * error * inputs
            weights[0] += learning_rate * error  # Actualizamos el bias
            total_error += abs(error)  # Acumulamos el error absoluto para analizar el desempeño
        # print(f'Epoch {epoch+1}/{epochs}, Total Error: {total_error}')
        # Si el error total es 0, el perceptrón ya ha convergido
        if total_error == 0:
            break
    return weights





# PARA AND
print("AND")
training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1]) 

weights = train_perceptron(training_data, labels)

# Datos de prueba
test_data = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
for data in test_data:
    prediction = predict(data, weights)
    if prediction == 1:
        print(f"El punto {data} resultado 1")
    else:
        print(f"El punto {data} resultado 0")



# PARA OR
print("OR")
training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 1, 1, 1]) 

weights = train_perceptron(training_data, labels)

# Datos de prueba
test_data = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
for data in test_data:
    prediction = predict(data, weights)
    if prediction == 1:
        print(f"El punto {data} resultado 1")
    else:
        print(f"El punto {data} resultado 0")