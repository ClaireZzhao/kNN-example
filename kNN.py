# -*- coding: utf-8 -*-


import random 
from math import sqrt



random.seed(10)
target_data = []
for i in range(100):
    target_data.append([random.random(), random.random()])                   

base_data = [random.random(), random.random()]


print(target_data) # [[0.5714025946899135, 0.4288890546751146],...]
print(base_data) # [0.32766572871399635, 0.3220972200771334]


class kNN:
    def __init__(self, base_data, target_data, k):
        self.x = base_data[0]
        self.y = base_data[1]
        self.target_data = target_data
        self.k = k
        self.top()
        
    def distance(self):
        self.result = []
        for data in self.target_data:
            distance = sqrt((self.x - data[0])**2 + (self.y- data[1])**2)
            self.result.append([data[0], data[1], distance])
            
    def top(self):
        self.distance()
        sorted_result = sorted(self.result, key = lambda s: s[2])
        k_sorted_result = sorted_result[:self.k]
        self.distances = []
        self.real_datas = []
        for r in k_sorted_result:
            self.distances.append(round(r[2], 5))
            self.real_datas.append([round(r[0], 5), round(r[1], 5)])
        return self.distances, self.real_datas
    

k1 = kNN(base_data, target_data, 1)  
k1.distances
k1.real_datas
print('k1 -> ', k1.distances)
print('real data :', k1.real_datas[0])

k3 = kNN(base_data, target_data, 3)    
k3.distances
k3.real_datas[0][0]
print('k3 -> ', k3.distances)
print('real data : ', k3.real_datas[0],k3.real_datas[1],k3.real_datas[2])

k5 = kNN(base_data, target_data, 5)    
k5.distances
k5.real_datas
print('k5 -> ', k5.distances)
print('real data : ', k5.real_datas[0], k5.real_datas[1], k5.real_datas[2], k5.real_datas[3], k5.real_datas[4])



