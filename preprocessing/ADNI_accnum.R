# 필요한 패키지 로드
library(AnnotationDbi)
library(hgu219.db)
library(readr)

# CSV 파일 읽기
file_path <- "/work/home/nhkim/BiS495/used_data/ADNI_Gene_Expression_Profile.csv"
data <- read_csv(file_path, skip = 8)

# ProbeSet ID 가져오기
probe_ids <- data$ProbeSet
print(probe_ids[1:5])

# hgu219ACCNUM 객체에서 ProbeSet ID를 ACCNUM으로 변환
mapped_probes <- mappedkeys(hgu219ENTREZID)
entrezid_list <- as.list(hgu219ENTREZID[mapped_probes])

entrezid_mapping <- select(hgu219.db, keys=probe_ids, columns="ENTREZID", keytype="PROBEID")

# 데이터에 ACCNUM 추가
entrezid_df <- data.frame(PROBEID = entrezid_mapping$PROBEID, ENTREZID = entrezid_mapping$ENTREZID)

# ProbeSet 열을 ACCNUM으로 대체
data$ProbeSet <- entrezid_df$ENTREZID[match(probe_ids, entrezid_df$PROBEID)]

# 결과 확인
head(data)

# 변환된 데이터 저장
output_path <- "/work/home/nhkim/BiS495/data/ADNI_Gene_Expression_Profile_ENTREZID.csv"
write_csv(data, output_path)
