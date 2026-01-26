#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口


# 领取烤鱼任务
class KaoyuTask(BaseTask):
    name = "烤鱼"
    order = 90
    def run(self, stop_event: threading.Event):
        print(">>> 领取烤鱼任务开始")
        time.sleep(3)
        print(">>> 领取烤鱼任务结束")
