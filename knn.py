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
b = get_data_non0(ratings_train)
r = get_data_non0(ratings_train)
t = get_data_non0(ratings_test)


r.set_index(['User-ID','ISBN'],inplace = True)
t.set_index(['User-ID','ISBN'],inplace = True)
b.set_index(['ISBN','User-ID'],inplace = True)

ug = r.groupby(level = ['User-ID','ISBN'])['Book-Rating']
tg = t.groupby(level = ['User-ID','ISBN'])['Book-Rating']
bg = b.groupby(level = ['ISBN','User-ID'])['Book-Rating']

mat = {}

#k1[0] --> User-ID, k1[1] --> ISBN, k2[0] --> Book-Rating
for k1,k2 in ug:
	tmp = {}
	if(mat.has_key(k1[0])):
		tmp = mat[k1[0]]
	tmp[k1[1]] = k2[0]
	mat[k1[0]] = tmp
	
	#print k1[0], k1[1], k2[0]

mat_test = {}
for k1,k2 in tg:
	tmp = {}
	if(mat_test.has_key(k1[0])):
		tmp = mat_test[k1[0]]
	tmp[k1[1]] = k2[0]
	mat_test[k1[0]] = tmp
	


mat_book = {}
for k1,k2 in bg:
	tmp = {}
	if(mat_book.has_key(k1[0])):
		tmp = mat_book[k1[0]]
	tmp[k1[1]] = k2[0]
	mat_book[k1[0]] = tmp
	k1[0], k1[1], k2[0]

'''
knn = []
rmse = 0
count = 0	
'''


for i in range(1,11):
	#knn = []
	rmse = 0
	count = 0	
	for k1,v1 in mat_test.iteritems():
		for k2,v2 in v1.iteritems():
			if(k2 in mat_book):
				#t = {}
				#t['Book-Rating'] = v2
				#u = get_nn(k1,v1,k2,mat,mat_book[k2].keys())
				#t['pred-Book-Rating'] = get_nn(k1,v1,k2,mat,mat_book[k2].keys(),i)
				#mat[u][k2]	
				#t['rmse'] = (((t['Book-Rating'] - t['pred-Book-Rating'])**2)**0.5)
				#rmse += t['rmse']
				predict_val = get_nn(k1,v1,k2,mat,mat_book[k2].keys(),i)				
				rmse += (((v2 - predict_val)**2)**0.5)
				count += 1
				#knn.append(t)
	rmse = rmse/count
	print "k= ",i," RMSE: ",rmse

#1.46629419068
