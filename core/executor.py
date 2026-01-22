#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
from typing import List

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
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=10)
        self._thread = None

    def is_running(self):
        return self._thread is not None and self._thread.is_alive()

    # ---------- 内部调度 ----------
    def _run_tasks(self, task_cls_list):
        for cls in task_cls_list:
            if self._stop_event.is_set():
                break
            inst = cls()
            inst.run(self._stop_event)
            time.sleep(1)   # 任务间留缓冲