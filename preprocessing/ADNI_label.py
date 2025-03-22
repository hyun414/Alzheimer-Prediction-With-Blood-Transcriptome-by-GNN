import csv
import numpy as np
import pandas as pd

f = open("/work/home/nhkim/BiS495/data/ADNI_Gene_Expression_Profile.csv", "r")
reader = csv.reader(f)
profile = list(reader)
prof = np.array(profile)

prof_visit = prof[1,3:-1]
prof_id = prof[2,3:-1]

f.close()

# 2 2 3 2 1 2 1 3 3 2-3
# 073_S_2182 m03
# 072_S_4102 v04
# 006_S_4192 v04
# 013_S_4268 v04
# 072_S_4103 v04
# 009_S_4564 v02
# 022_S_4266 v04
# 114_S_4379 v04
# 094_S_4282 v04
# 037_S_4432 v04
# 해당 결과가 없는 경우 앞 뒤 진단의 결과를 보고 판단 마지막 데이터의 경우 이전에는 2 이후에는 3이 되어 제거


csv_file = open('/work/home/nhkim/BiS495/data/ADNI_simple.csv')

reader = csv.reader(csv_file)

diag = list(reader)

diag = np.array(diag)
diag = diag[1:,1:]

diag_list = []
cnt = 0
di_list = [2, 2, 3, 2, 1, 2, 1, 3, 3]
index_l = []

for id, visit in zip(prof_id, prof_visit):
    t = 0
    iv = visit + ' ' + id
    index_l.append(iv)
    for d in diag:
        if((d[0] == id) and (d[1] == visit)):
            t = 1
            diag_list.append(d[2])
            break
    if (t == 0):
        if (cnt == 9):
            print(index_l[-1])
            del index_l[-1]
        else:
            diag_list.append(di_list[cnt])
            cnt += 1

df = pd.DataFrame(data = diag_list, index = index_l)
df.to_csv('/work/home/nhkim/BiS495/data/ADNI_label.csv', index=True)