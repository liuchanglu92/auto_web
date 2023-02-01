# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:24
#Auth : liuchanglu
#File : utils.py
公共方法模块
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


def get_alter_msg(by,value):
    msg = DriverUtils.get_driver().find_element(By.XPATH,'//p[@class="alertbox"]')
    return msg
class DriverUtils(object):
    __drover = None  #浏览器默认初始状态,只需要在类内部使用，因此定义为私有变量
    @classmethod
    def get_driver(cls):
        if cls.__drover is None:
            cls.__drover = webdriver.Chrome()
            cls.__drover.get('https://1.cih-index.com/sys/v2/kfyLogin')
            cls.__drover.maximize_window()  # 窗口最大化
            cls.__drover.implicitly_wait(10)  # 隐式等待 测试环境10s，正式环境30s。
        return cls.__drover
    @classmethod
    def quit_driver(cls):
        if cls.__drover is not None:
            sleep(2)
            cls.__drover.quit()
            cls.__drover=None

if __name__ == '__main__':
    # my_driver = DriverUtils()
    # my_driver.get_driver()
    # sleep(2)
    # my_driver.quit_driver()
    DriverUtils.get_driver()
    sleep(2)
    DriverUtils.quit_driver()