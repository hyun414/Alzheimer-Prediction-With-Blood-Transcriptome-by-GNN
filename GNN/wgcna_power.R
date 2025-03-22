# Load necessary libraries
library(WGCNA)

# Define parameters and folders
data_folder = "/work/home/nhkim/BiS495/GNN/input_features_labels"
output_folder = "/work/home/nhkim/BiS495/GNN/input_adjacency_matrix"
data_file = paste(data_folder, "split10_train_features.csv", sep='/')
dir.create(paste(output_folder), showWarnings = FALSE)

# Load data
data = read.csv(data_file, header = FALSE) # each row is a patient
geneExp = as.matrix(data[2:dim(data)[1], 2:dim(data)[2]])
geneExp[is.na(geneExp)] <- 0 # Replace NA values with zero

# Range of powers to test
powers = c(1:10) # Modify this range as needed
sft = pickSoftThreshold(geneExp, powerVector = powers, verbose = 5)

# Plot scale-free topology fit index as a function of the soft-thresholding power
pdf(file = paste(output_folder, "scale_free_fit.pdf", sep = "/"))
plot(sft$fitIndices[, 1], -sign(sft$fitIndices[, 3]) * sft$fitIndices[, 2],
     xlab = "Soft Threshold (power)", ylab = "Scale Free Topology Model Fit, signed R^2",
     type = "n", main = "Scale independence")
text(sft$fitIndices[, 1], -sign(sft$fitIndices[, 3]) * sft$fitIndices[, 2],
     labels = powers, col = "red")
abline(h = 0.8, col = "red") # Threshold for scale-free topology
dev.off()

# Plot mean connectivity as a function of the soft-thresholding power
pdf(file = paste(output_folder, "mean_connectivity5.pdf", sep = "/"))
plot(sft$fitIndices[, 1], sft$fitIndices[, 5],
     xlab = "Soft Threshold (power)", ylab = "Mean Connectivity",
     type = "n", main = "Mean connectivity")
text(sft$fitIndices[, 1], sft$fitIndices[, 5], labels = powers, col = "blue")
dev.off()

# Print each power value along with its scale-free topology fit and mean connectivity
for (i in 1:length(powers)) {
  cat("Power:", sft$fitIndices[i, 1], 
      " Scale-Free Topology Fit (R^2):", round(-sign(sft$fitIndices[i, 3]) * sft$fitIndices[i, 2], 3),
      " Mean Connectivity:", round(sft$fitIndices[i, 5], 3), "\n")
}
