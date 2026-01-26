#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import client_offset


# 每日免费一抽任务
class ChoukaTask(BaseTask):
    name = "抽卡"
    order = 30
    def run(self, stop_event: threading.Event):
        print(">>> 每日免费一抽任务开始")
        # 1. 每日免费一抽 抽卡任务
        time.sleep(3)
        off_chouka = client_offset()# 定义相对窗口坐标偏移量固定坐标
        time.sleep(2)
        print("匹配召唤图标")
        click_coord(match_pics(template_path='tdjimages/zhaohuan.png'),do_click=True)
        time.sleep(5)
        while not match_pics(template_path='tdjimages/chouka1.png'):
            click_coord(match_pics(template_path='tdjimages/zhaohuan.png'),do_click=True)
            time.sleep(3)
        time.sleep(1)
        print("匹配抽卡图标")
        click_coord(match_pics(template_path='tdjimages/chouka1.png'),do_click=True)
        time.sleep(1)
        click_coord(match_pics(template_path='tdjimages/chouka1.png'),do_click=True)
        time.sleep(3)
        while not match_pics(template_path='tdjimages/zhaohuan_queren.png'):
            #直到匹配到确认才跳出循环
            # click_coord([(760,600,1.0)],do_drag=True,drag_distance=390)
            click_coord([(off_chouka[0] + 433, off_chouka[1] + 430, 1.0)],do_drag=True,drag_distance=390)
            time.sleep(3)
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 手动停止抽卡任务")
                return
        time.sleep(5)
        print("匹配抽卡确认图标")
        click_coord(match_pics(template_path='tdjimages/zhaohuan_queren.png'),do_click=True)
        time.sleep(3)    
        #一直匹配到启程图标 才会退出循环
        while not match_pics(template_path='tdjimages/qicheng.png'):
            click_coord(match_pics(template_path='tdjimages/zhaohuan_queren.png'),do_click=True)
            time.sleep(3)
            click_coord(match_pics(template_path='tdjimages/chouka_back.png'),do_click=True)
            time.sleep(3)
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 手动停止抽卡任务")
                return
        print(">>> 每日抽卡任务完成 成功返回营地")
