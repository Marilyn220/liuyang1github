# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/25 15:14
# @Author  : Chengzy
# @File    : run.py
# @Software: PyCharm
import logging
#from Public.Logs import Log
from Public.ReadConfig import ReadConfig
from Public.check_devices import check_devices
from Public.CaseStrategy import CaseStrategy
import time , os
from Public.RunCase import RunCases
from Public.DrObj import DrObj
from multiprocessing.pool import Pool


def func(d_info,suite):
    print ('当前子进程号为：%s' % os.getpid())
    #print d_info
    drobj = DrObj()
    print ('d_info.get_device :',d_info.get_device())

    if d_info.get_device().get('serial') and d_info.get_device().get('ip'):
        drobj.set_driver(d_info.get_device()['ip'])
        print ("drobj.set_driver(d_info.get_device()['ip'])",drobj.set_driver(d_info.get_device()['ip']))
    else:
        drobj.set_driver(d_info.get_device()['serial'])
        print ("drobj.set_driver(d_info.get_device()['serial'])",drobj.set_driver(d_info.get_device()['serial']))
    #l.info('开始执行测试用例')
    #d_info.run_testcase(suite)
    print ('子进程结束')


def cases(testcase_path):
    cs = CaseStrategy()
    suite = cs.collect_cases(testcase_path)
    return suite





if __name__=='__main__':
    #prodir当前路径
    proDir = os.path.split(os.path.realpath(__file__))[0]
    print ('当前文件路径:%s'%proDir)

    #配置文件路径
    configPath = os.path.join(proDir, "baseconfig.ini")
    print ('配置文件路径:%s'%configPath)

    rc = ReadConfig(proDir)
    #获取用例路径
    testcase_path = rc.get_testcase_path(configPath)
    print ('测试用例路径:%s'%testcase_path)

    log_path = rc.get_log_path(testcase_path)
    print ('log文件路径:%s'%log_path)
    #l = Log().getlog()
    from Public.Logs import JFMlogging
    logging = JFMlogging(log_path).getloger()
    logging.info('aaaaaaaaaaaaaaa')

    #获取报告路径
    test_report_path = rc.get_testreport(testcase_path)
    print ('报告路径:%s'%test_report_path)

    if testcase_path:
        suite = cases(testcase_path)
        if suite==[]:
            print ('suite为空')
            exit()
        cd = check_devices()
        devices_list = cd.check_device(rc)

        if devices_list==False:
            print ('devices_list 为 false')
            exit()
        else:
            print ('所有设备驱动信息如下：%s'%devices_list)
            devices_info = []

            for i in range(len(devices_list)):
                devices_info.append(RunCases(devices_list[i],test_report_path))

            pool = Pool(processes=len(devices_info))
            result = []
            print ('aaaaaaaaaaaaaaaaaaaaaaaa')
            for d_info in devices_info:
                result.append(pool.apply_async(func,(d_info,suite,)))
            pool.close()
            pool.join()
            for i in result:
                print (i.get())
            print ('主进程结束')
    else:
        print ('testcase_path为空')
        exit()