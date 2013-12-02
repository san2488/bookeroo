from collections import *
import numpy as np

def get_rmse_from_data(data, actual_col="Book-Rating", predicted_col="pred-Book-Rating"):
    return get_rmse(data[actual_col], data[predicted_col])

def get_rmse(d1, d2):
    return np.sqrt(((d1 - d2)**2).mean())    

def get_distance(v1,v2,mu):
	sum = 0
	flag = False

	for k,v in v1.iteritems():
		if(k in v2):
			sum += ((v - v2[k])**2)
			flag = True
		else:
			sum += ((v - mu)**2)

	for k, v in v2.iteritems():
		if(k not in v1):
			sum += ((v - mu)**2)

	sum = np.sqrt(sum)
	if(sum>0 or flag):
		return sum
	else:
		return 1000


def get_nn(u1,v1,k2,mat,users,knn):
	
	d = {}
	for u in users:
		if(u in mat):
			d[u] = get_distance(v1,mat[u],0)
	

	
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
	 

	

