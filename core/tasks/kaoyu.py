#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口


# 领取烤鱼任务
class KaoyuTask(BaseTask):
    name = "烤鱼"
    order = 90
    def run(self, stop_event: threading.Event):
        print(">>> 领取烤鱼任务开始")
        time.sleep(3)
        print("点击领取烤鱼图标")
        click_coord(match_pics(template_path='tdjimages/kaoyu.png'),do_click=True)
        time.sleep(2)
        if match_pics(template_path='tdjimages/kaoyu_get.png'):
            print("匹配到烤鱼获取图标 点击固定坐标118 620")
            click_coord([(off_huanjing[0] + 118, off_huanjing[1] + 620, 1.0)],do_click=True,clicks=2)
            time.sleep(2)
        kaoyu_count = 0
        while not match_pics(template_path='tdjimages/qicheng.png'):
            print(">>> 未匹配到启程图标 继续等待")
            kaoyu_count += 1
            if kaoyu_count > 5:
                print(">>> 领取烤鱼任务超时10秒未匹配到启程图标")
                return
            time.sleep(3)
        print(">>> 领取烤鱼任务结束 当前营地界面")