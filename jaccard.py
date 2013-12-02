from load_data import *
from pprint import pprint
from utils import *
import numpy as np
import pandas as pd

ratings = load_rating_data()

ratings_train, ratings_test = get_sample_data(ratings, 0.90)

r = get_data_non0(ratings_train)
t = get_data_non0(ratings_test)

ug = r.groupby('User-ID')['ISBN']
tg = t.groupby('User-ID')['ISBN']

for name, group in tg:
    # print type(group)
    for book in group.values:
        cng = ug.filter(lambda x: book in x.values)
        maxjac = -999999999
        neighbor = None
        for cn_u, cn_g in cng:
            jac = jaccard_score(cn.values, group.values)
            if(jac > maxjac):
                neighbor = cn_u
                maxjac = jac
            # maxjac = 
            pass
        print neighbor
        # mask = cng.filter(lambda x: x in group.values)
        # print mask
        # for cn, cg in cng:

        #     pass
        pass
    # books = tgroups[tkey]
    # print books
    # print cn
    # for book in books:
    #     cn = ug.filter(lambda x: )
    # #     # print book
    #     print cn
    #     pass
    pass

def jaccard_score(I, K):
    InK = []
    IuK = []
    for i in I:
        for k in K:
            if i == k:
                InK.append(i)
            else:
                if i not in IuK:
                    IuK.append(i)
                if k not in IuK:
                    IuK.append(k)
            pass
    return len(InK) / len(IuK)