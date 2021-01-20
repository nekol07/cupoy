#!/usr/bin/env python3

import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

m = english_score > math_score
n = np.logical_and(chinese_score > english_score, chinese_score > math_score) 

print(f"英文成績比數學高的有 {np.sum(m == True)} 位")
print(f"全班同學最高分都是國文: {n}")
