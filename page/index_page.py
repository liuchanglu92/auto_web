# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:25
#Auth : liuchanglu
#File : index_page.py
首页页面
"""
from selenium.webdriver.common.by import By

from utils import DriverUtils


class IndexPage(object):
    """首页对象层"""
    def __init__(self):
        self.driver = DriverUtils().get_driver() #获取浏览器对象

    def find_login(self):
        return self.driver.find_element(By.XPATH, '//*[@class="login_way login_by_mima"]')



