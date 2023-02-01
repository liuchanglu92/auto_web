# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:29
#Auth : liuchanglu
#File : login_handle.py

"""
from page.login_page import LoginPage


class LoginHanle(object):
    def __init__(self):
        self.login_page = LoginPage()
    def input_username(self,name):
        self.login_page.find_username().send_keys(name)
    def input_pwd(self,pwd):
        self.login_page.find_pwd().send_keys(pwd)
    def click_login(self):
        self.login_page.find_login().click()