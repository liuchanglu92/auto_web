# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:27
#Auth : liuchanglu
#File : test_login.py

"""
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from task.index_task import IndexTask
from task.login_task import LoginTask
from utils import DriverUtils, get_alter_msg


class TestLogin(object):
    """登录测试类"""
    def setup_class(self):
        self.driver = DriverUtils.get_driver() #获取浏览器对象
        self.index_task = IndexTask() #实例化首页业务层对象
        self.login_task = LoginTask()
    def teardown_class(self):
        sleep(2)
        DriverUtils.quit_driver()
    def setup(self):
        self.driver.get('https://1.cih-index.com/sys/v2/kfyLogin')
        #self.driver.find_element(By.XPATH, '//*[@class="login_way login_by_mima"]').click()
        self.index_task.go_to_login() #切换登录
    def teardown(self):
        pass

    def test_account_does_not_exist(self):
        self.login_task.login_menthod('zhangxiaoxing1@fang.com','industry369')
        # self.driver.find_element(By.XPATH, '//*[@placeholder="请输入账号"]').send_keys('zhangxioaxing1@fang.com')
        # self.driver.find_element(By.XPATH, '//*[@placeholder="输入密码"]').send_keys('industry369')
        # sleep(2)
        # self.driver.find_element(By.XPATH, '//*[@class="login_btn"]').click()
        #获取alter弹窗值
        # msg=get_alter_msg()
        # print('alter值',msg)
    def test_wrong_password(self):
        self.login_task.login_menthod('zhangxiaoxing@fang.com', 'industry3691')
        # self.driver.find_element(By.XPATH, '//*[@placeholder="请输入账号"]').send_keys('zhangxioaxing@fang.com')
        # self.driver.find_element(By.XPATH, '//*[@placeholder="输入密码"]').send_keys('industry369')
        # sleep(2)
        # self.driver.find_element(By.XPATH, '//*[@class="login_btn"]').click()


if __name__ == '__main__':
    pytest.main(['-s','baidu_login.py'])