### For each split of the features, perform WGCNA and generate adjacency matrix. 

data_folder = "/work/home/nhkim/BiS495/GNN/input_features_labels"
output_folder = "/work/home/nhkim/BiS495/GNN/input_adjacency_matrix"

data_file = paste(data_folder, "split10_train_features.csv", sep='/')
dir.create(paste(output_folder))
# WGCNA parameters
wgcna_power = 7
wgcna_minModuleSize = 10
wgcna_mergeCutHeight = 0.25
data = read.csv(data_file, header=F) # each row is a patient
geneExp = as.matrix(data[2:dim(data)[1], 2:dim(data)[2]])

# gene as columns for WGCNA
# geneExp = t(geneExp)
dim(geneExp)

## imputate the NA by zero values.
geneExp[is.na(geneExp)]<-0

library(WGCNA)
adjacency = adjacency(geneExp, power = wgcna_power)
write.csv(adjacency,file=paste(output_folder, "split10_adjacency_matrix.csv", sep='/'),quote=F,row.names = F)