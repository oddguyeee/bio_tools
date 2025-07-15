这段 shell 脚本是用于处理单拷贝直系同源基因序列（Single Copy Orthologue Sequences），执行比对（MAFFT）-剪切（Gblocks）-重命名（seqkit）-拼接（seqkit concat）的一套流程，常用于构建系统发育树前的多序列比对准备。

下面是详细解析：
# 环境、变量

激活 seqkit 环境，seqkit 是一个用于处理FASTA/FASTQ的命令行工具。
```sh
conda activate seqkit
```
定义一个变量 single_copy，指向 OrthoFinder 生成的 单拷贝同源基因目录。
```sh
single_copy=~/PA_flower_color/genomic/present_gen/comparative_gen/orthofinder/primary_transcripts/OrthoFinder/Results_Feb09/Single_Copy_Orthologue_Sequences
```
将所有 .faa 文件（不同物种的蛋白质序列）列出（ll 是 ls -l），输出写入 species.list 文件，便于后续构建 kv 替换文件（用于重命名序列）。
```sh
ll ~/PA_flower_color/genomic/present_gen/comparative_gen/orthofinder/primary_transcripts/*.faa > species.list
```
# 主循环：对每个单拷贝基因做处理
遍历 Single_Copy_Orthologue_Sequences 目录下的每个文件，处理每个单拷贝基因。
```sh
for i in `ls $single_copy`; do
```
去除扩展名（如 .fa, .fasta, .faa）作为前缀名。
```sh
  prefix=${i%.fa*}
```
# 使用 MAFFT 进行多序列比对
```sh
  mafft --maxiterate 1000 --localpair "${single_copy}/${prefix}.fa" > "./${prefix}.aln"
##  使用 MAFFT 进行多序列比对：
##  --localpair: 进行局部比对；
##  --maxiterate 1000: 多次迭代优化；
##  结果写入 ${prefix}.aln 文件。
```
# 使用 Gblocks 进行剪切保守区域
```sh
Gblocks "./${prefix}.aln" -b4=5 -b5=h -t=p -e=.gb
#  使用 Gblocks 去除不可靠区域（gap 多、保守性低的区域）：
#  -b4=5: 要求一个保守块最小长度为5；
#  -b5=h: 半严格模式；
#  -t=p: 蛋白质序列；
#  -e=.gb: 输出扩展名为 .gb。
```
# 将Gblocks结果进一步格式整理（不换行）
将 .gb 文件格式转为一行一条记录的 FASTA 格式，便于后续处理。
```sh
seqkit seq "./${prefix}.aln.gb" -w 0 > "${prefix}.new.aln"
```
获取序列ID（用于重命名）
提取所有序列的 ID（-n）输出到 output.ids。
```sh
seqkit seq -n "${prefix}.new.aln" > output.ids
```
构造 ID 替换键值文件，并进行批量替换。将序列 ID 和之前生成的 species.list 合并为一个两列的文件 combined_output.txt，每行为 原ID\t新ID，用于替换。
```sh
paste output.ids species.list > combined_output.txt
```
用 seqkit replace 替换 FASTA 文件中所有的序列 ID，替换规则来自 combined_output.txt。
替换后的文件写入 temp${prefix} 文件。
```sh
  seqkit replace -p "^(.+)" -r "{kv}" -w 0 --kv-file combined_output.txt "${prefix}.new.aln" > temp${prefix}
#  -p "^(.+)": 匹配原始 ID；
#  -r "{kv}": 用键值替换；
#  -w 0: 不换行；
```
# 拼接所有单拷贝基因
将所有临时文件（temp*）拼接为一个总对齐文件 sing_copy_pro.aln，用于系统发育树构建。
```sh
seqkit concat temp* -w 0 -o sing_copy_pro.aln

# 删除临时文件和 Gblocks 可能生成的中间文件 N0*。确保结果无误后再删除
rm temp* N0*
```
