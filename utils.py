import numpy as np

def get_rmse_from_data(data, actual_col="Book-Rating", predicted_col="pred-Book-Rating"):
    return get_rmse(data[actual_col], data[predicted_col])

def get_rmse(d1, d2):
    return np.sqrt(((d1 - d2)**2).mean())    