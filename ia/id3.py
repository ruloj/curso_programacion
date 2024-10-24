import pandas as pd # Tablas
import math         # Calculos matematico (logaritmo)

def entropy(data, target_col):
    counts = data[target_col].value_counts()
    entropy = 0
    total_samples = len (data)

    for label in counts.index:
        prob = counts[label] / total_samples
        entropy -= prob * math.log2(prob)

    return entropy

def information_gain(data, feature_col, target_col):
    total_entropy = entropy(data, target_col)
    feature_values = data[feature_col].unique()
    weighted_entropy = 0

    for value in feature_values:
        subset = data[data[feature_col] == value]
        subset_entropy = entropy(subset, target_col)
        weight = len(subset) / len(data)
        weighted_entropy += weight + subset_entropy

    return total_entropy - weighted_entropy

def get_best_feature(data, features, target_col):
    information_gains = {feature: information_gain(data,feature,target_col) for feature in features}
    return max(information_gains, key=information_gains.get)

def id3(data, original_data, features, target_col):
    # si todos los target_values son los mismos regresa ese valor
    if len(data[target_col].unique()) == 1:
        return data[target_col].iloc[0]

    # si no hay más caracteristicas para dividir los datos, retorna la clase más frecuente
    if len(features) == 0:
        return original_data[target_col].mode().iloc[0]

    # construccion del arbol
    best_feature = get_best_feature(data, features, target_col)
    tree = {best_feature: {}}

    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        remaining_features = [f for f in features if f != best_feature]
        subtree = id3(subset, original_data, remaining_features,target_col)
        tree[best_feature][value]= subtree

    return tree

def predict(example, tree):
    feature = list(tree.keys())[0]
    value = example[feature]
    subtree = tree[feature][value]

    if isinstance(subtree, dict):
        return predict(example, subtree)
    else:
        return subtree


# Muestra 'Play golf' dataset
data = pd.DataFrame({
    'panorama': ['soleado','soleado','nublado','lluvioso','lluvioso','lluvioso','nublado','soleado','soleado','lluvioso','soleado','nublado','nublado','lluvioso'],
    'temperatura': ['caliente','caliente','caliente','templada','fria','Fria','fria','templada','fria','templada','templada','templada','caliente','templada'],
    'humedad': ['alta','alta','alta','alta','normal','normal','normal','alta','normal','normal','normal','alta','normal','alta'],
    'viento': ['no','si','no','no','no','si','si','no','no','no','si','si','no','si'],
    'jugar': ['no','no','si','si','si','no','si','no','si','si','si','si','si','no']
})

# Extraer caracteristicas y clases esperadas
features = ['panorama','temperatura','humedad','viento']
target_col = 'jugar'

# Generacion del arbol de decision ID3
tree = id3(data,data,features, target_col)

# Test
test = {'panorama': 'soleado','temperatura': 'caliente','humedad': 'alta','viento': 'no'}
print("Para los parametros: ", test, "se recomienda ", predict(test,tree).upper(), "jugar.")