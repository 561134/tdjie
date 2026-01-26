#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口


# 好友任务
class HaoyouTask(BaseTask):
    name = "好友"
    order = 10
    def run(self, stop_event: threading.Event):
        print(">>> 好友任务开始")
        # 领取 & 赠送
        time.sleep(3)
        print("匹配好友图标 点击好友图标")
        click_coord(match_pics('tdjimages/haoyou.png'), do_click=True)
        time.sleep(3)
        print("匹配好友全部领取图标 点击好友全部领取")
        click_coord(match_pics('tdjimages/haoyou_lingqu.png'), do_click=True)
        time.sleep(2)
        print("匹配好友全部赠送图标")
        click_coord(match_pics('tdjimages/haoyou_zengs.png'), do_click=True)
        time.sleep(2)
        # 一直匹配到启程图标 才会退出循环
        while not match_pics(template_path='tdjimages/qicheng.png'):
            click_coord(match_pics(template_path='tdjimages/haoyou_back.png'),do_click=True)
            time.sleep(3)# 点击返回
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 手动停止好友任务")
                return
        print(">>> 好友任务完成 成功返回营地界面")
