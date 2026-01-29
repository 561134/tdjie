#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口

# 天地阁任务
class TdgeTask(BaseTask):
    name = "天地阁"
    order = 20
    def run(self, stop_event: threading.Event):
        print(">>> 天地阁任务开始")
        # 1. 点击闪电任务
        print("点击闪电图标任务")
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/tdge_shandian.png'),do_click=True)
        time.sleep(2)
        print("闪电任务完成")
        # 2. 好友加速任务
        time.sleep(2)
        print("开始好友加速任务 点击天地阁")
        click_coord(match_pics(template_path='tdjimages/tdge.png'),do_click=True)
        time.sleep(3)
        print("匹配动态图标")
        click_coord(match_pics(template_path='tdjimages/tdge_dongtai.png'),do_click=True)
        time.sleep(3)
        print("匹配一键加速图标")
        click_coord(match_pics(template_path='tdjimages/tdge_jiasu.png'),do_click=True)
        time.sleep(3)
        # 3. 领取天地阁任务奖励
        print("开始天地阁任务奖励领取")
        click_coord(match_pics(template_path='tdjimages/tdge_renwu.png'),do_click=True)
        time.sleep(3)
        # 一次性获取匹配所有领取图标结果 确保每个图标都被点击到
        matches_lingqu = match_pics(template_path="tdjimages/tdge_renwu_lingqu.png",threshold=0.7)
        time.sleep(2)
        if matches_lingqu:
            print(f"[INFO] 找到 {len(matches_lingqu)} 个领取图标，开始点击...")
            for i, match in enumerate(matches_lingqu):  
                click_coord([match], do_click=True, clicks=1)
                time.sleep(2)
                if match_pics(template_path='tdjimages/tdge_renwu_mark.png'):
                    click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
                    time.sleep(2)
                print(f"[INFO] 已领取第 {i+1} 个任务奖励")
            time.sleep(2)
        else:
            print("[INFO] 没有要领取任务奖励 下次再来")
        # 返回到上级界面 能匹配到远征图标 确保返回到远征界面
        while not match_pics(template_path='tdjimages/tdge_yuanz.png'):
            click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
            time.sleep(3)
        print("开始天地阁远征任务")
        # 4. 点击远征任务
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz.png'),do_click=True)
        time.sleep(3)
        if match_pics(template_path='tdjimages/tdge_yuanz_taofa_over.png'):
            print("领取上次讨伐奖励")
            click_coord(match_pics(template_path='tdjimages/tdge_yuanz_taofa_over.png'),do_click=True)#讨伐完成
            time.sleep(2)
            click_coord(match_pics(template_path='tdjimages/tdge_yuanz_taofa_gift.png'),do_click=True)#讨伐完成
            time.sleep(2)
            while not match_pics(template_path='tdjimages/tdge_yuanz.png'):
                click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
                time.sleep(3)
        print("匹配远征BOSS图标 出战图标")
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz.png'),do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_boss1.png'),do_click=True)
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_boss2.png'),do_click=True)
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_boss3.png'),do_click=True)
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_boss4.png'),do_click=True)
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_boss5.png'),do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz_chuzhan.png'),do_click=True)
        time.sleep(3)
        print("匹配远征推荐角色图标 至少需要3个推荐角色")
        # 一次性获取所有匹配结果
        matches_tuijian = match_pics(template_path="tdjimages/tdge_tuijian.png", threshold=0.7)
        time.sleep(1)
        if len(matches_tuijian) >= 3:# 确保至少有3个推荐角色图标
            click_coord(matches_tuijian, do_click=True, index=0, clicks=1)
            time.sleep(1)
            click_coord(matches_tuijian, do_click=True, index=1, clicks=1)
            time.sleep(1)
            click_coord(matches_tuijian, do_click=True, index=2, clicks=1)
            time.sleep(3)
            print("匹配远征出战2图标")
            click_coord(match_pics(template_path='tdjimages/tdge_yuanz_chuzhan2.png'),do_click=True)
            time.sleep(3)
            # 4.返回营地
            while not match_pics(template_path='tdjimages/qicheng.png'):
                print("匹配返回图标")
                click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
                time.sleep(3)
                if stop_event.is_set():# ★随时响应“停止”
                    print(">>> 手动停止天地阁任务")
                    return
            print(">>> 天地阁任务完成 成功返回营地界面")
        else:
            print(f"警告：只找到 {len(matches_tuijian)} 个推荐角色图标，不满足3个 即将返回营地界面")
            while not match_pics(template_path='tdjimages/qicheng.png'):
                print("匹配返回图标")
                click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
                time.sleep(3)
                if stop_event.is_set():# ★随时响应“停止”
                    print(">>> 手动停止天地阁任务")
                    return
            print(">>> 天地阁任务结束 成功返回营地界面")

