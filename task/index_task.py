# -*- coding:utf-8 -*-#
"""
#Time : 2023/2/1 19:28
#Auth : liuchanglu
#File : index_task.py

"""
from handle.index_handle import IndexHandle


class IndexTask(object):
    """首页业务层"""
    def __init__(self):
        self.indexhandle = IndexHandle() #获取操作层对象

    def go_to_login(self):
        self.indexhandle.click_login()