import numpy as np
import csv

f = open("/work/home/nhkim/BiS495/data/ADNI_ACCNUM.csv", "r")
reader = csv.reader(f)
profile = list(reader)
prof = np.array(profile)

prof = prof[0,1:]
del_num = 0

for i in range(600, len(prof)):
    if prof[i] == 'v04 037_S_4432':
        del_num = i
        break

print(del_num)