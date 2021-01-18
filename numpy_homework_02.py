#!/usr/bin/env python3

import numpy as np

array1 = np.array(range(30))
print(f"Origin Array = {array1}\n")

array_5x6 = array1.reshape(5, 6, order="F")
print(f"New Array 5x6 = {array_5x6}\n")

index = np.where(array_5x6%6 == 1)
print(f"Index: {index}")

