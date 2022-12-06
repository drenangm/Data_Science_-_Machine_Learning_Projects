# Pacotes
import math
import numpy as np
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
# Gera o plot do matplotlib na tela para o VSCode
import matplotlib
matplotlib.use('TKAgg')

# Funcao para normalizar os dados
def normaliza_dados(X, axis = -1, order = 2):
    l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    l2[l2 == 0] = 1
    return X / np.expand_dims(l2, axis)

# Funcao para calcular a distancia euclidiana entre 2 vetores
def calcula_distancia_euclidiana(x1, x2):
    distance = 0
    for i in range(len(x1)):
        distance += pow((x1[i] - x2[i]), 2)
    return math.sqrt(distance)

# Classe para o algoritmo K-means
# Aprendizagem nao-supervisionada
class KMeans():
    
    # Construtor da classe
    def __init__(self, k = 3, max_iterations = 500):
        self.k = k
        self.max_iterations = max_iterations
    
    # Inicializa os centroides com k amostras randomicas de x
    def _init_random_centroids(self, X):
        n_samples, n_features = np.shape(X)
        centroids = np.zeros((self.k, n_features))
        for i in range(self.k):
            centroid = X[np.random.choice(range(n_samples))]
            centroids[i] = centroid
        return centroids
    
    # Retorna o indice mais proximo do centroide da amostra
    def _closest_centroid(self, sample, centroids):
        closest_i = 0
        closest_dist = float('inf')
        for i, centroid in enumerate(centroids):
            distance = calcula_distancia_euclidiana(sample, centroid)
            if distance < closest_dist:
                closest_i = i
                closest_dist = distance
    
        return closest_i

    # Associa as amostras de dados aos centroides mais proximos para criar os clusters (grupos)
    def _create_clusters(self, centroids, X):
        n_samples = np.shape(X)[0]
        clusters = [[] for _ in range(self.k)]
        for sample_i, sample in enumerate(X):
            centroid_i = self._closest_centroid(sample, centroids)
            clusters[centroid_i].append(sample_i)
        
        return clusters
    
    # Calcula novos centroides como a media das amostras em cada cluster
    def _calculate_centroids(self, clusters, X):
        n_features = np.shape(X)[1]
        centroids = np.zeros((self.k, n_features))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(X[cluster], axis = 0)
            centroids[i] = centroid
        
        return centroids
    
    # Classifica as amostras com o indice dos seus clusters
    def _get_cluster_labels(self, clusters, X):
        y_pred = np.zeros(np.shape(X)[0])
        for cluster_i, cluster in enumerate(clusters):
            for sample_i in cluster:
                y_pred[sample_i] = cluster_i
        
        return y_pred

    # Faz a previsao de cada cluster e retorna os indices dos clusters
    def predict(self, X):
        
        # Inicializa centroides como k amostras aleatorias de X
        centroids = self._init_random_centroids(X)
        
        # Iterar ate a convergencia ou para iteracoes maximas
        for _ in range(self.max_iterations):
            
            # Atribuir amostras aos centroides mais proximos (criar clusters)
            clusters = self._create_clusters(centroids, X)
            
            # Salvar os centroides atuais para verificacao de convergencia
            prev_centroids = centroids
            
            # Calcular novos centroides a partir dos clusters
            centroids = self._calculate_centroids(clusters, X)
            
            # Se nenhum centroide mudou => convergencia
            diff = centroids - prev_centroids
            if not diff.any():
                break
                
        return self._get_cluster_labels(clusters, X)

# Calcula a matriz de co-variancia
def calculate_covariance_matrix(X, Y = None):
    if Y is None:
        Y = X
    n_samples = np.shape(X)[0]
    covariance_matrix = (1 / (n_samples - 1)) * (X - X.mean(axis = 0)).T.dot(Y - Y.mean(axis = 0))
    
    return np.array(covariance_matrix, dtype = float)

# Calcula a matriz de correlacao
def calculate_correlation_matrix(X, Y = None):
    if Y is None:
        Y = X
    n_samples = np.shape(X)[0]
    covariance = (1/ n_samples) * (X - X.mean(0)).T.dot(Y - Y.mean(0))
    std_dev_X = np.expand_dims(calculate_std_dev(X), 1)
    std_dev_y = np.expand_dims(calculate_std_dev(Y), 1)
    correlation_matrix = np.divide(covariance, std_dev_X.dot(std_dev_y.T))
    
    return np.array(correlation_matrix, dtype = float)

# Classe para criar o plot
class Plot():
    
    # Contrutor da classe
    def __init__(self):
        self.cmap = plt.get_cmap('viridis')
        
    # Funcao para transformar os dados 
    def _transform(self, X, dim):
        covariance = calculate_covariance_matrix(X)
        eigenvalues, eigenvectors = np.linalg.eig(covariance)
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx][:dim]
        eigenvectors = np.atleast_1d(eigenvectors[:, idx])[:,:dim]
        X_transformed = X.dot(eigenvectors)
        
        return X_transformed
    
    # Plot do dataset X e seus correspondentes labels y em 2D usando PCA
    def plot_in_2d(self, X, y = None, title = None,  accuracy = None, legend_labels = None):
        X_transformed = self._transform(X, dim = 2)
        x1 = X_transformed[:, 0]
        x2 = X_transformed[:, 1]
        class_distr = []
        
        y = np.array(y).astype(int)
        
        colors = [self.cmap(i) for i in np.linspace(0, 1, len(np.unique(y)))]

        # Plot de diferentes distribuicoes de classe
        for i, I in enumerate(np.unique(y)):
            _x1 = x1[y == I]
            _x2 = x2[y == I]
            _y = y[y == I]
            class_distr.append(plt.scatter(_x1, _x2, color = colors[i]))
            
        # Plot da legenda
        if not legend_labels is None:
            plt.legend(class_distr, legend_labels, loc = 1)
            
        # Plot do titulo
        if title:
            if accuracy:
                perc = 100 * accuracy
                plt.suptitle(title)
                plt.title('Acuracia: %.1f%%' % perc, fontsize = 10)
            else:
                plt.title(title)
                
        # Axis labels
        plt.xlabel('Componente Principal 1')
        plt.ylabel('Componente Principal 2')
        
        plt.show()

from sklearn.datasets import make_blobs

# Funcao para execucao principal do programa
def main():
    
    # Carrega o dataset
    X, y = make_blobs()
    
    # Executa o algoritmo para k = 3
    clf = KMeans(k = 3)
    y_pred = clf.predict(X)
    
    # Projeta os dados com 2 componentes principais
    p = Plot()
    p.plot_in_2d(X, y_pred, title = 'Segmentacao de Clientes com K-Means')
    
if __name__ == '__main__':
    main()
        