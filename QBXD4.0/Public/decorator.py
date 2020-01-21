# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/1/17 16:42
# @Author  : Chengzy
# @File    : decorator.py
# @Software: PyCharm

from run import log_path
# print log_path
# from Public.Logs import JFMlogging
# logger = JFMlogging(log_path).getloger()
# logger.info('bbbbbbbbbbbbbbbb')
#from Logs import Log
#

def step(*dargs,**dkwargs):
    def wrapper(func):
        def _wrapper(*args,**kwargs):
            #l = Log(func.__name__).getlog()
            #l = Log().getlog()
            #print 'decorator param:' ,dargs, dkwargs
            #print 'function param:',args[1:], kwargs
            #l.info('decorator param:%s--%s'%(dargs, dkwargs))
            #l.info('function param: %s--%s'%(args[1:],kwargs))
            return func(*args,**kwargs)
        return _wrapper
    return wrapper



