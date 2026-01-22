#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import get_window_size

# 天地阁任务
class TiandigeTask(BaseTask):
    name = "天地阁"
    order = 20
    def run(self, stop_event: threading.Event):
        print(">>> 天地阁任务开始")
        time.sleep(3)
        if stop_event.is_set():# ★随时响应“停止”
            return
        print("重置窗口 聚焦窗口")
        get_window_size()
        # 1. 点击闪电任务
        time.sleep(2)
        print("点击闪电图标任务")
        click_coord(match_pics(template_path='tdjimages/tdge_shandian.png'),do_click=True)
        time.sleep(2)
        print("天地阁闪电任务结束")
        # 2. 好友加速任务
        time.sleep(2)
        print("开始好友加速任务 点击天地阁")
        click_coord(match_pics(template_path='tdjimages/tdge.png'),do_click=True)
        time.sleep(3)
        print("匹配tdge_dongtai图标 点击天地阁动态")
        click_coord(match_pics(template_path='tdjimages/tdge_dongtai.png'),do_click=True)
        time.sleep(3)
        print("匹配tdge_jiasu图标 点击天地阁一键加速")
        click_coord(match_pics(template_path='tdjimages/tdge_jiasu.png'),do_click=True)
        time.sleep(3)
        print("一键加速结束 远征任务开始 点击远征")
        # 3. 点击远征任务
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz.png'),do_click=True)
        time.sleep(3)
        print("匹配tdge_yuanz4图标 点击周四BOSS")
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz4.png'),do_click=True)
        time.sleep(3)
        print("匹配tdge_yuanz_chuzhan图标 点击出战")
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_chuzhan.png'),do_click=True)
        time.sleep(3)
        print("匹配tdge_tuijian图标 点击远征推荐角色 3个")
        # 一次性获取所有匹配结果
        matches = match_pics(template_path="tdjimages/tdge_tuijian.png", threshold=0.7)
        if len(matches) >= 3:
            # 按顺序点击
            click_coord(matches, do_click=True, index=0, clicks=1)
            time.sleep(1)
            click_coord(matches, do_click=True, index=1, clicks=1)
            time.sleep(1)
            click_coord(matches, do_click=True, index=2, clicks=1)
        else:
            print(f"警告：只找到 {len(matches)} 个推荐角色图标，需要 3 个")
        time.sleep(3)
        print("匹配tdge_yuanz_chuzhan2图标 点击出战")
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_chuzhan2.png'),do_click=True)
        time.sleep(3)
        print("远征结束")

        # 4.全部做完 返回营地
        while not match_pics(template_path='tdjimages/qicheng.png'):
            time.sleep(1)
            print("匹配tdge_back图标 点击返回到营地界面")
            click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
            time.sleep(3)
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 天地阁任务被中断")
                return
        print(">>> 天地阁任务结束 回到营地界面")

