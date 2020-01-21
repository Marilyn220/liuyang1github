# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/6 19:20
# @Author  : Chengzy
# @File    : creat_username_phone.py
# @Software: PyCharm
from datetime import date
from datetime import timedelta
import random as r
import os
def createusername():

    a1=['张','金','李','王','赵','孙','周','吴','郑','窦','章']

    a2=['玉','明','龙','芳','军','玲','海','德','机','简','多']

    a3=['','立','玲','','国','','浩','初','有','构','询','笔','各','码','小']

    name=r.choice(a1)+r.choice(a2)+r.choice(a3)
    return name


def createPhone():
    prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
    return r.choice(prelist)+"".join(r.choice("0123456789") for i in range(8))


def getdistrictcode():
    codelist = []
    print (os.getcwd())
    file_path = os.path.split(os.path.realpath(__file__))[0]
    print (file_path)
    path = os.path.join(file_path,'districtcode.txt')
    file = open(path,'r',encoding='gbk')
    #file = open(file_path + '/districtcode.txt')
    lines = file.readlines()  # 逐行读取
    for line in lines:
        if line.lstrip().rstrip().strip() != '' and (line.lstrip().rstrip().strip())[:6][
                                                    -2:] != '00':  # 如果每行中去重后不为空，并且6位数字中最后两位不为00，则添加到列表里。（最后两位为00时为省份或地级市代码）
            codelist.append(line[:6])
            # print(line[:6])
            # print(codelist)
    return codelist

def gennerator():
    codelist = getdistrictcode()
    id = codelist[r.randint(0, len(codelist))]  # 地区项
    id = id + str(r.randint(1950, 1998))  # 年份项
    da = date.today() + timedelta(days=r.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(r.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count % 11)]  # 算出校验码
    return id


if __name__=='__main__':
    print (gennerator())