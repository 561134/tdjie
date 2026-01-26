#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口


# 历练奖励领取任务 里面有体力点
class LilianTask(BaseTask):
    name = "历练"
    order = 40
    def run(self, stop_event: threading.Event):
        print(">>> 历练任务开始")
        time.sleep(3)
        print("匹配历练图标")
        click_coord(match_pics(template_path='tdjimages/lilian.png'),do_click=True)
        time.sleep(3)
        print("匹配一键领取图标")
        click_coord(match_pics(template_path='tdjimages/lilian_lingqu.png'),do_click=True)
        time.sleep(3)
        #一直匹配到启程图标 才会退出循环
        while not match_pics(template_path='tdjimages/qicheng.png'):
            click_coord(match_pics(template_path='tdjimages/lilian_back.png'),do_click=True)
            time.sleep(3)# 点击返回
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 手动停止历练任务")
                return
        print(">>> 历练任务完成 成功返回营地")
