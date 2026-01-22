#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CV 相关工具
"""
import cv2
import numpy as np
import pyautogui


# 匹配一个或多个目标 返回列表 元素是元组 坐标点
def match_pics(template_path, threshold=0.8, method=cv2.TM_CCOEFF_NORMED, 
               grayscale=True, nms_threshold=0.5, draw=False):
    """
    匹配屏幕中所有符合阈值的目标并返回排序后的坐标列表
    :param template_path: 模板图像路径
    :param threshold: 匹配阈值（0-1）
    :param method: OpenCV模板匹配方法
    :param grayscale: 是否使用灰度匹配
    :param nms_threshold: 非极大值抑制阈值（0-1）控制目标去重强度（0.3-0.6为宜）
    :param draw: 是否绘制所有匹配区域
    :return: 排序后的匹配列表[(中心x, 中心y, 匹配值), ...]
    """
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
    screenshot_color = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # 读取模板
    template = cv2.imread(template_path)
    if template is None:
        raise ValueError("无法加载模板图像")
    
    # 灰度处理
    if grayscale:
        src_img = cv2.cvtColor(screenshot_color, cv2.COLOR_BGR2GRAY)
        tmp_img = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    else:
        src_img = screenshot_color
        tmp_img = template
    
    # 执行模板匹配
    res = cv2.matchTemplate(src_img, tmp_img, method)
    res_h, res_w = res.shape

    # 根据匹配方法确定有效值范围
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        compare = np.less_equal if method == cv2.TM_SQDIFF else np.greater_equal
        valid_res = 1 - res if method == cv2.TM_SQDIFF_NORMED else res
    else:
        compare = np.greater_equal
        valid_res = res

    # 获取所有候选位置
    loc = np.where(compare(res, threshold))
    locations = list(zip(*loc[::-1]))  # 转换为(x,y)坐标列表
    if not locations:
        return []

    # 获取匹配值并组合数据
    h, w = tmp_img.shape[:2]
    matches = []
    for pt in locations:
        x, y = pt
        if x + w > res_w or y + h > res_h:  # 过滤边缘越界结果
            continue
        match_val = valid_res[y, x]  # 注意OpenCV结果的维度顺序是(height, width)
        matches.append((x, y, w, h, match_val))

    # 非极大值抑制（NMS）
    def nms(boxes, scores, threshold):
        if len(boxes) == 0:
            return []
        boxes = np.array(boxes)
        scores = np.array(scores)

        x1 = boxes[:,0]
        y1 = boxes[:,1]
        x2 = x1 + boxes[:,2]
        y2 = y1 + boxes[:,3]

        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        order = scores.argsort()[::-1]

        keep = []
        while order.size > 0:
            i = order[0]
            keep.append(i)
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])

            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            ovr = inter / (areas[i] + areas[order[1:]] - inter)

            inds = np.where(ovr <= threshold)[0]
            order = order[inds + 1]

        return keep

    # 执行NMS
    boxes = [(x, y, w, h) for (x, y, w, h, _) in matches]
    scores = [val for (_, _, _, _, val) in matches]
    keep_indices = nms(boxes, scores, nms_threshold)
    final_matches = [matches[i] for i in keep_indices]

    # 按匹配值排序（从高到低）
    final_matches.sort(key=lambda x: x[4], reverse=(method not in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]))

    # 转换为中心坐标并收集结果
    results = []
    for (x, y, w, h, val) in final_matches:
        center_x = x + w // 2
        center_y = y + h // 2
        results.append((center_x, center_y, float(val)))

    # 绘制所有匹配区域
    if draw:
        for (x, y, w, h, _) in final_matches:
            cv2.rectangle(screenshot_color, 
                         (x, y), (x + w, y + h),
                         (0, 255, 0) if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] else (0, 0, 255),
                         2)
        cv2.imshow('Multi-Match Results', screenshot_color)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # print("result:",results)
    return results


def click_coord(matches, index=0, do_click=False, clicks=1, interval=1, do_drag=False, do_dragTo=False, dragTo_coord=None, **kwargs):
    """
    对指定序号的匹配目标执行操作
    :param matches: find_all_matches返回的匹配列表
    :param index: 要操作的目标序号（从0开始）
    :param do_click: 是否点击
    :param do_drag: 是否拖动
    :param do_dragTo: 是否拖动到指定坐标（新增参数）
    :param dragTo_coord: 目标坐标元组 (x, y)（新增参数）
    :param kwargs: 传递给perform_actions的参数
    """
    if not matches or index >= len(matches):
        print(f"无效的目标序号：{index}（共找到{len(matches)}个目标）")
        return
    
    # 校验拖动目标坐标参数
    if do_dragTo:
        if not dragTo_coord or len(dragTo_coord) != 2:
            raise ValueError("使用do_dragTo时必须提供有效的dragTo_coord参数，格式：(x, y)")
    
    target = matches[index]
    print(f"操作目标[{index}] 坐标：({target[0]}, {target[1]}) 匹配值：{target[2]:.3f}")
    clicks_action((target[0], target[1]), do_click=do_click, clicks=clicks, interval=interval,
                  do_drag=do_drag, do_dragTo=do_dragTo, dragTo_coord=dragTo_coord, **kwargs)


# clicks_action
def clicks_action(center, do_click=False, do_drag=False, do_dragTo=False, drag_distance=100, dragTo_coord=None, 
                   button='left', clicks=1, interval=0.5, drag_duration=0.5, click_duration=0.5):
    """
    执行鼠标操作
    :param center: 中心坐标 (x, y)
    :param do_click: 是否执行点击
    :param do_drag: 是否执行拖动
    :param drag_distance: 拖动距离（像素）
    :param button: 鼠标按钮
    :param drag_duration: 拖动持续时间（秒）
    :param click_duration: 点击后暂停时间（秒）
    :param do_dragTo: 是否拖动到指定坐标（新增）
    :param dragTo_coord: 目标坐标 (x, y)（新增）
    """
    if not center:
        return   
    x, y = center 
    if do_click:
        pyautogui.moveTo(x, y, duration=click_duration)
        pyautogui.click(button=button,clicks=clicks, interval=interval)
    if do_drag:
        pyautogui.moveTo(x, y, duration=click_duration)
        pyautogui.drag(0, -drag_distance, duration=drag_duration, button=button)
    # 拖动到指定坐标（新增逻辑）
    if do_dragTo and dragTo_coord:
        target_x, target_y = dragTo_coord
        pyautogui.moveTo(x, y, duration=click_duration)
        pyautogui.dragTo(target_x, target_y, duration=drag_duration, button=button)

