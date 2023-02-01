# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:28
#Auth : liuchanglu
#File : index_handle.py

"""
from page.index_page import IndexPage


class IndexHandle(object):
    """首页操作层"""
    def __init__(self):
        self.index_page = IndexPage()   #获取对象层对象

    def click_login(self):
        self.index_page.find_login().click()