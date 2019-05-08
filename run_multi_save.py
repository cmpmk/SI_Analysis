import os
import numpy as np

A = np.arange(1, 21, 1)

for i in A:
    os.system('python3 save_vars.py %s' % i)
    
