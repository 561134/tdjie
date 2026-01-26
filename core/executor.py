#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
from typing import List
from utils.window import get_window_size, click_center


# 任务执行器
class Executor:
    def __init__(self):
        self._thread: threading.Thread | None = None
        self._stop_event = threading.Event()

    # ---------- 对外接口 ----------
    def start_tasks(self, task_cls_list: List[type]):
        if self.is_running():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run_tasks, args=(task_cls_list,), daemon=True
        )
        self._thread.start()

    def stop(self):
        """
        非阻塞停止任务
        设置停止事件后立即返回，不等待线程结束
        """
        print("[INFO] 正在停止任务...")
        self._stop_event.set()
        # 不等待线程结束，避免阻塞GUI
        # 线程会在适当的时机自行结束
        print("[INFO] 停止指令已发送，任务将在适当时机停止")

    def is_running(self):
        """
        检查任务是否正在运行
        如果线程存在且处于活动状态，则返回True
        否则返回False，并清理_thread属性
        """
        if self._thread is None:
            return False
        if not self._thread.is_alive():
            # 线程已结束，清理_thread属性
            self._thread = None
            return False
        return True

    # ---------- 内部调度 ----------
    def _run_tasks(self, task_cls_list):
        """
        执行任务列表
        定期检查stop_event，确保能够及时响应停止指令
        """
        try:
            # 激活游戏窗口
            # print("[INFO] 获取窗口")
            get_window_size()
            time.sleep(1)
            click_center()
        except Exception as e:
            print(f"[WARNING] 校正窗口失败: {e}")
        
        for cls in task_cls_list:
            inst = cls()
            inst.run(self._stop_event)
            time.sleep(1)   # 任务间留缓冲
        
        # 任务执行完成，清理_thread属性
        print("[INFO] 任务执行完成")
        self._thread = None