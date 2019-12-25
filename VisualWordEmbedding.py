import numpy as np
import matplotlib.pyplot as plt
import pickle
with open('./word_embedding.tx','wb') as f:
    word_embedding = pickle.load(f)
from sklearn import manifold,datasets
tsne = manifold.TSNE(n_components=2)
tsne.fit_transform(word_embedding)
print(tsne.embedding_)

