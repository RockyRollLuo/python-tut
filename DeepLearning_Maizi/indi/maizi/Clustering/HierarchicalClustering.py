# -*- coding:utf-8 -*- 
# Created by Rocky on 2018-01-31
import math


class cluster_node:
    def __init__(self,vec,left=None,right=None,distance=0.0,id=None,count=0):
        self.vec=vec
        self.left=left
        self.right=right
        self.id=id
        self.distance=distance
        self.count=count

def L2dist(v1,v2):
    return math.sqrt(sum(v1-v2)**2)

def L1dist(v1,v2):
    return sum(math.fabs(v1-v2))