import numpy as np

def predict(inputs,weights):
    summation = np.dot(inputs, weights[1:]) + weights[0]
    return 1 if summation > 0 else 0

def train_perceptron(training_data, labels, learning_rate=0.01, epochs=100):
    input_size = training_data. shape[1]
    weights = np.random.rand(input_size + 1) # +1 for bias term
    for _ in range(epochs):
        for inputs, label in zip(training_data, labels):
            prediction = predict(inputs, weights)
            error = label - prediction
            weights [1:] += learning_rate * error * inputs
            weights [0] += learning_rate * error
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