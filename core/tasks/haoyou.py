#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import get_window_size

# 好友任务
class HaoyouTask(BaseTask):
    name = "好友"
    order = 10

    def run(self, stop_event: threading.Event):
        print(">>> 好友任务开始")
        time.sleep(3)
        print("重置窗口 聚焦窗口")
        get_window_size()
        # 1. 领取 & 赠送
        time.sleep(3)
        print("匹配haoyou图标 点击好友图标")
        click_coord(match_pics('tdjimages/haoyou.png'), do_click=True)
        time.sleep(3)
        print("匹配haoyou_lingqu图标 点击好友全部领取")
        click_coord(match_pics('tdjimages/haoyou_lingqu.png'), do_click=True)
        time.sleep(2)
        print("匹配haoyou_zengs图标 点击好友全部赠送")
        click_coord(match_pics('tdjimages/haoyou_zengs.png'), do_click=True)
        time.sleep(2)
        print("即将回到营地界面")
        # 2. 退回到营地（循环检测“返回”按钮）
        while not match_pics(template_path='tdjimages/qicheng.png'):
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 好友任务被中断")
                return
            print("匹配lilian_back图标 点击返回到营地界面")
            click_coord(match_pics('tdjimages/lilian_back.png'), do_click=True)
            time.sleep(2)
        print(">>> 好友任务结束 成功返回营地")