import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
from load_data import *
from collections import Counter

ratings = load_rating_data()

ratings_rest, ratings_sample =  get_sample_data(ratings, 0.1)

ratings_non0 = get_data_non0(ratings_sample)

# print ratings_non0.mean()
# 7.60106624607
# print ratings_non0.count()  
# 433671



# print ratings_sample



# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 229956 entries, 1030937 to 196884
# Data columns (total 3 columns):
# User-ID        229956  non-null values
# ISBN           229956  non-null values
# Book-Rating    229956  non-null values
# dtypes: int64(2), object(1)

hist, bins = np.histogram(ratings_non0['Book-Rating'], bins=10, range=(1, 10))
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.ylabel('Instances')
plt.xlabel('Possible Ratings')
plt.title('Ratings Distribution')
plt.bar(center, hist, align='center', width=width, color='c', linewidth=0)
plt.show()

# count = Counter(ratings_non0['ISBN'])
# counts = count.values()
# bin_counts = np.bincount(counts)
# hist, bins = np.histogram(counts, bins=90, range=(1, 90))
# width = 0.7 * (bins[1] - bins[0])
# center = (bins[:-1] + bins[1:]) / 2
# cs = ['r'] * len(center)
# index = 0
# for c in center:
#     if c > 3:
#         cs[index] = 'c'
#     index+=1
#     pass
# plt.bar(center, hist, align='center', width=width, log=True, color=cs, linewidth=0)
# # plt.plot(center, hist)
# # plt.yscale('log')
# ymin, ymax = plt.ylim()   # return the current ylim
# plt.ylim( (10**-0.1, ymax) )  # set the ylim to ymin, ymax
# plt.ylabel('Number of books with X number of ratings')
# plt.xlabel('Number of ratings')
# plt.title('Visualizing Sparsity')
# plt.show()

# count = Counter(ratings_non0['User-ID'])
# counts = count.values()
# bin_counts = np.bincount(counts)
# hist, bins = np.histogram(counts, bins=90, range=(1, 90))
# width = 0.7 * (bins[1] - bins[0])
# center = (bins[:-1] + bins[1:]) / 2
# cs = ['r'] * len(center)
# index = 0
# for c in center:
#     if c > 3:
#         cs[index] = 'c'
#     index+=1
#     pass
# plt.bar(center, hist, align='center', width=width, log=True, color=cs, linewidth=0)
# # plt.plot(center, hist)
# # plt.yscale('log')
# ymin, ymax = plt.ylim()   # return the current ylim
# plt.ylim( (10**-0.1, ymax) )  # set the ylim to ymin, ymax
# plt.ylabel('Number of users giving X ratings')
# plt.xlabel('Number of ratings')
# plt.title('Visualizing Sparsity')
# plt.show()

# x = y = range(len(bin_counts))
# y = np.array(y)
# y.fill(1)
# sizes = np.array((bin_counts))
# plt.scatter(x, y, s=sizes, marker='o', c=sizes, alpha=0.5)