#!/usr/bin/env python3

import numpy as np

array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open("save_multi_array.npz", "wb") as file:
    np.savez(file, a1=array1, a2=array2)

file_npz = np.load("save_multi_array.npz")
print(file_npz.files)

a1 = file_npz['a1']
a2 = file_npz['a2']
# 增加新的 array3
array3 = np.random.rand(30)

with open("save_multi_array_1.npz", "wb") as file:
    np.savez(file, a1=a1, a2=a2, a3=array3)
    
file_npz_1 = np.load("save_multi_array_1.npz")
print(file_npz_1.files)
