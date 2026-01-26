#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口
from utils.window import client_offset


# 奇遇任务
class QiyuTask(BaseTask):
    name = "奇遇"
    order = 60
    def run(self, stop_event: threading.Event):
        print(">>> 奇遇任务开始 需20点体力")
        time.sleep(3)
        off_qiyu = client_offset()# 定义相对窗口坐标偏移量
        time.sleep(2)
        print("点击启程图标")
        while not match_pics(template_path='tdjimages/qicheng.png'):
            click_coord(match_pics(template_path='tdjimages/hj_back.png'),do_click=True)
            click_coord(match_pics(template_path='tdjimages/hj_x.png'),do_click=True)
            time.sleep(3)
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 手动停止奇遇任务")
                return
        click_coord(match_pics(template_path='tdjimages/qicheng.png'),do_click=True)
        time.sleep(5)# 等待5秒 确保进入奇遇界面
        while not match_pics(template_path='tdjimages/qiyu.png'):
            click_coord(match_pics(template_path='tdjimages/qicheng.png'),do_click=True)
            time.sleep(3)
        print("点击奇遇图标")
        click_coord(match_pics(template_path='tdjimages/qiyu.png'),do_click=True)
        time.sleep(6)
        print("优先匹配奇遇-危图标 没有就打随机一个10体力任务")
        if match_pics(template_path='tdjimages/qiyu_wei.png'):
            print("点击奇遇-危图标")
            click_coord(match_pics(template_path='tdjimages/qiyu_wei.png'),do_click=True)
            time.sleep(5)
        elif match_pics(template_path='tdjimages/qiyu_10.png'):# 奇遇10体力任务
            print("此次打奇遇-10体力任务")
            click_coord(match_pics(template_path='tdjimages/qiyu_10.png'),do_click=True)
            time.sleep(5)
        else:
            print("没有匹配到任何 奇遇-危以及普通任务")
        time.sleep(3)
        print("点击奇遇-前往图标")
        click_coord(match_pics(template_path='tdjimages/qiyu_qianwang.png'),do_click=True)
        time.sleep(18)
        print("点击奇遇-出战图标")
        click_coord(match_pics(template_path='tdjimages/qiyu_chuzhan.png'),do_click=True)
        time.sleep(2)
        print("点击奇遇-提示图标")
        click_coord(match_pics(template_path='tdjimages/qiyu_tishi.png'),do_click=True)
        time.sleep(2)
        print("点击奇遇-确认图标")
        click_coord(match_pics(template_path='tdjimages/qiyu_queding.png'),do_click=True)
        time.sleep(3)
        print("点击奇遇-自动战斗图标")
        click_coord(match_pics(template_path='tdjimages/qiyu_zidong.png'),do_click=True)
        time.sleep(1)
        click_coord(match_pics(template_path='tdjimages/qiyu_zidong.png'),do_click=True)
        time.sleep(1)
        click_coord(match_pics(template_path='tdjimages/qiyu_zidong.png'),do_click=True)
        time.sleep(3)
        click_coord(match_pics(template_path='tdjimages/qiyu_zidong.png'),do_click=True)
        time.sleep(1)
        print("点击奇遇-跳过战斗图标")
        click_coord(match_pics(template_path='tdjimages/qiyu_tiaoguo.png'),do_click=True)
        time.sleep(1)
        click_coord(match_pics(template_path='tdjimages/qiyu_tiaoguo.png'),do_click=True)
        time.sleep(1)
        click_coord(match_pics(template_path='tdjimages/qiyu_tiaoguo.png'),do_click=True)
        time.sleep(1)
        click_coord(match_pics(template_path='tdjimages/qiyu_tiaoguo.png'),do_click=True)
        time.sleep(2)
        click_coord(match_pics(template_path='tdjimages/qiyu_tiaoguo.png'),do_click=True)
        time.sleep(12)
        qiyu_count = 0# 记录奇遇次数 达到上限就退出任务
        while not match_pics(template_path='tdjimages/zhaying.png'):
            click_coord(match_pics(template_path='tdjimages/hj_back.png'),do_click=True)
            click_coord(match_pics(template_path='tdjimages/hj_x.png'),do_click=True)
            print("点击空白固定图标")
            click_coord([(off_qiyu[0] + 100, off_qiyu[1] + 400, 1.0)],do_click=True)
            click_coord([(off_qiyu[0] + 100, off_qiyu[1] + 400, 1.0)],do_click=True)
            time.sleep(5)
            qiyu_count += 1
            if qiyu_count > 5:
                print("qiyu_count次数超过5次 停止循环匹配扎营图标")
                break
        time.sleep(3)
        while not match_pics(template_path='tdjimages/qicheng.png'):
            print("点击扎营图标 回营地界面")
            click_coord(match_pics(template_path='tdjimages/zhaying.png'),do_click=True)
            click_coord(match_pics(template_path='tdjimages/hj_x.png'),do_click=True)
            click_coord(match_pics(template_path='tdjimages/hj_back.png'),do_click=True)
            time.sleep(5)
            if stop_event.is_set():# ★随时响应“停止”
                print(">>> 手动停止奇遇任务")
                return
        time.sleep(3)
        if match_pics(template_path='tdjimages/qicheng.png'):
            print(">>> 奇遇任务结束 成功返回营地")

