from load_data import *
from pprint import pprint
import pandas as pd
import numpy as np

books, users, ratings = load_data()

# pprint(books)
# pprint(users)
# pprint(ratings)

# print books.ix[1:5]
# print users.ix[1:5]
# print ratings.ix[1:5]

ratings_train, ratings_test = get_training_test_data(ratings, 0.90)

# print ratings_train
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 1034803 entries, 0 to 1149779
# Data columns (total 3 columns):
# User-ID        1034803  non-null values
# ISBN           1034803  non-null values
# Book-Rating    1034803  non-null values
# dtypes: int64(2), object(1)

mu = np.average(ratings_train['Book-Rating'])

print mu

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
