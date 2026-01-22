#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ctypes
import sys
import subprocess
import os
from pathlib import Path
import time
from utils.image import match_pics, click_coord
from utils.window import client_offset# 用于直接传递相对游戏窗口的坐标点击 （图片不好匹配直接传坐标实现）
# 先声明高 DPI 感知，后面启动的游戏会继承
ctypes.windll.user32.SetProcessDPIAware()


# 天地劫手游客户端路径
CONFIG_FILE = "tdjgame_path.txt"

# 判断是否管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
# 提升管理员权限
def elevate():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1
    )
    sys.exit()
# 加载游戏路径
def load_game_path():
    cfg = Path(CONFIG_FILE)
    if not cfg.exists():
        raise FileNotFoundError(f"请在同目录创建 {CONFIG_FILE} 并写入游戏路径")
    path = cfg.read_text(encoding="utf8").strip()
    return path
# 启动游戏
def launch_game():
    if not is_admin():
        elevate()          # 已确保管理员
    game_path = load_game_path()
    # print("管理员模式，启动路径:", game_path)

    # 等价于双击：正常显示 + 同一工作目录
    subprocess.Popen(
        [game_path],
        cwd=os.path.dirname(game_path),   # 关键：工作目录=exe所在目录
        creationflags=subprocess.CREATE_NEW_CONSOLE  # 让启动器独立控制台
    )
    # print("子进程已创建")

# 启动游戏界面
def begin():
    time.sleep(3)
    # 如果未提权则自我提升
    if not is_admin():
        print("检测到无管理员权限，正在请求提权...")
        elevate()
    else:
        print("当前已拥有管理员权限 启动游戏")
        launch_game()

# 启动游戏界面2
def begin2():
    time.sleep(5)
    while not match_pics(template_path='tdjimages/begin_x.png'):
        time.sleep(5)
    
    time.sleep(3)
    click_coord(match_pics(template_path='tdjimages/begin_x.png'),do_click=True)

    off = client_offset()# 获取游戏客户区左上角在屏幕上的绝对坐标 (left, top)
    # 等待开始画面出现
    time.sleep(5)
    click_coord(match_pics(template_path='tdjimages/begin_x.png'),do_click=True)
    time.sleep(3)
    # 换区匹配先不用
    while not match_pics(template_path='tdjimages/huanqu.png',threshold=0.7):
        click_coord(match_pics(template_path='tdjimages/begin_x.png'),do_click=True)
        time.sleep(3)# 匹配到启程图片 已经进入到游戏界面
    click_coord([(off[0] + 600, off[1] + 333, 1.0)],do_click=True)#传入相对游戏窗口中心点的坐标 进入游戏
    # click_coord([(800,500,1.0)],do_click=True)#匹配到换区点击窗口中心位置进入游戏
    time.sleep(15)
    while not match_pics(template_path='tdjimages/qicheng.png'):
        click_coord(match_pics(template_path='tdjimages/qiandao.png'),do_click=True)
        time.sleep(3)
        click_coord([(off[0] + 60, off[1] + 558, 1.0)],do_click=True)#点击空白关闭（每个版本分享弹窗提示）
        # click_coord([(380,770,1.0)],do_click=True)#点击空白关闭（每个版本分享弹窗提示）
        time.sleep(3)

    time.sleep(3)
    if match_pics(template_path='tdjimages/qicheng.png'):
        print("进入到游戏营地界面")


