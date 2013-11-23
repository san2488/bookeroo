import csv
import pandas as pd
import numpy as np
dir = '/Users/SAN/Documents/Classes/ALDA/Project/BX-CSV-Dump'

def load_data():
    return load_book_data(), load_user_data(), load_rating_data()

def load_book_data():
    book_data = pd.read_csv(dir + '/BX-Books.csv', sep=';', quotechar='"', escapechar='\\', usecols=[0, 3], index_col=False)

    return book_data

def load_user_data():
    user_data = pd.read_csv(dir + '/BX-Users.csv', sep=';', quotechar='"', escapechar='\\', index_col=False, usecols=[0, 2])

    return user_data

def load_rating_data():
    rating_data = pd.read_csv(dir + '/BX-Book-Ratings.csv', sep=';', quotechar='"', escapechar='\\', index_col=False)

    return rating_data

def get_training_test_data(data, train_ratio, seed=1234):
    ''' Randomly samples the data into training and test data. Returns train, test '''
    np.random.seed(seed)
    rows = np.random.choice(data.index, size=len(data.index)*(1 - train_ratio), replace=False)

    return data.drop(rows), data.ix[rows]