from load_data import *
from pprint import pprint
import pandas as pd
import numpy as np
import numpy.ma as ma

books, users, ratings = load_data()

# pprint(books)
# pprint(users)
# pprint(ratings)

# print books.ix[1:5]
# print users.ix[1:5]
# print ratings.ix[1:5]

ratings_train, ratings_test = get_sample_data(ratings, 0.90)

# print ratings_train
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 1034803 entries, 0 to 1149779
# Data columns (total 3 columns):
# User-ID        1034803  non-null values
# ISBN           1034803  non-null values
# Book-Rating    1034803  non-null values
# dtypes: int64(2), object(1)

ratings_train_non0 = ma.masked_equal(ratings_train['Book-Rating'], 0)

mu = ratings_train_non0.mean()
count = ratings_train_non0.count()

print "Mean: "  + str(mu) + ", Count: " + str(count)

# Mean: 7.60085608515, Count: 43220


# rat_mat = pd.DataFrame(columns=books['ISBN'], index=users['User-ID'])

# for user in users:

# print book_data

# pd.merge(book_data, ratings_data, left_index=True, right_index=True)
# user_ratings = pd.merge(left=user_data, right=ratings_data, )

# for r in review_train:
#     userid = r['user_id']
#     businessid = r['business_id']
#     stars = r['stars']
#     ratings = user_business_ratings.setdefault(userid, {})
#     ratings.update({businessid: stars})
#     user_business_ratings.update({userid: ratings})

# pprint(user_business_ratings)
