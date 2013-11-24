import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
from load_data import *

ratings = load_rating_data()

ratings_rest, ratings_sample =  get_sample_data(ratings, 1)

ratings_non0 = ma.masked_values(ratings_sample['Book-Rating'], 0)

print ratings_non0.mean()
# 7.60106624607
print ratings_non0.count()  
# 433671



# print ratings_sample



# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 229956 entries, 1030937 to 196884
# Data columns (total 3 columns):
# User-ID        229956  non-null values
# ISBN           229956  non-null values
# Book-Rating    229956  non-null values
# dtypes: int64(2), object(1)

hist, bins = np.histogram(ratings_non0, bins=10, range=(1, 10))

width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()
