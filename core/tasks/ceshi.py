#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import get_window_size
from utils.window import client_offset
import win32gui
# import pyautogui# 测试用
# pyautogui.moveTo(offceshi[0] + 746, offceshi[1] + 221)
# pyautogui.click()

class CeshiTask(BaseTask):
    name = "测试"
    order = 1000

    def run(self, stop_event: threading.Event):
        print(">>> 测试任务开始")
        time.sleep(3)
        get_window_size()
        print("重置窗口 聚焦窗口")
        time.sleep(1)
        hwnd = win32gui.FindWindow(None, "天地劫：幽城再临")
        client_rect = win32gui.GetClientRect(hwnd)   # (0,0,w,h)
        print("客户区尺寸：", client_rect[2], "x", client_rect[3])

        time.sleep(3)
        offceshi = client_offset()# 获取游戏客户区左上角在屏幕上的绝对坐标 (left, top)
        time.sleep(3)
        while True:# 循环测试某个功能
            # click_coord(match_pics('tdjimages/haoyou.png'), do_click=True)
            # click_coord([(offceshi[0] + 746, offceshi[1] + 221, 1.0)],do_click=True)
            # click_coord(match_pics('tdjimages/haoyou.png'), do_click=True)
            print("点击了相对窗口坐标：", offceshi[0], offceshi[1])
            
            time.sleep(10)
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 测试任务结束")
                return
            
