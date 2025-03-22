import GEOparse
import pandas as pd
import numpy as np

gse = GEOparse.get_GEO(filepath="/work/home/nhkim/BiS495/used_data/GSE63061_family.soft.gz")
# for gpl_name, gpl in gse.gpls.items():
#     print("Name: ", gpl_name)
#     print("Metadata:",)
#     for key, value in gpl.metadata.items():
#         print(" - %s : %s" % (key, ", ".join(value)))
#     print("Table data:",)
#     print(gpl.table.head())
#     break

# cnt = 0
# for gsm_name, gsm in gse.gsms.items():
#     print("Name: ", gsm_name)
#     print("Metadata:",)
#     for key, value in gsm.metadata.items():
#         print(" - %s : %s" % (key, ", ".join(value)))
#     print ("Table data:",)
#     print (gsm.table)
#     break
#     if (cnt == 2):
#         break
#     cnt += 1

#gpl table의 ID와 gsm table의 ID_REF가 일치될 때의 Accesion값 연결
#환자번호_환자status로 연결

patient = ''
index_name = []
accnum = []
row = 0
t = 0

for gpl_name, gpl in gse.gpls.items():
    gpl_table_dict = {}
    for index, gpl_entry in gpl.table.iterrows():
        gpl_table_dict[gpl_entry['ID']] = gpl_entry['Entrez_Gene_ID']
    break

cnt = 0
for gsm_name, gsm in gse.gsms.items():
    status = gsm.metadata.get('characteristics_ch1')[0][8:]
    if (row == 0):
        val_data = np.empty((0, 1))
        value_array = gsm.table['VALUE'].values.reshape(-1, 1)
        val_data = np.append(val_data, value_array, axis=0)
        row = 1
    else:
        value_array = gsm.table['VALUE'].values.reshape(-1, 1)
        val_data = np.append(val_data, value_array, axis=1)
    # patient 변수 생성
    patient = gsm_name + '_' + status
    index_name.append(patient)
    if (t == 0):
        for gpl_name, gpl in gse.gpls.items():
            t = 1
            for gsm_entry in gsm.table.iterrows():
                if gsm_entry[1]['ID_REF'] in gpl_table_dict:
                    accnum.append(gpl_table_dict[gsm_entry[1]['ID_REF']])
                else:
                    cnt += 1
                    accnum.append('NA')
            break

df = pd.DataFrame(data=val_data, index=accnum, columns=index_name)

print(df)
print(cnt)

df.to_csv('/work/home/nhkim/BiS495/data/ANM1_ei.csv', index=True)