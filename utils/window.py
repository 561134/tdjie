#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import win32gui
import win32con
import time
import pyautogui


# 天地劫手游窗口句柄标题
WINDOW_TITLE = "天地劫：幽城再临"

# 获取窗口句柄并确保窗口状态正常
def get_window_handle():
    """
    获取游戏窗口句柄并确保窗口状态正常 包括：查找窗口、恢复窗口、显示窗口、激活窗口
    返回窗口句柄
    """
    hwnd = win32gui.FindWindow(None, WINDOW_TITLE)
    if not hwnd:
        raise RuntimeError("未找到目标窗口")  
    # 直接恢复窗口（无论是否最小化）
    # print("[INFO] 确保窗口状态正常...")
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    time.sleep(1)
    # 直接显示窗口（确保可见）
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    time.sleep(1)
    # 激活窗口
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    return hwnd

# 获取游戏窗口大小
def get_window_size():
    """
    返回 (x, y, width, height) 并把窗口强制 1280x720 置顶
    """
    hwnd = get_window_handle()
    rect = win32gui.GetWindowRect(hwnd)
    x, y, x2, y2 = rect
    win32gui.MoveWindow(hwnd, 300, 160, 1280, 720, False)
    time.sleep(1)
    return x, y, x2 - x, y2 - y

# 用于直接传递相对游戏窗口的坐标点击 （图片不好匹配直接传坐标实现）
def client_offset():
    """
    返回游戏客户区左上角在屏幕上的绝对坐标 (left, top)
    用于把“相对 720p 客户区的坐标”转成屏幕绝对坐标
    """
    hwnd = get_window_handle()
    left, top = win32gui.ClientToScreen(hwnd, (0, 0))
    return left, top

# 点击游戏窗口中心（确保获得交互焦点）
def click_center():
    """
    点击游戏窗口中心（使用 client_offset 处理缩放）
    """
    off_windows = client_offset()  # 获取实际客户区坐标
    center_x = off_windows[0] + 1280 // 2   # 客户区左边界 + 宽度/2
    center_y = off_windows[1] + 250         # 客户区上边界 + 高度/2
    for i in range(3):
        pyautogui.click(center_x, center_y)
    print(f"[INFO] 点击窗口中心坐标 3次: ({center_x}, {center_y})")
