# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/31 17:40
# @Author  : Chengzy
# @File    : tt.py
# @Software: PyCharm

import multiprocessing
import os,time


def a()

def run_p(name):
    print ('ccccccccccccccccccc{0},{1}'.format(name,os.getpid()))
    time.sleep(2)

if __name__ == '__main__':

    p = multiprocessing.Pool(processes=3)
    l = []
    for i in range(6):
        print ('11111111111')
        l.append(p.apply_async(run_p, args=(i,)))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')
    for x in l:
        print (x.get())