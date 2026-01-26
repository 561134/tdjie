#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import client_offset

# 山河志跑片任务
class ShanhezTask(BaseTask):
    name = "山河志"
    order = 70
    def run(self, stop_event: threading.Event):
        print(">>> 山河志跑片任务开始")
        time.sleep(3)
        off_shanhez = client_offset()# 定义相对窗口坐标偏移量
        print("匹配山河志图标")
        click_coord(match_pics(template_path='tdjimages/shanhez.png'),do_click=True)
        time.sleep(3)
        print("领取山河志上次奖励")
        while match_pics(template_path='tdjimages/shanhe_lingqu.png'):
            click_coord(match_pics(template_path='tdjimages/shanhe_lingqu.png'),do_click=True)
            time.sleep(2)
        time.sleep(2)
        print("点击空白位置 取消领取界面")# 点击空白位置 取消领取界面
        # click_coord([(330,800,1.0)],do_click=True)
        click_coord([(off_shanhez[0] + 23, off_shanhez[1] + 606, 1.0)],do_click=True)
        print("领取山河志奖励2")# 领取奖励2
        time.sleep(2)
        while match_pics(template_path='tdjimages/shanhe_lingqu2.png'):
            click_coord(match_pics(template_path='tdjimages/shanhe_lingqu2.png'),do_click=True)
            time.sleep(2)
        time.sleep(2)
        print("点击空白位置 取消领取界面")# 点击空白位置 取消领取界面
        # click_coord([(330,800,1.0)],do_click=True)
        click_coord([(off_shanhez[0] + 23, off_shanhez[1] + 606, 1.0)],do_click=True)
        time.sleep(2)
        print("开始做432跑片任务")
        shanhe_list = ['tdjimages/shanh_bianj.png','tdjimages/shanh_saiwai.png','tdjimages/shanh_tianfu.png','tdjimages/shanh_xixia.png']
        for i in shanhe_list:
            print("匹配到图标: ",i)
            click_coord(match_pics(template_path=i),do_click=True)
            time.sleep(2)
            print("匹配到委托图标")
            click_coord(match_pics(template_path='tdjimages/shanh_weituo.png'),do_click=True)
            time.sleep(2)
            print("匹配到派遣图标")
            click_coord(match_pics(template_path='tdjimages/shanh_paiqian.png'),do_click=True)
            time.sleep(3)
        time.sleep(3)
        while not match_pics(template_path='tdjimages/qicheng.png'):
            print("未匹配到启程图标 点击山河志返回图标")
            click_coord(match_pics(template_path='tdjimages/shanhe_back.png'),do_click=True)
            time.sleep(3)
        
        print("山河志跑片任务完成 成功回到营地界面")


