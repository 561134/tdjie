#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import threading

# 任务基类
class BaseTask(ABC):
    name: str = ""          # GUI 显示的中文名
    order: int = 999        # 执行顺序，升序

    @abstractmethod
    def run(self, stop_event: threading.Event):
        """具体任务实现，需定期检测 stop_event.is_set() 以响应取消"""
        raise NotImplementedError