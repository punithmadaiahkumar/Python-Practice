#Python script to compute percentiles!

import numpy as np

array = np.array([3,4,7,8,6])

percentile = np.percentile(array,45) #checking 45th percentile
print(percentile)