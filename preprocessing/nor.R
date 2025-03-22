# install the core bioconductor packages, if not already installed
source("http://bioconductor.org/biocLite.R")
biocLite()

# install additional bioconductor libraries, if not already installed
biocLite("GEOquery")  # Get data from NCBI Gene Expression Omnibus (GEO)
biocLite("affy")  # Methods for Affymetrix Oligonucleotide Arrays
BiocManager::install("oligo")
biocLite("illuminaHumanv3.db", type = "source")  # GSE1297: Platform_title = [HG-U133A]
biocLite("hgu133acdf")