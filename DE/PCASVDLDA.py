import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X=np.array([[1,2,3],[4,5,6],[7,8,9]])
scaler=StandardScaler().fit_transform(X)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(scaler)
print("PCA Result:\n", X_pca)

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'I love machine learning',
    'PCA is a dimensionality reduction technique',
    'Truncated SVD is used for sparse data' 
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
svd = TruncatedSVD(n_components=2)
X_svd = svd.fit_transform(X)
print("Truncated SVD Result:\n", X_svd)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
X=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array([0,1,1])
scaler=StandardScaler().fit_transform(X)
lda=LinearDiscriminantAnalysis(n_components=1)
X_lda=lda.fit_transform(scaler,y)
print("LDA Result:\n", X_lda)