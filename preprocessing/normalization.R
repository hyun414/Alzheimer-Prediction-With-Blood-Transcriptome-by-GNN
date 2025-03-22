library(sva)
library(data.table)

# 데이터 파일 경로
file_path_anm1 <- "/work/home/nhkim/BiS495/data_f/filtered_anm1.csv"
file_path_anm2 <- "/work/home/nhkim/BiS495/data_f/filtered_anm2.csv"
file_path_adni <- "/work/home/nhkim/BiS495/data_f/filtered_adni.csv"

# 데이터 불러오기
data_adni <- fread(file_path_adni)
data_anm1 <- fread(file_path_anm1)
data_anm2 <- fread(file_path_anm2)

data_adni_t <- t(data_adni)
data_anm1_t <- t(data_anm1)
data_anm2_t <- t(data_anm2)

data_adni_t <- as.data.frame(data_adni_t[-1,])
data_adni_t$batch <- "adni"
data_anm1_t <- as.data.frame(data_anm1_t[-1,])
data_anm1_t$batch <- "anm1"
data_anm2_t <- as.data.frame(data_anm2_t[-1,])
data_anm2_t$batch <- "anm2"

# 모든 데이터 결합
combined_data <- rbind(data_adni_t, data_anm1_t, data_anm2_t)
print(combined_data[1:10, 1:5])
print(combined_data$batch)

# ComBat 적용
dat <- as.matrix(combined_data[, -ncol(combined_data)])  # 배치 정보 열 제외
print(dat[1,1:5])
print(dim(dat))
dat <- t(dat)

batch <- combined_data$batch
print(str(batch))
combat_data <- ComBat(dat, batch, mod=NULL, par.prior=TRUE, prior.plots=FALSE)

# 보정된 데이터를 데이터프레임으로 변환
combat_data_df <- as.data.frame(combat_data)

# 파일 저장: 파일명 뒤에 '_cb' 추가
write.csv(combat_data_df, file="/work/home/nhkim/BiS495/data_f/filtered_cb_2.csv", row.names=FALSE)

# 저장 확인 메시지
cat("Combat이 적용된 데이터를 filtered_adni_cb.csv, filtered_anm1_cb.csv, filtered_anm2_cb.csv로 저장했습니다.\n")
