import csv
import numpy as np
import pandas as pd

f = open("/work/home/nhkim/BiS495/data/ADNI_Gene_Expression_Profile_ACCNUM.csv", "r")
reader = csv.reader(f)

data = list(reader)

data = np.array(data)
column = data[1:,0]

data = np.delete(data, [0], axis = 0)
data_dropped = np.delete(data, [0, 1, 2, -1], axis=1)

f.close()

f = open("/work/home/nhkim/BiS495/data/ADNI_Gene_Expression_Profile.csv", "r")
reader = csv.reader(f)

profile = list(reader)

prof = np.array(profile)
prof_id = prof[1,3:]
prof_visit = prof[2,3:]

new_index = [f"{id_} {visit}" for id_, visit in zip(prof_id, prof_visit)]

df = pd.DataFrame(data = data_dropped, index = column, columns = new_index)
df.to_csv('/work/home/nhkim/BiS495/data/ADNI_ACCNUM.csv', index=True)