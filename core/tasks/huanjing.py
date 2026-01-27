#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
import datetime
from utils.window import client_offset


# 幻境任务
class HuanjingTask(BaseTask):
    name = "幻境"
    order = 100
    def run(self, stop_event: threading.Event):
        print(">>> 幻境任务开始 打5次幻境")
        time.sleep(3)
        off_huanjing = client_offset()# 定义相对窗口坐标偏移量
        time.sleep(1)
        # 1. 幻境任务
        current_time = datetime.datetime.now().time()
        weekday = datetime.datetime.now().weekday()
        # 如果是周日且晚上10点后则跳过该任务 周日10点-12点打不开幻境
        if weekday == 6 and current_time >= datetime.time(21, 45):
            print("周日且晚上21点45分 跳过幻境竞技场任务")
            while not match_pics(template_path='tdjimages/qicheng.png'):
                    click_coord(match_pics(template_path='tdjimages/hj_x.png'),do_click=True)
                    time.sleep(2)
                    click_coord(match_pics(template_path='tdjimages/hj_back.png'),do_click=True)
                    time.sleep(2)
            time.sleep(3)
            return
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/menu.png'),do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/huanjing.png'), do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/huanjing.png'), do_click=True)
        time.sleep(5)
        # 如果匹配2次后还能匹配到幻境入口说明不能参与幻境了 直接返回营地
        if match_pics(template_path='tdjimages/huanjing.png'):
            while match_pics(template_path='tdjimages/huanjing.png'):# 这里点一下启程图标来关闭菜单显示状态 就回到初始状态了
                click_coord(match_pics(template_path='tdjimages/qicheng.png'), do_click=True)
                time.sleep(3)
            print("周日且晚上21点45分 这个时间段不能参加幻境任务 结束任务")
            return
        # 检查是否成功进入下一界面
        time.sleep(2)
        if not match_pics(template_path='tdjimages/hj_x2.png'):
            print("幻境任务出现错误hj_x2 结束幻境任务 返回营地")
            while not match_pics(template_path='tdjimages/qicheng.png'):
                    click_coord(match_pics(template_path='tdjimages/hj_x.png'),do_click=True)
                    time.sleep(2)
                    click_coord(match_pics(template_path='tdjimages/hj_back.png'),do_click=True)
                    time.sleep(2)
                    if stop_event.is_set():# ★随时响应“停止”
                        return
            time.sleep(3)
            return
        # 2. 匹配2x pve 打5次幻境
        for i in range(5):
            time.sleep(2)
            print(f"第{i+1}次挑战2x玩家")
            click_coord(match_pics(template_path='tdjimages/hj_x2.png'),do_click=True)
            time.sleep(3)
            print("匹配2x玩家 自动战斗")
            click_coord(match_pics(template_path='tdjimages/hj_auto.png'),do_click=True)
            time.sleep(10)
            if match_pics(template_path='tdjimages/hj_wendie.png'):
                print("匹配到文牒不够 马上退到营地界面")
                while not match_pics(template_path='tdjimages/qicheng.png'):
                    click_coord(match_pics(template_path='tdjimages/hj_x.png'),do_click=True)
                    time.sleep(2)
                    click_coord(match_pics(template_path='tdjimages/hj_back.png'),do_click=True)
                    time.sleep(2)
                    if stop_event.is_set():# ★随时响应“停止”
                        return
                time.sleep(3)
                return
            chu_count = 0
            while not match_pics(template_path='tdjimages/hj_chuzhan.png'):
                time.sleep(3)
                chu_count += 1
                if chu_count > 5:
                    break
                if stop_event.is_set():# ★随时响应“停止”
                    return
        
            time.sleep(1)
            click_coord(match_pics(template_path='tdjimages/hj_chuzhan.png'),do_click=True)
            time.sleep(1)
            click_coord(match_pics(template_path='tdjimages/hj_chuzhan.png'),do_click=True)
            time.sleep(1)
            click_coord(match_pics(template_path='tdjimages/hj_tishi_01.png'),do_click=True)
            time.sleep(1)
            click_coord(match_pics(template_path='tdjimages/hj_tishi_sure.png'),do_click=True)
            time.sleep(1)
            click_coord(match_pics(template_path='tdjimages/hj_skipbattle.png'),do_click=True)
            time.sleep(3)
            click_coord(match_pics(template_path='tdjimages/hj_skipbattle.png'),do_click=True)
            time.sleep(3)
            click_coord(match_pics(template_path='tdjimages/hj_skipbattle.png'),do_click=True)
            time.sleep(3)
            click_coord(match_pics(template_path='tdjimages/hj_skipbattle.png'),do_click=True)
            time.sleep(6)
            count = 0
            # 匹配x2界面此次战斗结束，就可以进行下一场战斗
            while not match_pics(template_path='tdjimages/hj_x2.png'):
                # click_coord([(520,500,1.0)],do_click=True,clicks=2)# 点击空白位置 战斗结束
                click_coord([(off_huanjing[0] + 211, off_huanjing[1] + 333, 1.0)],do_click=True,clicks=2)
                time.sleep(3)
                click_coord(match_pics(template_path='tdjimages/hj_chuzhan.png'),do_click=True)
                click_coord(match_pics(template_path='tdjimages/hj_tishi_01.png'),do_click=True)
                click_coord(match_pics(template_path='tdjimages/hj_tishi_sure.png'),do_click=True)
                click_coord(match_pics(template_path='tdjimages/hj_skipbattle.png'),do_click=True)
                time.sleep(3)
                count += 1
                if count > 5:
                    print("count>5 超次数退出判断hj_x2")
                    break
                if stop_event.is_set():# ★随时响应“停止”
                    return

        time.sleep(5)
        while not match_pics(template_path='tdjimages/qicheng.png'):
            click_coord(match_pics(template_path='tdjimages/hj_x.png'),do_click=True)
            time.sleep(3)
            click_coord(match_pics(template_path='tdjimages/hj_back.png'),do_click=True)
            time.sleep(3)
            click_coord([(off_huanjing[0] + 211, off_huanjing[1] + 333, 1.0)],do_click=True,clicks=2)
            time.sleep(3)
            if stop_event.is_set():# ★随时响应“停止”
                return

        if match_pics(template_path='tdjimages/qicheng.png'):
            print("幻境任务做完 已经返回营地界面")
        




