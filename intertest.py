# coding = utf-8
import requests
import datetime
import time
import threading
import json

class url_request():
    times = []
    error = []
    def req(self):
        myreq=url_request()
        header={'token':'2a50fcd520084efd9be1f65c9985179b','Content-Type':'application/json;charset=UTF-8'}
        datainfo ={"sourceOrganizationNo":"O20160901100001","sourceProduct":"01","channel":"01","productType":"28"}
        datainfo2 = json.dumps(datainfo)
        r = requests.post("http://172.28.38.83/merchant/api/credit/queryMerchantCredit", headers=header, data=datainfo2)
        ResponseTime=float(r.elapsed.microseconds)/1000 #获取响应时间，单位ms
        myreq.times.append(ResponseTime) #将响应时间写入数组
        if r.status_code !=200 :
            myreq.error.append("0")
if __name__=='__main__':
    myreq=url_request()
    threads = []
    starttime = datetime.datetime.now()
    print("request start time %s" %starttime)
    nub = 10#设置并发线程数
    ThinkTime = 0.5#设置思考时间
    for i in range(1, nub+1):
        t = threading.Thread(target=myreq.req)
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        #print "thread %s" %t #打印线程
        t.setDaemon(True)
        t.start()
        t.join()
    endtime = datetime.datetime.now()
    print("request end time %s" %endtime)
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times))) #计算数组的平均值，保留3位小数
    print("Average Response Time %s ms" %AverageTime)#打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second) #计算总的思考时间+请求时间
    print("Concurrent processing %s" %nub) #打印并发数
    print ("use total time %s s" %(totaltime-float(nub*ThinkTime))) #打印总共消耗的时间
    print ("fail request %s" %myreq.error.count("0")) #打印错误请求数
