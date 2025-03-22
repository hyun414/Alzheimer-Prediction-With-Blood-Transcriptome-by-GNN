import csv
import numpy as np
import pandas as pd

f = open("/work/home/nhkim/BiS495/used_data/ADNI_Gene_Expression_Profile.csv", "r")
reader = csv.reader(f)
profile = list(reader)
prof = np.array(profile)

RIN = prof[5, 3:-1]
RIN = RIN.astype(float)
del_list = []

for i in range(len(RIN)):
    if RIN[i] < 6.9:
        del_list.append(i)

print(del_list)