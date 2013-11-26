'''
Created on Nov 25, 2013

@author: Jinay
'''
from load_data import *
from pprint import pprint
from utils import *
import pandas as pd
import numpy as np


ratings = load_rating_data()
ratings_train, ratings_test = get_sample_data(ratings, 0.9)
r = get_data_non0(ratings_train)
r.set_index(['User-ID','ISBN'],inplace = True)


ug = r.groupby(level = ['User-ID','ISBN'])['Book-Rating']


mat = {}

#k1[0] --> User-ID, k1[1] --> ISBN, k2[0] --> Book-Rating
for k1,k2 in ug:
	tmp = {}
	if(mat.has_key(k1[0])):
		tmp = mat[k1[0]]
	tmp[k1[1]] = k2[0]
	mat[k1[0]] = tmp
	
	#print k1[0], k1[1], k2[0]



#mat = {1:{'a' : 1, 'd' : 2},2:{'a' : 1, 'b' : 2, 'c' : 3, 'd' : 3, 'e' : 1},3:{'b':2, 'c':3, 'd':4}}

users = {}
for k1,v1 in mat.iteritems():
	tmp = {}
	for k2, v2 in mat.iteritems():
		tmp[k2] = get_distance(v1,v2,0)
	users[k1] = tmp
	print users[k1]	



        
