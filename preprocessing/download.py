import GEOparse

gsenum = ["GSE63061"]
for gn in gsenum:
    gse = GEOparse.get_GEO(geo=gn, destdir="./data")