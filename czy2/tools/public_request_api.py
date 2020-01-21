# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/7 13:41
# @Author  : Chengzy
# @File    : public_request_api.py
# @Software: PyCharm

import requests,json
from  requests import exceptions
class TestRequest():
    def __init__(self,session):
        self.session = session

    def get(self, url,headers,parms,**kwargs):#get消息
        try:
            self.r = self.session.get(url, headers=headers,params=parms,timeout=30,**kwargs)
            self.r.encoding = 'UTF-8'
            spend=self.r.elapsed.total_seconds()
            json_response = json.loads(self.r.text)
            return json_response,spend
        except exceptions.Timeout :
            return {'get请求出错': "请求超时" }
        except exceptions.InvalidURL:
            return {'get请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'get请求出错': "http请求错误"}
        except Exception as e:
            return {'get请求出错':"错误原因:%s"%e}

    def json_post(self, url, data, headers):  # post消息
        data = json.dumps(data)
        try:
            self.r = self.session.post(url, data=data, headers=headers)
            #self.r = requests.post(url, data=data, headers=headers)
            #json_response = json.loads(self.r.text)
            json_response = self.r.json()
            spend = self.r.elapsed.total_seconds()
            return json_response, spend
        except exceptions.Timeout:
            return {'post请求出错': "请求超时"}
        except exceptions.InvalidURL:
            return {'post请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'post请求出错': "http请求错误"}
        except Exception as e:
            return {'post请求出错': "错误原因:%s" % e}


    def from_post(self, url, data, headers,**kwargs):  # post消息
        try:
            self.r = self.session.post(url, data=data, headers=headers,**kwargs)
            json_response = self.r.json()
            spend = self.r.elapsed.total_seconds()
            return json_response, spend
        except exceptions.Timeout:
            return {'post请求出错': "请求超时"}
        except exceptions.InvalidURL:
            return {'post请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'post请求出错': "http请求错误"}
        except Exception as e:
            return {'post请求出错': "错误原因:%s" % e}


    def get_imgcode_get(self, url):  # 获取图片验证码.url 中需要带手机号
        try:
            print ('图片验证码url：',url)
            self.r = self.session.get(url)
            con = self.r.text
            #print (con)
            ds = con[con.rfind("{"):]
            dict_response = eval(ds)
            spend = self.r.elapsed.total_seconds()
            return dict_response
        except exceptions.Timeout:
            return {'post请求出错': "请求超时"}
        except exceptions.InvalidURL:
            return {'post请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'post请求出错': "http请求错误"}
        except Exception as e:
            return {'post请求出错': "错误原因:%s" % e}