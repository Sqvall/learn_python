import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
u1 = [0, 1, 1, 0]
u2 = [0, 0, 1, 1]
vbl = [0, 0, 2, 0]
vb = np.array(vbl)

print(round(cosine_similarity(np.array([vb, np.array(u1)]))[0][1]*100, 2))
print(round(cosine_similarity(np.array([vb, np.array(u2)]))[0][1]*100, 2))

print(cosine_similarity(np.array([vb, np.array(u2)])))
