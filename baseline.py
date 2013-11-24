from load_data import *
from pprint import pprint
from utils import *
import pandas as pd
import numpy as np

ratings = load_rating_data()

ratings_train, ratings_test = get_sample_data(ratings, 0.90)

r = get_data_non0(ratings_train)

# print len(ratings_train_non0)
# 43220

mu = np.average(r['Book-Rating'])

ug = r.groupby('User-ID')['Book-Rating']
bg = r.groupby('ISBN')['Book-Rating']

delta = 20

bias_fn = lambda x: (x.mean() - mu) / (delta + x.count())

# bias_u = ug.transform(bias_fn)
bias_u = ug.agg(bias_fn)
bias_b = bg.agg(bias_fn)

# print bias_u
# User-ID
# 8         -1.600856
# 26         1.399144
# 39        -0.050428
# ...
# 278832     2.399144
# 278851    -2.600856
# 278854    -1.600856
# Name: Book-Rating, Length: 18572, dtype: float64

# print bias_b
# User-ID
# 8         -1.600856
# 26         1.399144
# 39        -0.050428
# ...
# 278832     2.399144
# 278851    -2.600856
# 278854    -1.600856
# Name: Book-Rating, Length: 18572, dtype: float64

r['pred-Book-Rating'] = mu + r['User-ID'].map(lambda x: bias_u.get(x, 0)) + r['ISBN'].map(lambda x: bias_b.get(x, 0))

train_rmse = get_rmse_from_data(r)

t = get_data_non0(ratings_test)

t['pred-Book-Rating'] = mu + t['User-ID'].map(lambda x: bias_u.get(x, 0)) + t['ISBN'].map(lambda x: bias_b.get(x, 0))

test_rmse = get_rmse_from_data(t)

print "For delta: "  + str(delta)
print "train: " + str(train_rmse)
print "test: " + str(test_rmse)
# For delta: 0
# train: 1.10600244505
# test: 1.9584315216

# For delta: 10
# train: 1.63972076951
# test: 1.8226827117

# For delta: 20
# train: 1.73279184732
# test: 1.83037260929