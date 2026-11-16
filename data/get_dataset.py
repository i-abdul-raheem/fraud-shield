import gdown

FILE_ID = "1A7B3VUXwDuzLBsjoCtjQMBDEfV6NCUvt"

gdown.download(
    id=FILE_ID,
    output="data/paysim_1.csv",
    quiet=False
)
