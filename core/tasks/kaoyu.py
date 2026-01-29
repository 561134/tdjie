#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import client_offset


# 领取烤鱼任务
class KaoyuTask(BaseTask):
    name = "烤鱼"
    order = 90
    def run(self, stop_event: threading.Event):
        print(">>> 烤鱼任务开始")
        off_kaoyu = client_offset()# 定义相对窗口坐标偏移量
        time.sleep(3)
        if match_pics(template_path='tdjimages/kaoyu.png'):
            print("点击领取烤鱼")
            click_coord(match_pics(template_path='tdjimages/kaoyu.png'),do_click=True)
            time.sleep(3)
            if match_pics(template_path='tdjimages/kaoyu_get.png'):
                print("匹配到烤鱼获取图标 点击固定坐标118 620")
                click_coord([(off_kaoyu[0] + 118, off_kaoyu[1] + 620, 1.0)],do_click=True,clicks=2)
                time.sleep(2)
        else:
            print("没有烤鱼")
        while not match_pics(template_path='tdjimages/qicheng.png'):
            print(">>> 未匹配到启程图标 继续等待")
            time.sleep(3)
        print(">>> 烤鱼任务结束 当前营地界面")