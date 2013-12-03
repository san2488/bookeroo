import csv
import pandas as pd
import numpy as np
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bookeroo.cfg')

dir = config.get('bookeroo', 'bx-data-path')

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

def get_userdata_non0(data, field='Age'):
    tmp = data[~data[field].isnull()]
    tmp = tmp[tmp[field] < 120]
    return tmp[tmp[field] != 0]


