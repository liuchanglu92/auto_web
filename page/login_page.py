# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:26
#Auth : liuchanglu
#File : login_page.py

"""
from time import sleep

from selenium.webdriver.common.by import By

from utils import DriverUtils


class LoginPage(object):
    def __init__(self):
        self.driver = DriverUtils().get_driver()
    def find_username(self):
        return self.driver.find_element(By.XPATH, '//*[@placeholder="请输入账号"]')
    def find_pwd(self):
        return self.driver.find_element(By.XPATH, '//*[@placeholder="输入密码"]')
    def find_login(self):
        return self.driver.find_element(By.XPATH, '//*[@class="login_btn"]')



