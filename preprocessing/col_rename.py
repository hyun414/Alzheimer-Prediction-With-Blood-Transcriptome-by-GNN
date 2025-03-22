import pandas as pd
import numpy as np
import csv

filtered_anm1 = pd.read_csv('/work/home/nhkim/BiS495/data_f/filtered_anm1.csv', index_col=0)
filtered_anm2 = pd.read_csv('/work/home/nhkim/BiS495/data_f/filtered_anm2.csv', index_col=0)

new_columns_anm1 = [col[:10] for col in filtered_anm1.columns]
new_columns_anm2 = [col[:10] for col in filtered_anm2.columns]

# 새로운 컬럼 이름 설정
filtered_anm1.columns = new_columns_anm1
filtered_anm2.columns = new_columns_anm2

# 새로운 CSV 파일로 저장
filtered_anm1.to_csv('/work/home/nhkim/BiS495/data_f/filtered_anm1_m.csv')
filtered_anm2.to_csv('/work/home/nhkim/BiS495/data_f/filtered_anm2_m.csv')

print("Patient IDs have been truncated and saved to new CSV files.")