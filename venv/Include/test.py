#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import subprocess
import sys

k = 0
result = []
if (os.path.exists("log")):
    subprocess.call(["rm -rf  log"], shell=True)

# 给readme.txt加可执行权限
subprocess.call(["chmod a+x readme.txt"], shell=True)
# 删除readme.txt中的注释行和空格行并重定向给Shell_update.txt
subprocess.call(["sed  '/^#.*\|^$/d' readme.txt > Shell_update.txt"], shell=True)
# 将Shell_update.txt中的所有88888888行--99999999行之间的内容重定向给变量名文件（1，2，3.....）
subprocess.call(["cat Shell_update.txt | awk '/888/{++i;f=1} f{print $0>i}/999/{f=0}'"], shell=True)
# 将Shell_update.txt中的所有88888888行-99999999行之间的内容删除
subprocess.call(["sed -i '/888/,/999/{//!d}' Shell_update.txt"], shell=True)
# 将Shell_update.txt中的所有888888行和9999999999行的内容全部删除
subprocess.call(["sed -i '/^888.*\|^999/d' Shell_update.txt"], shell=True)
# 将Shell_update.txt中的所有空行内容全部删除
subprocess.call(["sed -i /^[[:space:]]*$/d Shell_update.txt"], shell=True)
# 消除dos下的换行符
subprocess.call([" tr -d ‘\r’< Shell_update.txt > unixfile.txt"], shell=True)
for x in range(1, 20):
    z = str(x)
    if (os.path.exists(z)):
        subprocess.call(["sed -i '/^888.*\|^999/d' " + z], shell=True)
# 读取Shell_update.txt中的每一行并存到result【】数组内
with open('unixfile.txt', 'r') as f:
    for line in f:
        result.append(list(line.strip('\n').split(',')))
# res=[1]*len(result)

# 遍历每一条指令
for i in range(len(result)):

    str1 = "".join(result[i])

    str7 = str1[0:2]
    print
    "正在执行命令  " + str1
    # 若有vi 指令则直接将vi命令下面的文本重定向给目标地址文件
    if ('vi' in str7):

        k += 1
        m = str(k)
        str3 = str1.replace('vi', '')
        print(str3)
        o = subprocess.call(["cat " + m + " > " + str3], shell=True)
        if (o == 0):
            subprocess.call(["echo  执行成功 : 第" + str(i + 1) + "行指令:   " + str1 + " >> log"], shell=True)
            subprocess.call([" echo >> log"], shell=True)
            print
            "【\033[1;32;40m OK \033[0m】" + str1
        else:
            subprocess.call(["echo  执行失败 : 第" + str(i + 1) + "行指令:   " + str1 + " >> log"], shell=True)
            print
            "【\033[1;31;40m ERROR \033[0m】" + str1
    else:
        o = subprocess.call(result[i], shell=True)
        str5 = "".join(result[i])
        if (o == 0):
            subprocess.call(["echo  执行成功 : 第" + str(i + 1) + "行指令:   " + str5 + " >> log"], shell=True)
            subprocess.call([" echo >> log"], shell=True)
            print
            "【\033[1;32;40m OK \033[0m】" + str5

        else:
            subprocess.call(["echo  执行失败 : 第" + str(i + 1) + "行指令:   " + str1 + " >> log"], shell=True)
            subprocess.call([str5 + " 2>> log"], shell=True)
            subprocess.call([" echo >> log"], shell=True)
            print
            "【\033[1;31;40m ERROR \033[0m】" + str5
    if ((i + 1) == len(result)):
        print
        "\033[1;32;40m Complete! \033[0m"

if (os.path.exists("Shell_update.txt")):
    subprocess.call(["rm -rf  Shell_update.txt"], shell=True)
if (os.path.exists("unixfile.txt")):
    subprocess.call(["rm -rf  unixfile.txt"], shell=True)
for x in range(1, 20):
    z = str(x)
    if (os.path.exists(z)):
        subprocess.call(["rm -rf " + z], shell=True)









