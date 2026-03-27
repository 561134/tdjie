#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
import glob
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import client_offset


# 天地阁任务
class TdgeTask(BaseTask):
    name = "天地阁"
    order = 20
    def run(self, stop_event: threading.Event):
        print(">>> 天地阁任务开始")
        off_tdge = client_offset()
        # 1. 点击闪电任务
        print("点击闪电图标任务")
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/tdge_shandian.png'),do_click=True)
        time.sleep(2)
        print("闪电任务完成")
        # 2. 好友加速任务
        time.sleep(2)
        print("点击天地阁")
        click_coord(match_pics(template_path='tdjimages/tdge.png'),do_click=True)
        time.sleep(3)
        print("点击绳子标记 防止其它弹窗干扰")
        click_coord(match_pics(template_path='tdjimages/tdge_mark.png'),do_click=True,clicks=2)
        time.sleep(3)
        print("匹配动态图标")
        click_coord(match_pics(template_path='tdjimages/tdge_dongtai.png'),do_click=True)
        time.sleep(3)
        print("匹配一键加速图标")
        click_coord(match_pics(template_path='tdjimages/tdge_jiasu.png'),do_click=True)
        time.sleep(3)
        # 3. 领取天地阁任务奖励
        print("任务奖励领取")
        click_coord(match_pics(template_path='tdjimages/tdge_renwu.png'),do_click=True)
        time.sleep(3)
        # 一次性获取匹配所有领取图标结果 确保每个图标都被点击到
        matches_lingqu = match_pics(template_path="tdjimages/tdge_renwu_lingqu.png",threshold=0.7)
        if matches_lingqu:
            print(f"[INFO] 找到 {len(matches_lingqu)} 个领取图标，开始点击...")
            for i, match in enumerate(matches_lingqu):  
                click_coord([match], do_click=True, clicks=1)
                time.sleep(2)
                if match_pics(template_path='tdjimages/tdge_renwu_mark.png'):
                    click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
                    time.sleep(2)
                print(f"[INFO] 已领取第 {i+1} 个任务奖励")
        else:
            print("[INFO] 没有要领取任务奖励 下次再来")
        time.sleep(1)
        # 返回到上级远征界面
        while not match_pics(template_path='tdjimages/tdge_yuanz.png'):
            click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
            time.sleep(3)
        print("开始天地阁远征任务")
        # 3. 点击远征任务
        click_coord(match_pics(template_path='tdjimages/tdge_yuanz.png'),do_click=True)
        time.sleep(3)
        
        # 检查BOSS图标，只点击找到的第一个
        boss_icons = glob.glob('tdjimages/tdge_yuanz_boss*.png')
        boss_found = False
        for boss_icon in boss_icons:
            if match_pics(template_path=boss_icon):
                click_coord(match_pics(template_path=boss_icon), do_click=True)
                boss_found = True
                print(f"找到并点击BOSS图标: {boss_icon}")
                break
        
        if not boss_found:
            print("未找到任何BOSS图标")
        
        time.sleep(3)
        if match_pics(template_path='tdjimages/tdge_yuanz_chuzhan.png'):
            click_coord(match_pics(template_path='tdjimages/tdge_yuanz_chuzhan.png'),do_click=True)
            time.sleep(3)
            print("优先点击推荐角色图标")# 一次性获取所有匹配结果
            matches_tuijian = match_pics(template_path="tdjimages/tdge_tuijian.png", threshold=0.7)
            if matches_tuijian:# 有推荐就点推
                for i in range(len(matches_tuijian)):
                    click_coord(matches_tuijian, do_click=True, index=i, clicks=1)
                    time.sleep(1)
            time.sleep(1)
            print("防止推荐个数不够 再补充点击3个固定坐标")
            click_coord([(off_tdge[0] + 211, off_tdge[1] + 335, 1.0)],do_click=True)
            click_coord([(off_tdge[0] + 335, off_tdge[1] + 335, 1.0)],do_click=True)
            click_coord([(off_tdge[0] + 459, off_tdge[1] + 335, 1.0)],do_click=True)
            print("远征出战2图标")
            click_coord(match_pics(template_path='tdjimages/tdge_yuanz_chuzhan2.png'),do_click=True)
        else:
            print("没有匹配到远征出战图标 是打过了")
        time.sleep(3)
        # 4.返回启程界面
        while not match_pics(template_path='tdjimages/qicheng.png'):
            # 如果返回过程匹配到有上次讨伐奖励图标就领取
            if match_pics(template_path='tdjimages/tdge_yuanz_taofa_wan.png'):
                print("领取上次讨伐奖励")
                click_coord(match_pics(template_path='tdjimages/tdge_yuanz_taofa_wan.png'),do_click=True)#讨伐完成
                time.sleep(2)
                click_coord(match_pics(template_path='tdjimages/tdge_yuanz_taofa_gift.png'),do_click=True)#讨伐完成
                time.sleep(2)
            click_coord(match_pics(template_path='tdjimages/tdge_back.png'),do_click=True)
            time.sleep(3)
        print(">>> 天地阁任务完成 成功返回营地界面")
