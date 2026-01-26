#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
import datetime


# 异闻任务 灵脉+创命 print("异闻扫荡 创命3次 灵脉3次 需要体力150点")
class YiwenTask(BaseTask):
    name = "异闻"
    order = 50
    def run(self, stop_event: threading.Event):
        print(">>> 异闻任务开始 异闻扫荡 创命3次 灵脉3次 体力需150点")
        time.sleep(3)
        # 1. 异闻--灵脉副本
        print("点击营地菜单图标")
        click_coord(match_pics(template_path='tdjimages/menu.png'),do_click=True)
        time.sleep(3)
        print("点击异闻图标")
        click_coord(match_pics(template_path='tdjimages/yiwen.png'),do_click=True)
        time.sleep(3)
        print("异闻-灵脉副本 扫荡3次")
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/yiw_lingmai.png'),do_click=True)
        time.sleep(3)
        # 获取当前星期几 0=周一 6=周日 这样设置是每日打不同的灵脉
        today = datetime.datetime.today().weekday()
        if today == 0:
            choose_lingmai_day="tdjimages/yiw_lingm_yan.png"  
        if today == 1:
            choose_lingmai_day="tdjimages/yiw_lingm_bing.png" 
        if today == 2:
            choose_lingmai_day="tdjimages/yiw_lingm_lei.png"
        if today == 3:
            choose_lingmai_day="tdjimages/yiw_lingm_guang.png"
        if today == 4:
            choose_lingmai_day="tdjimages/yiw_lingm_an.png"
        if today == 5:
            choose_lingmai_day="tdjimages/yiw_lingm_you.png"
        if today == 6:
            choose_lingmai_day="tdjimages/yiw_lingm_yan.png"
        # 点击灵脉
        time.sleep(3)
        print("今天打{}灵脉...".format(choose_lingmai_day))
        click_coord(match_pics(template_path=choose_lingmai_day),do_click=True)
        time.sleep(2)#这里点击就会扫荡1次
        click_coord(match_pics(template_path='tdjimages/lingmai_saodang.png'),do_click=True)
        time.sleep(1)# 扫荡1次
        click_coord(match_pics(template_path='tdjimages/yiw_saodang_again.png'),do_click=True)
        time.sleep(1)# 扫荡1次
        click_coord(match_pics(template_path='tdjimages/yiw_saodang_again.png'),do_click=True)
        time.sleep(3)
        while not match_pics(template_path='tdjimages/yiw_lingmai.png'):
            click_coord(match_pics(template_path='tdjimages/yiw_back.png'),do_click=True)
            time.sleep(3)
        print("异闻-灵脉副本 结束")

        # 2. 异闻--创命副本 直到匹配到灵脉入口
        print("开始异闻-创命副本 扫荡3次")
        click_coord(match_pics(template_path='tdjimages/yiw_chuangm.png'),do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/yiw_saodang.png'),do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/yiw_saodang_again.png'),do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/yiw_saodang_again.png'),do_click=True)
        time.sleep(3)
        print("异闻-创命副本 结束")

        print("即将返回营地界面")#一直匹配到启程图标 才会退出循环
        while not match_pics(template_path='tdjimages/qicheng.png'):
            click_coord(match_pics(template_path='tdjimages/yiwen_back.png'),do_click=True)
            time.sleep(3)# 点击返回
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 手动停止异闻任务")
                return
        print(">>> 异闻任务结束 成功返回营地")
        
