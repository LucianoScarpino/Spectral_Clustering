import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import cm
from Laplacian import Laplacian
from EigenMethods import EigenMethods

class SpectralClustering(object):
    """This class perfoms clustering and scatterplot them
        Input arguments:
        - eigenvalues: eigenvalues of Laplacian metrix computed before
        - eigenvectors: eigenvectors of Laplacian metrix computed before
        - M: number of clusters decided
        - dataset: dataset used
     """
    def __init__(self, n_nearest, dataset_name, similarity : str = "exp", sparse : bool= True):
        self.laplacian = Laplacian(similarity, sigma = 1)
        self.dataset_name = dataset_name
        self.eigen = EigenMethods(eigenval_method = "shifting", eigenvec_method = "shifting")
        self.n_nearest = n_nearest
        self.sparse = sparse
    
    def fit_predict(self, X, player_mode = False):
        try:
            X = X.values
        except:
            X = X
        L,W,D = self.laplacian.LWD(X, self.n_nearest, sparse_cond = self.sparse)
        M = self.select_M()
        eigenval, eigenvec = self.eigen.eigencompute(L,5)
        U = self.rotation_matrix(eigenval, eigenvec, M)
        if player_mode:
            return U, self.KMeans(U, M), eigenval
        return self.KMeans(U, M)
    
    def norm_fit_predict(self, X, player_mode = False):
        try:
            X = X.values
        except:
            X = X
        L_norm,W,D = self.laplacian.norm_LWD(X, self.n_nearest, sparse_cond = self.sparse)
        M = self.select_M()
        eigenval, eigenvec = self.eigen.eigencompute(L_norm,5)
        U = self.rotation_matrix(eigenval, eigenvec, M)
        if player_mode:
            return U, self.KMeans(U, M), eigenval
        return self.KMeans(U, M)

    def select_M(self):
        if self.dataset_name == "Circle.csv":
            match self.n_nearest:
                case 10:
                    return 3
                case 20:
                    return 3
                case 40:
                    return 2
        elif self.dataset_name == "Spiral.csv":
            return 3
        elif self.dataset_name == "3D_Dataset.csv":
            return 4
        raise RuntimeError("Algorithm cannot manage this case")
    
    def rotation_matrix(self, eigenvalues, eigenvectors, M):
        """Compute rotation matrix U appending eigenvectors of Laplacian matrix as columns
        """
        sorted_eigenvectors_idx= np.argsort(eigenvalues)[:M]
        return eigenvectors[:,sorted_eigenvectors_idx]

    def KMeans(self, U : np.ndarray, M):
        kmeans = KMeans(n_clusters = M)
        return kmeans.fit_predict(U)
