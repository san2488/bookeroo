import csv
import pandas as pd
import numpy as np
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bookeroo.cfg')

dir = config.get('bookeroo', 'bx-data-path')

def get_k_folds(k=3):
    ratings = load_rating_data()
    fold_size = len(ratings) / k
    folds = []
    for i in range(k):
        folds.append(ratings[i * fold_size:i * fold_size + fold_size])
        pass
    return folds

def get_k_fold_data(i, k=3):
    folds = get_k_folds(k)
    test = folds[i]
    del folds[i]
    return pd.concat(folds), test

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

def get_sample_data(data, sample_ratio, seed=1234):
    ''' Randomly samples the data into remaining and sample data. Returns train, test '''
    np.random.seed(seed)
    rows = np.random.choice(data.index, size=len(data.index)*(sample_ratio), replace=False)

    return data.drop(rows), data.ix[rows]

def get_data_non0(data, field='Book-Rating'):
    return data[data[field] != 0]

