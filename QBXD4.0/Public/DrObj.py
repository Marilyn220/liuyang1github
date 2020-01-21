#coding=utf-8
#from Public.Logs import Log
import uiautomator2 as u2

class DrObj(object):
    @classmethod
    def set_driver(cls, dri):
        cls.d = u2.connect_usb(dri)

    def get_driver(self):
        return self.d