#PIID(1), VISCODE(3), DIAGNOSIS(6)

import csv
import numpy as np
import pandas as pd

f = open("/work/home/nhkim/BiS495/data/DXSUM_PDXCONV_30Jun2024.csv", "r")
reader = csv.reader(f)

profile = list(reader)

prof = np.array(profile)

prof = prof[3869:10015,:7]
print(prof)
data_dropped = np.delete(prof, [0,2,4,5], axis=1)

f.close()

df = pd.DataFrame(data = data_dropped)
df.to_csv('/work/home/nhkim/BiS495/data/ADNI_simple.csv', index=True)