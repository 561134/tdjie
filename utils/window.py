#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import win32gui
import time

# 天地劫手游窗口句柄标题
WINDOW_TITLE = "天地劫：幽城再临"
# 获取游戏窗口大小
def get_window_size():
    """
    返回 (x, y, width, height)
    并把窗口强制 1280x720 置顶
    """
    hwnd = win32gui.FindWindow(None, WINDOW_TITLE)
    if not hwnd:
        raise RuntimeError("未找到游戏窗口")
    rect = win32gui.GetWindowRect(hwnd)
    x, y, x2, y2 = rect
    win32gui.MoveWindow(hwnd, 300, 160, 1280, 720, False)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.5)
    return x, y, x2 - x, y2 - y

# 用于直接传递相对游戏窗口的坐标点击 （图片不好匹配直接传坐标实现）
def client_offset():
    """
    返回游戏客户区左上角在屏幕上的绝对坐标 (left, top)
    用于把“相对 720p 客户区的坐标”转成屏幕绝对坐标
    """
    hwnd = win32gui.FindWindow(None, WINDOW_TITLE)
    if not hwnd:
        raise RuntimeError("未找到游戏窗口")
    left, top = win32gui.ClientToScreen(hwnd, (0, 0))
    return left, top