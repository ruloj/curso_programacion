import pandas as pd
# Ajusta el directorio de trabajo
pacientes = pd.read_csv('D:/Dropbox/Anahuac/ML/Pacientes2.csv', engine = 'python', index_col=0)

pacientes.head()

# Variables predictoras
X = pacientes.iloc[:,1:11]

# Variable a predecir
Y = pacientes.iloc[:,0]

# Mostramos las primeras 5 filas
X.head()

from sklearn.model_selection import train_test_split

# X_train y Y_train para entrenamiento
# X_test y Y_test para prueba
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size = 0.75, random_state=0)


X_train.info()


# Creamos el modelo de árbol de decisión
from sklearn.tree import DecisionTreeClassifier

# Llamamos al algoritmo
arbol = DecisionTreeClassifier(max_depth=4)

# Entrenamos el modelo
arbol_enfermedad = arbol.fit(X_train, Y_train)


from matplotlib import pyplot as plt
from sklearn import tree

# Dimensiones del gráfico
fig = plt.figure(figsize=(25,20))

tree.plot_tree(arbol_enfermedad, feature_names=list(X.columns.values),class_names=list(Y.values), filled=True)

plt.show()

# Predecir la respyesta para el conjunto de evaluación
Y_pred = arbol_enfermedad.predict(X_test)

print("Y_pred: ", Y_pred)

from sklearn.metrics import confusion_matrix

Matriz_de_confusion = confusion_matrix(Y_test, Y_pred)

print("Matriz_de_confusion: ", Matriz_de_confusion)

# Calcula la precisión global del modelo
import numpy as np

precisión_global = np.sum(Matriz_de_confusion.diagonal())/np.sum(Matriz_de_confusion)

print("precisión_global: ", precisión_global)

precision_no = ((Matriz_de_confusion[0,0]))/sum(Matriz_de_confusion[0,])
print("precision_no: ", precision_no)

precision_si = ((Matriz_de_confusion[1,1]))/sum(Matriz_de_confusion[1,])
print("precision_si: ", precision_si)

