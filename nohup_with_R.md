假设现在有5个R脚本：

`step1.R`
```R
# 睡眠 5 分钟（300 秒）
Sys.sleep(300)

# 打印提示信息
cat("This is step1\n")
```
`step2.R`
```R
# 睡眠 5 分钟（300 秒）
Sys.sleep(300)

# 打印提示信息
cat("This is step2\n")
```
...
`step5.R`
```R
# 睡眠 5 分钟（300 秒）
Sys.sleep(300)

# 打印提示信息
cat("This is step5\n")
```
<img width="472" height="109" alt="image" src="https://github.com/user-attachments/assets/be60b623-0c49-4cfe-9ce0-c6748c6a81fa" />

现在可在linux bash，使用下列命令批量提交：
```sh
timestamp=$(date +%Y%m%d%H%M%S)
for i in {1..5}; do
  nohup Rscript step${i}.R > ${timestamp}-step${i}.out &
  sleep 1
done
```
<img width="733" height="247" alt="image" src="https://github.com/user-attachments/assets/d97afd34-db14-4bd1-b7bb-9703877afa2d" />

<img width="468" height="24" alt="image" src="https://github.com/user-attachments/assets/20d9416f-c1e0-4340-8991-6aac1fea69c3" />

提交后，`nohup`将程序挂起,避免用户离线后任务终止。末尾的`&`将任务放至后台运行，避免占用命令行。提交完成后，可使用`top -u liusuguo`查看任务进度（注意`liusuguo`为你登录服务器时使用的用户名）：

<img width="1610" height="460" alt="image" src="https://github.com/user-attachments/assets/de0eebfd-6e32-48d7-a607-fdc11fa91d34" />
`top`界面内按`c`可查看命令的具体信息。
<img width="1480" height="476" alt="image" src="https://github.com/user-attachments/assets/4eb54845-a3ad-4251-9de4-2c563876dc9e" />
