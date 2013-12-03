from collections import *
import numpy as np
import pandas as pd
from load_data import *

def get_rmse_from_data(data, actual_col="Book-Rating", predicted_col="pred-Book-Rating"):
    return get_rmse(data[actual_col], data[predicted_col])

def get_rmse(d1, d2):
    return np.sqrt(((d1 - d2)**2).mean())    

def get_distance(v1,v2,exst_book,mu):
	sm = 0
	flag = False

	for k,v in v1.iteritems():
		#print k, exst_book
		if(k in v2):
			sm += ((v - v2[k])**2)
			flag = True
		else:
			sm += ((v - mu)**2)

	for k, v in v2.iteritems():
		if(k not in v1):
			sm += ((v - mu)**2)

	sm = np.sqrt(sm)
	if(sm>0 or flag):
		return sm
	else:
		return 1000


def get_jaccard_distance(v1,v2):
	num = 0
	den = 1
	

	for k,v in v1.iteritems():
		#print k, exst_book
		if(k in v2):
			num += 1		
		den += 1

	for k, v in v2.iteritems():
		if(k not in v1):
			den +=1

	return num/den

def baseline_dist(v1,v2,mu,delta):

	bias_u = 0
	bias_b = 0

	for v in v1:
		bias_u += (v - mu)

	bias_u /= float(delta + len(v1))
	
	for v in v2:
		bias_b += (v - mu)
	
	bias_b /= float(delta + len(v2))
	m = mu + bias_u + bias_b
	#print v1, len(v1), v2, len(v2), m
	return m

def age_weighted_distance(u1,v1,k2,mat,users,knn,us):
	
	d = {}
	for u in users:
		if(u in mat):
			d[u] = get_distance(v1,mat[u],k2,0)
	

	
	ord_dict = OrderedDict(sorted(d.items(), key=lambda t: t[1]))		
	
	
	#Age Adjustment
	uage = 0
	sage = 120

	if(u1 in us.keys()):
		uage = us[u1][0]

	
	ages = []
	nausers = []
	adjustes_sums = {}
	flag = False
	
	if(uage == 0):
		flag = True			
		
	
	
	for k in ord_dict.iterkeys():
		if(k in us.keys()):
			ages.append(us[k][0])
			#adjustes_sums[k] = (sage - abs(us[k][0] - uage))
		else:
			flag = True
			nausers.append(k)
			
	
	
	
	if(flag):
		foo = np.array(ages,dtype='f')
		if(all(foo == 0)):
			for k in nausers:
				adjustes_sums[k] = 120
				if(uage == 0):
					uage =  120
		else:
			m = np.median(foo[foo > 0])
			if(uage == 0):
				uage = m
			for k in nausers:
				adjustes_sums[k] = (sage - abs(m - uage))	
		

	for k in ord_dict.iterkeys():
		if(k in us.keys()):
			adjustes_sums[k] = (sage - abs(us[k][0] - uage))



	tsum = np.sum(np.array(adjustes_sums.values()))
	
	
	count = 0;
	rating = 0

	for k in ord_dict.iterkeys():
		count+=1
		if(count <= knn):
			#print count, knn, mat[k][k2] 
			#print "Adjust Ratings",adjustes_sums[k]
			#print adjustes_sums[k] * mat[k][k2]		
			rating = rating + adjustes_sums[k] * mat[k][k2]


	rating = rating/tsum
	#print "Adjust: ", adjustes_sums, "tsum", tsum, "U1", uage, "rating: ", rating
	return rating
	

def get_nn(u1,v1,k2,mat,users,knn,us):
	
	d = {}
	for u in users:
		if(u in mat):
			d[u] = get_distance(v1,mat[u],k2,0)
	

	
	ord_dict = OrderedDict(sorted(d.items(), key=lambda t: t[1]))		
	
	count = 0;
	tsum = 0
	avgc = 0

	for k in ord_dict.iterkeys():
		count+=1
		if(count <= knn):
			#print count, knn, mat[k][k2] 
			avgc += 1
			tsum += mat[k][k2]

	
	tsum = tsum/avgc
	return tsum
	 
def jaccard_weighted_distance(u1,v1,k2,mat,users,knn,us):
	
	d = {}
	for u in users:
		if(u in mat):
			d[u] = get_distance(v1,mat[u],k2,0)
			adjustes_sums[k] = get_jaccard_distance(v1,mat[u])

	
	ord_dict = OrderedDict(sorted(d.items(), key=lambda t: t[1]))		
	
	tsum = np.sum(np.array(adjustes_sums.values()))
	
	
	count = 0;
	rating = 0

	for k in ord_dict.iterkeys():
		count+=1
		if(count <= knn):		
			rating = rating + adjustes_sums[k] * mat[k][k2]


	rating = rating/tsum
	#print "Adjust: ", adjustes_sums, "tsum", tsum, "U1", uage, "rating: ", rating
	return rating
	
	

