# Alzheimer diagnosis with blood transcriptome

This repository contains the code and methodology used for predicting Alzheimer’s disease using blood transcriptome data via a Graph Neural Network (GNN). The goal is to predict Alzheimer's disease stages based on the expression of blood transcriptome features and using deep learning methods such as GNN.


### Overview

Alzheimer's disease is a neurodegenerative condition that leads to cognitive decline. Early diagnosis plays a crucial role in managing and potentially treating the disease. In this project, we use blood transcriptome data to predict the onset and progression of Alzheimer's disease by leveraging Graph Neural Networks (GNN). The data consists of gene expression profiles that are transformed into a graph structure to capture the interactions between genes, which are then analyzed for prediction.


### Dataset

The dataset used in this project includes gene expression profiles from three sources:

AddNeuroMed (ANM1, ANM2): Gene expression data from patients categorized as Alzheimer’s Disease (AD), Mild Cognitive Impairment (MCI), and Cognitively Normal (CN).

ADNI: The Alzheimer’s Disease Neuroimaging Initiative dataset, containing similar categories (AD, MCI, CN).

Total number of samples:

ANM1: 329 samples (145 AD, 80 MCI, 104 CN)

ANM2: 382 samples (139 AD, 109 MCI, 134 CN)

ADNI: 713 samples (98 AD, 371 MCI, 244 CN)


### Methodology

![image](https://github.com/user-attachments/assets/50322ba8-c714-415f-a024-8a49a65c3640)


#### 1. Data Preprocessing

**DEGs (Differentially Expressed Genes)**: 479 genes were selected based on their relevance to Alzheimer’s disease.

**WGCNA**: Weighted Gene Co-expression Network Analysis was used to construct a gene co-expression network and calculate edge matrices.

**Gene Co-expression Graph**: Nodes represent genes, and edges represent gene interactions. These were constructed using WGCNA and used as input for the GNN.


#### 2. Model Architecture
The model consists of several key components:

**Gene Co-expression Network Construction**: A graph is created from the gene expression data where nodes represent genes, and edges represent co-expression relationships.

**GNN Model**: A multi-level graph is constructed and passed through several Graph Attention Network (GAT) layers. The features from these layers are fully fused for prediction.

**Fully Connected (FC) Layers**: The output of the GNN layers is passed through fully connected layers (1437 → 128 → 96 → 64 → 32 units) for final classification.

**Prediction**: The final output is predicted using a sigmoid activation function (0 to 1), representing the probability of the sample being Alzheimer's-related.


#### 3. Evaluation Metrics
The model is evaluated using standard classification metrics, such as accuracy, precision, recall, and F1-score.


### References
1. Xiaohan Xing et al., Multi-level attention graph neural network based on co-expression gene modules for disease diagnosis and prognosis. Bioinformatics, Volume 38, Issue 8, March 2022
The implementation of the MLA-GNN model used in this project is based on the code available in the Tencent AILab Healthcare GitHub repository.
2. Lee T., Lee H., Prediction of Alzheimer’s disease using blood gene expression data. Sci Rep 10, 3485, 2020
