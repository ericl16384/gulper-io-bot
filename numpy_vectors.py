import numpy as np

def to_vector(v, dtype=np.float32):
    return np.array(v, dtype=dtype)

def vector_to_int_tuple(vector):
    return tuple(np.array(vector, dtype=int))

def magnitude(vector):
    return np.linalg.norm(vector)

def normalize(vector):
    return vector / magnitude(vector)