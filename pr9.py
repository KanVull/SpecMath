import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = [
    'sepal-length', 
    'sepal-width', 
    'petal-length', 
    'petal-width', 
    'Class',
]
dataset = pd.read_csv(url, names=names)
sns.pairplot(dataset)
plt.show()
groups = {}
for array in dataset.values:
    if array[4] not in groups.keys():
        groups[array[4]]=[array[:4]]
    else:
        groups[array[4]].append(array[:4])      
for key in groups:
    groups[key] = np.array(groups[key])

labels = list(groups.keys())
colors = [
    'red',
    'green',
    'blue',
]
x = dataset.iloc[:, [0, 1, 2, 3]].values
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)
for i in range(3):
    plt.scatter(x[y_kmeans == i, 0], x[y_kmeans == i, 1], s = 100, c = colors[i], label = labels[i])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1],s = 100, c = 'black', label = 'Centroids')
plt.legend()
plt.show()
