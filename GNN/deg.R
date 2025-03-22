library(limma)
library(readr)

data <- read_csv("/work/home/nhkim/BiS495/data_f/f_data.csv")
label <- read_csv("/work/home/nhkim/BiS495/data_f/f_label.csv")

data <- data[, -1]

exprs_matrix <- as.matrix(data)

group <- factor(label$diagnosis)

design <- model.matrix(~ group)

cat("exprs_matrix dimensions:", dim(exprs_matrix), "\n")
cat("label dimensions:", dim(design), "\n")

exprs_matrix <- t(exprs_matrix)

fit <- lmFit(exprs_matrix, design)

fit2 <- eBayes(fit)

deg_results <- topTable(fit2, adjust.method="fdr", number=Inf, p.value=0.00000001)

head(deg_results)

cat("deg_results dimensions:", dim(deg_results), "\n")

degs <- deg_results[deg_results$adj.P.Val < 0.0001, ]

cat("degs dimensions:", dim(degs), "\n")

print(group)

write.csv(degs, file = "/work/home/nhkim/BiS495/data_f/degs_results5.csv", row.names = TRUE)
