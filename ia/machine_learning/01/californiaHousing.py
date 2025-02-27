from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

### FUNCIONES AUXILIARES ###
# Graficar importancia de atributos
def plot_features_importance(features, importances, algorithm):
    from matplotlib import pyplot as plt
    plt.rcParams.update({'figure.figsize': (8.0, 6.0)})
    plt.rcParams.update({'font.size': 12})

    plt.barh(features,importances)
    plt.xlabel("Importancia de atributos en " + algorithm)
    plt.show()

# Graficar árbol de decisión
def plot_decision_tree(dt):
    import matplotlib.pyplot as plt
    from sklearn import tree

    plt.figure(figsize=(30,15))
    plt.rcParams.update({'font.size': 14})

    _ = tree.plot_tree(dt, filled=True)
    plt.show()

# Imprimir diccionario ordenado
def print_sorted_dict(data):
    sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        print(f'{key}: {value}')
    print()




#### ALGORITMOS ####

### LINEAR REGRESSION ###
def linear_regression(df):
    from sklearn.linear_model import LinearRegression
    # Preparar datos
    X = df.data
    y = df.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=0)

    # Obtención del modelo
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Predicción
    y_pred = lr.predict(X_test)

    # Importancia de atributos
    dict_coef =  dict(zip(df.feature_names,lr.coef_.round(3)))
    dict_coef['Intercept'] = lr.intercept_.round(3)
    print("Influencia de los atributos en la variable respuesta.")
    print_sorted_dict(dict_coef)
    plot_features_importance(df.feature_names,lr.coef_.round(3), "Linear Regression")

    # Evaluación
    print("Evaluación: ", mean_squared_error(y_test, y_pred))


### RANDOM FOREST REGRESSION ###
def random_forest_regression(df):
    from sklearn.ensemble import RandomForestRegressor
    # Preparar datos
    X = df.data
    y = df.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=0)

    # Obtención del modelo
    regresion = RandomForestRegressor(n_estimators=1000, criterion='squared_error', random_state=4, n_jobs=-1)
    regresion.fit(X_train, y_train)

    # Predicción
    y_pred = regresion.predict(X_test)

    # Importancia de atributos
    feature_importances =  dict(zip(df.feature_names, regresion.feature_importances_.round(3)))
    print("Influencia de los atributos en la variable respuesta.")
    print_sorted_dict(feature_importances)
    plot_features_importance(df.feature_names, regresion.feature_importances_.round(3), "Random Forest")

    # Evaluación
    print("Evaluación: ", mean_squared_error(y_test, y_pred))


### MULTILAYER PERPCEPTRON REGRESSOR (BLACK BOX) ###
def multilayer_perceptron_regressor(df):
    from sklearn.neural_network import MLPRegressor
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline

    # Preparar datos
    X = df.data
    y = df.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle=True)

    # Obtención del modelo
    mlp = make_pipeline(StandardScaler(), MLPRegressor(max_iter=500, learning_rate_init=0.01))
    mlp.fit(X_train, y_train)

    # Predicción
    y_pred = mlp.predict(X_test)

    # Importancia de los atributos
    print("Influencia de los atributos en la variable respuesta.")
    print("no se puede obtener - black box")

    # Evaluación
    print("Evaluación: ", mean_squared_error(y_test, y_pred))


### DECISION TREE REGRESSOR (WHITE BOX) ###
def decision_tree_regressor(df):
    from sklearn.tree import DecisionTreeRegressor

    # Preparar datos
    X = df.data
    y = df.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle=True)

    # Obtención del modelo
    dt = DecisionTreeRegressor(max_depth=5)
    dt.fit(X_train, y_train)

    # Predicción
    y_pred = dt.predict(X_test)

    # Importancia de los atributos
    feature_importances =  dict(zip(df.feature_names, dt.feature_importances_.round(3)))
    print("Influencia de los atributos en la variable respuesta.")
    print_sorted_dict(feature_importances)
    plot_features_importance(df.feature_names, dt.feature_importances_.round(3), "Decision Tree")

    # Evaluación
    print("Evaluación: ", mean_squared_error(y_test, y_pred))

    # Visualización del árbol
    plot_decision_tree(dt)



### PROBANDO LOS ALGORITMOS ###
# Cargar dataset
housing = fetch_california_housing(as_frame=True)
'''
    Instancias: 20640

    Atributos (8 numericos)
        MedInc	    Ingreso medio de los hogares
        HouseAge	Edad promedio de las casas
        AveRooms  	Número promedio de habitaciones por hogar
        AveBedrms	Número promedio de dormitorios por hogar
        Population	Población total en la zona
        AveOccup	Promedio de ocupantes por hogar
        Latitude	Latitud geográfica
        Longitude	Longitud geográfica

    Target: Precio medio de la vivienda en cientos de miles de dólares.
        Valor continuo: algoritmo de regresión

    Para más información: housing.DESCR
'''

## LINEAR REGRESSION ###
print("LINEAR REGRESSION")
linear_regression(housing)
print("------------------------------------------", end="\n\n")

### RANDOM FOREST REGRESSION ###
print("RANDOM FOREST REGRESSION")
random_forest_regression(housing)
print("------------------------------------------", end="\n\n")

### MULTILAYER PERPCEPTRON REGRESOR (BLACK BOX) ###
print("MULTILAYER PERPCEPTRON REGRESOR (BLACK BOX)")
multilayer_perceptron_regressor(housing)
print("------------------------------------------", end="\n\n")

### DECISION TREE REGRESSOR (WHITE BOX) ###
print("DECISION TREE REGRESSOR (WHITE BOX)")
decision_tree_regressor(housing)
print("------------------------------------------", end="\n\n")