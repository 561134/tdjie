#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading
from ..base_task import BaseTask
from utils.image import match_pics, click_coord   # 统一入口


# 神龛任务
class ShenkanTask(BaseTask):
    name = "神龛"
    order = 80
    def run(self, stop_event: threading.Event):
        print(">>> 神龛任务开始")
        time.sleep(3)
        print(">>> 神龛任务完成")
