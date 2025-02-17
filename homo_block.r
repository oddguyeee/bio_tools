df <- read.csv("ath_block_information.csv")

tandem_length <- 200

df$start <- df$start2 - df$start1
df$end <- df$end2 - df$end1

df_tandem <- df[abs(df$start) <= tandem_length |
     abs(df$end) <= tandem_length,]

gff <- read.table("ath.gff")

syn_block1 <-  df_tandem[1,c("block1", "block2")]

gene_order <- unlist(
  lapply(syn_block1, strsplit, split="_", fixed=TRUE, useBytes=TRUE)
)

gene_order <- unique(as.numeric(gene_order))


syn_block1_gene <- gff[ gff$V6 %in% gene_order, "V2"]

#BiocManager::install("org.At.tair.db")
library(org.At.tair.db)
library(clusterProfiler)

ego <- enrichGO(syn_block1_gene, 
                OrgDb = org.At.tair.db, 
                keyType = "TAIR",ont = "BP"
                )
dotplot(ego)
