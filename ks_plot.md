setwd("E:/Li/flower_color/wgd/Ks_plots-master/")

r_files <- list.files(pattern = "\\.R$")

# 逐个加载这些文件
for (file in r_files) {
  source(file)
}

x <- read.table("Pflo.ksNG86",header = T)

ks_NG86 <- x$ks_NG86

summary(ks_NG86)  # 查看数据摘要

ploidy_result <- ploidy.test(ks_NG86)

# 自动模型选择
bic_results <- bic.test.wgd(
  x = ks_NG86,
  startK = 2,
  maxK = 5,
  model = 1,
  nstarts = 100,
  outPrefix = "pf_raw_bic"
)

# 手动优化（示例）
K4 <- mixEM(ks_NG86, k=4, model=4, nstarts=100)
K3 <- mixEM(ks_NG86, k=3, model=4, nstarts=100)
K2 <- mixEM(ks_NG86, k=2, model=4, nstarts=100)
print(K4)
print(K3)
print(K2)

# 绘图

# 打开 PDF 设备
pdf("K4plotComponents.pdf", width = 8, height = 6)

# 绘制图形
plotComponents(
  x = ks_NG86,
  lambda = K4$lambda,
  params = K4$parameters,
  model = 4
)

# 关闭 PDF 设备
dev.off()

# 打开 PDF 设备
pdf("K3plotComponents.pdf", width = 8, height = 6)

# 绘制图形
plotComponents(
  x = ks_NG86,
  lambda = K3$lambda,
  params = K3$parameters,
  model = 4
)

# 关闭 PDF 设备
dev.off()

# 关闭 PDF 设备
dev.off()

# 打开 PDF 设备
pdf("K2plotComponents.pdf", width = 8, height = 6)

# 绘制图形
plotComponents(
  x = ks_NG86,
  lambda = K2$lambda,
  params = K2$parameters,
  model = 1
)

# 关闭 PDF 设备
dev.off()


library(ggplot2)


p2 <- ggplot(x, aes(x = ks_median)) +
  geom_density(color = "darkblue", fill = "lightblue", alpha = 0.5)


pdf("basedist.pdf", width = 8, height = 6)
p2
dev.off()
