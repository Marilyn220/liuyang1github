# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/31 14:34
# @Author  : Chengzy
# @File    : t.py
# @Software: PyCharm


import re,os
import subprocess
from subprocess import Popen,PIPE
from multiprocessing.pool import Pool
import uiautomator2 as u2

#查找设备信息
class check_devices:

    def check_device(self):
        l = ['172.28.66.234:7545', '172.28.66.234:7477', '172.28.66.234:7413']
        dr_lists = l
        devices_list = self.connect_devices(dr_lists)
        return devices_list

    def connect_devices(self,dr_lists):
        print ('dr_list is %s'%dr_lists)
        if dr_lists==[]:
            return False
        for dr in dr_lists:
            loutput = subprocess.check_output(['adb','connect',dr])
            out = loutput.decode()
            if 'unable to'in out:
                continue

        for dr in dr_lists:
            loutput = subprocess.check_output(['adb', 'connect', dr])
            out = loutput.decode()
            if 'unable to' in out:
                continue
        output = subprocess.check_output(['adb', 'devices'])
        #print ('找到的信息如下：%s')%output
        #output = output.decode()
        pattern = re.compile(
            r'(?P<serial>[^\s]+)\t(?P<status>device|offline)')
        matches = pattern.findall(output.decode())
        valid_serials = [m[0] for m in matches if m[1] == 'device']
        print ('valid_serials is :',valid_serials)

        if valid_serials==[]:
            output = subprocess.check_output(['adb', 'devices'])
            # print ('找到的信息如下：%s')%output
            # output = output.decode()
            pattern = re.compile(
                r'(?P<serial>[^\s]+)\t(?P<status>device|offline)')
            matches = pattern.findall(output.decode())
            valid_serials = [m[0] for m in matches if m[1] == 'device']
            #print('valid_serials is :', valid_serials)
        if valid_serials:
            print('Start check %s devices connected on PC: ' % len(valid_serials))
            pool = Pool(processes=len(valid_serials))
            tmp_list = []
            for run in valid_serials:
                tmp_list.append(pool.apply_async(self.check_alive, args=(run,)))
            pool.close()
            pool.join()
            devices_list = []
            for i in tmp_list:
                if i.get():
                    devices_list.append(i.get())
            return devices_list
        if len(valid_serials) == 0:
            print("未找到可用的设备--代码结束.")
            return False

    def check_alive(self,device):
        print ('正在执行check_alive的子进程信息')
        if device:
            d = u2.connect_usb(device)
            if d.agent_alive:
                d.healthcheck()
                if d.alive:
                    if re.match(r"(\d+\.\d+\.\d+\.\d)", device):
                        dict_tmp = d.device_info
                        dict_tmp['ip'] = device
                        print('%s is alive' % device)
                    else:
                        dict_tmp = d.device_info
                    return dict_tmp
                else:
                    print('%s is not alive' % device)
                    return None
            else:
                print('The device atx_agent %s  is not alive,please checkout!' % device)
                return None


if __name__=="__main__":
    c = check_devices()
    c.check_device()