# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/2/18 11:22
# @Author  : Chengzy
# @File    : views.py
# @Software: PyCharm

from . import pay
import json
from flask import request
#https://sit-apis.csdnpay.com
@pay.route('/v1/id_auth',methods=['GET','POST'])
def hello():
    if request.method == "POST":
        print('*****************二要素请求**************')
        print ('走的是post请求')
        print ('url:', request.url)
        print ('请求参数如下：',request.json,type(request.json))

    #返回固定的信息，但程序只对信息标识做判断 并未取标识内信息
        respone = {
                "SIGN": "sig72pyE1YVIP3Bwp9CJivIREAm6OlTquF8QS4yTlRk/6AT/rAHdFhyzskwN47YCYWHrrmOroNCsdY4RkSEsIOmd5gulUG1K5oeKZgu2YzvIzIuJoR5m/DEpIJUJciafhk+BW2FPoc8uvzP7nAC6AQuVZ4Bwbx9RDb4680VF8Sk=",
                "MERCHANT": "100000160123822",
                "CER": "m2TeYsan4eqM6C4JJJ7v/VijZRikEfxnN5Yfs5TFY/mZRHOdo0TXLIevFO1qmkDd1IdHWaMMnhCtFdh0RbVmN1R/mJqcdn0pQQQEQEgWC5i8VDldHWJDFWR1VtS3SC/8ab7vn+KVyqntflxSMPwabaT92/rMVruUeFfLav7CRZo=",
                "DATA": "IgODcvtgnU37eoqywlq5igq4QI3Jpr0z6QFUOIP+FZTwQTUTYG6MCzG/Ocil1+eJwiNRHh4konYp1vsHCz3pWhXxrFaHPWdDUFJ3uVUaZGTGDdBVZyVu0v32radYAvAY6ud6hYIxFsdcq9kS0wgoANQcYI17Hs6dw0BE6jj2/lqop4r2tbzvWOrd3QxKYIW7L3lAnT8pZYgNww05pOn21Y4F1oKdRMFfYXq1sikkiOu1BkabJcrmaExYtIh1cG9Y"
            }

        return json.dumps(respone)
    else:
        return '走的是易贷绑卡get 请求'



@pay.route('/v1/sign_apply',methods=['GET','POST'])
def hello1():
    if request.method == "POST":
        print ('走的是post请求')
        print ('请求参数如下：',request.json,type(request.json))

    #返回固定的信息，但程序只对信息标识做判断 并未取标识内信息
        respone = {
            "SIGN":"VwdzCt/Q/7ol23cfGy5EN+QAwiIqvOa+T3Bq2tKg4Kd6qpa8cKscgTWq+nT0aZARmUBizyjNSxRc9fctyN9ANUCJQLicKGgyrEFpxXRIb3kjsb14k4UxrNj5M7vwsRryrud6CgLXlieYa4IXZnQFOjmUrUhi/EiI7QBW+TrVZD0=",
            "MERCHANT":"100000160123822",
            "CER":"d+7Kfg8awgDbX39nxw1D09vzLVrCgdGhGG3j26X9dv97z7vX4W9qOpTEkSC0707rg+Bw7KtChh1jojlRJqDvvOh4B6GcxCKB/kdlyx6UKOKEXFYUSR3A7SUFiIhy+Ki/9NmO04jurzG1Oj+Gm/3eP/XGzYd6B6VxD3mC1ayx3Jo=",
            "DATA":"Pww+FlY2b4RmUg2bitLXr0kcISLd2e/iPJQeoNk9RD1fBiq8Z+8EW7XnvpBJjXdcT3VY5h3/3TyNQSob5diqaIiDn8k6vZKf3JH67u6+Dh2CJDHgQulChzZS/xXL6hy09JzcKPx0ao20X7zPNjrulvLce8Knd2FOPRqEkaJ7VLlGN7KiQZ3nL13knwEf7S0ZlX1lcCd3iCnkUadfZJAFiWUU5YF+86gk0xfwAoX3FeZ1ROF3/PzL6m8P6HlezPPM+VrhyrDSZhErO9AT35V1/Q=="
        }

        return json.dumps(respone)
    else:
        return '走的是商户贷绑卡发短信get 请求'




@pay.route('/v1/sign_confirm',methods=['GET','POST'])
def hello2():
    if request.method == "POST":
        print ('走的是post请求')
        print ('请求参数如下：',request.json,type(request.json))

        #返回固定的信息，但程序只对信息标识做判断 并未取标识内信息
        respone = {
            "SIGN":"QiqseIfE8fYYBo2uBlnf8bGMk5njFQplMMofRCHwWWnTlwcwhUxF3QtUKNl1WvNrTh56wLjyuu7aDBclgjjWUXFW165/8JyoNpBqRZdjaaPig4BMsOzcaW3yhrrVUpmBeaTK1FH+Bvalme1frYgAKCUJ4tzt/yRn8M2d2Njnq3Y=",
            "MERCHANT":"100000160123822",
            "CER":"Z0A+P4UMySTYxs4mTTY4DmI6L+lv5IdpWGaszHU+3XrwfKzOX6E4n2TXMkaG2aUKFiQH4/e1lEuL1RxatksVhw921UfiAE1az7zC4jqPYuTkqdeqYD9tT9E6IfkJB39VbIeNKsxWUqe7sDJ9XlahACsUlkjdqKdqQv1EaZXp5GM=",
            "DATA":"pxzEU6qvWtgKx41U0Y3I+Fu2RWGvUddl3ilMYcXf1nYD/kG1n4yhzB0P0mll04Kvz7yzWpczyaf19h+fUu224ZN7U8FanqpsAtOVG+fQubLiPIjWp6Fs7foLXlQSgm8ZpaBmcOJzD7O6HN6expnqKD3SC9PPUd3B9D0cJcdyWtpZCSo/oovu7lqJ1kSAN7IaUZF8KXXfHRF5RXkccx0Y3OqsbalWQd3r14Z/k/tkizt9W1ojT3cdRCLv7NSnLF3RcXQ6s5L8t2Yx9FT/A3CP+w=="
        }

        return json.dumps(respone)
    else:
        return '走的是商户贷绑卡确认短信get 请求'