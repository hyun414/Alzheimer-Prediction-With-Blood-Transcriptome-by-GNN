import GEOparse
import pandas as pd
import numpy as np

gse = GEOparse.get_GEO(filepath="/work/home/nhkim/BiS495/data/GSE63060_family.soft.gz")

status_list = []
patient_list = []

for gsm_name, gsm in gse.gsms.items():
    status = gsm.metadata.get('characteristics_ch1')[0][8:]
    if (status == 'CTL'): status_list.append(1)
    elif (status == 'MCI'): status_list.append(2)
    elif (status == 'AD'): status_list.append(3)
    elif (status == 'borderline MCI'): status_list.append(4)
    elif (status == 'OTHER'): status_list.append(5)
    elif (status == 'CTL to AD'): status_list.append(6)
    elif (status == 'MCI to CTL'): status_list.append(7)
    else: status_list.append(8)
    patient_list.append(gsm_name)
    
df = pd.DataFrame(data=status_list, index = patient_list)

print(df)

df.to_csv('/work/home/nhkim/BiS495/data/ANM1_label.csv', index=True)