# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:29
#Auth : liuchanglu
#File : login_task.py

"""
from time import sleep

from handle.login_handle import LoginHanle


class LoginTask(object):
    def __init__(self):
        self.login_handle = LoginHanle()
    def login_menthod(self,name,pwd):
        self.login_handle.input_username(name)
        self.login_handle.input_pwd(pwd)
        sleep(2)
        self.login_handle.click_login()