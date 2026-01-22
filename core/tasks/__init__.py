#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 手工导入所有任务类，顺序即执行顺序

from .ceshi import CeshiTask
from .haoyou import HaoyouTask
from .tiandige import TiandigeTask
# from .chouka import ChoukaTask
# from .shanhez import ShanhezTask
# from .yiwen import YiwenTask
# from .lilian import LilianTask
# from .qiyu import QiyuTask
# from .huanjing import HuanjingTask

# 获取所有任务类
def get_all_tasks():
    # 想调整顺序就改这里
    return [
        ("好友", HaoyouTask),
        ("天地阁", TiandigeTask),
        # ("每日一抽", ChoukaTask),
        # ("山河志", ShanhezTask),
        # ("异闻", YiwenTask),
        # ("历练", LilianTask),
        # ("奇遇", QiyuTask),   
        ("测试", CeshiTask),
        # ("幻境竞技场", HuanjingTask),
    ]