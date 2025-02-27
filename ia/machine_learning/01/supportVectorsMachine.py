#Importar librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score
from sklearn.datasets import load_wine



########## PREPARAR LA DATA ##########

#Importamos los datos de la misma librería de scikit-learn
dataset = load_wine()
print(dataset)

########## ENTENDIMIENTO DE LA DATA ##########

#Verifico la información contenida en el dataset
print('Información en el dataset:')
print(dataset.keys())
print()

#Verifico las características del dataset
print('Características del dataset:')
print(dataset.DESCR)

#Seleccionamos todas las columnas
X = dataset.data

#Defino los datos correspondientes a las etiquetas
y = dataset.target

########## IMPLEMENTACIÓN DE NAIVE BAYES ##########

from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



scaler=StandardScaler()
scaler_X_train=scaler.fit_transform(X_train)
print(scaler_X_train)

saler_X_test=scaler.transform(X_test)


#Defino el algoritmo a utilizar
# Support Vector Machine
from sklearn.svm import SVC

svc_clf = SVC(C=1.0, 
              kernel='rbf', 
              degree=3, 
              gamma='auto', 
              coef0=0.0, shrinking=True, 
              probability=False, 
              tol=0.001, cache_size=200, 
              class_weight=None, 
              verbose=False, max_iter=-1, 
              decision_function_shape='ovr', 
              break_ties=False,random_state=None)

#Entreno el modelo
svc_clf.fit(scaler_X_train,y_train)

#Realizo una predicción
svc_clf_predictions=svc_clf.predict(X_test)
print(svc_clf_predictions)

#Evaluación del modelo
c=confusion_matrix(y_test,svc_clf_predictions)
a=accuracy_score(y_test,svc_clf_predictions)
p=precision_score(y_test,svc_clf_predictions)
r=recall_score(y_test,svc_clf_predictions)
