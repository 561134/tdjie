#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 手工导入所有任务类，顺序即执行顺序

from .ceshi import CeshiTask
from .haoyou import HaoyouTask
from .tdge import TdgeTask
from .chouka import ChoukaTask
from .lilian import LilianTask
from .yiwen import YiwenTask
from .qiyu import QiyuTask
from .shanhez import ShanhezTask
from .kaoyu import KaoyuTask
from .huanjing import HuanjingTask
# 下面是以后扩展功能
# from .shenkan import ShenkanTask

# 获取所有任务类
def get_all_tasks():
    # 想调整顺序就改这里
    return [
        ("好友", HaoyouTask),
        ("天地阁", TdgeTask),
        ("每日一抽", ChoukaTask),
        ("历练", LilianTask),
        ("山河志", ShanhezTask),
        ("异闻", YiwenTask),
        ("奇遇", QiyuTask),
        ("烤鱼", KaoyuTask),
        ("幻境竞技场", HuanjingTask),
        # ("神龛", ShenkanTask),
        ("测试", CeshiTask),
    ]