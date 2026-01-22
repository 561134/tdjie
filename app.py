# app.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from core.executor import Executor
from core.tasks import get_all_tasks
from utils.window import get_window_size
from utils.image import match_pics, click_coord
import threading
import time
from utils.admin import begin, begin2
import traceback
import queue

executor = Executor()
log_q = queue.Queue()

# ---------- 全局变量先声明 ----------
root = None
vars_ = {}
btn_start = None
btn_launch = None          # 先置空
log_text = None
# ------------------------------------

# ---------- 日志 ----------
def log(msg):
    log_q.put(msg)

def poll_log():
    while not log_q.empty():
        log_text.insert(tk.END, log_q.get() + "\n")
        log_text.see(tk.END)
    root.after(200, poll_log)

# ---------- 启动 ----------
def launch_and_wait():
    # 现在可以安全访问 btn_launch 了
    btn_launch.config(state="disabled")
    try:
        try:
            get_window_size()
            log("[INFO] 游戏窗口已存在")
        except RuntimeError:
            log("[INFO] 未检测到窗口，准备启动")
            begin()
            time.sleep(8)
            while not match_pics("tdjimages/begingame.png"):
                log("等待启动器...")
                time.sleep(3)
            click_coord(match_pics("tdjimages/begingame.png"), do_click=True)
            time.sleep(20)
            get_window_size()
            begin2()

        for _ in range(30):
            if match_pics("tdjimages/qicheng.png"):
                log("[INFO] 游戏就绪！")
                btn_start.config(state="normal")
                return
            time.sleep(3)
        log("[ERROR] 超时未检测到启程")
    except Exception as e:
        traceback.print_exc()
        log(f"[ERROR] {e}")
    finally:
        btn_launch.config(state="normal")

# ---------- 开始任务 ----------
def start_tasks():
    selected = [cls for name, cls in get_all_tasks() if vars_[name].get()]
    if not selected:
        log("[WARN] 未选择任何任务")
        return
    log("[INFO] 开始执行...")
    executor.start_tasks(selected)

# ---------- GUI ----------
def run_gui():
    global root, vars_, btn_start, btn_launch, log_text
    root = tk.Tk()
    root.title("天地劫助手")
    root.geometry("720x420")
    root.resizable(True, True)

    # ---------- 左侧 ----------
    left = ttk.Frame(root)
    left.pack(side="left", fill="both", expand=True, padx=8, pady=5)

    task_frame = ttk.Labelframe(left, text="任务列表（默认不选）")
    task_frame.pack(fill="both", expand=True)
    COLS = 2# 每行 3 个任务（想 2 个就写 2）
    vars_ = {}
    for idx, (name, cls) in enumerate(get_all_tasks()):
        vars_[name] = tk.BooleanVar(value=False)
        cb = ttk.Checkbutton(task_frame, text=name, variable=vars_[name])
        # 网格布局：行号=idx//COLS，列号=idx%COLS
        cb.grid(row=idx//COLS, column=idx%COLS, sticky="w", padx=6, pady=2)
      
    # 计算最后一行的行号
    last_row = (len(list(get_all_tasks())) + COLS - 1) // COLS
    sel_bar = ttk.Frame(task_frame)
    sel_bar.grid(row=last_row, column=0, columnspan=COLS, sticky="ew", padx=6, pady=4)
    ttk.Button(sel_bar, text="全选", command=lambda: [v.set(True) for v in vars_.values()]).pack(side="left", padx=2)
    ttk.Button(sel_bar, text="取消全选", command=lambda: [v.set(False) for v in vars_.values()]).pack(side="left", padx=2)
    
    btn_bar = ttk.Frame(left)
    btn_bar.pack(fill="x", pady=6)
    style = ttk.Style()
    style.configure("TButton", width=8, font=("Microsoft YaHei", 9))

    # 关键：在这里真正创建 btn_launch
    btn_launch = ttk.Button(btn_bar, text="启动游戏", command=lambda: threading.Thread(target=launch_and_wait, daemon=True).start())
    btn_launch.pack(side="left", padx=4)

    btn_start = ttk.Button(btn_bar, text="开始任务", command=start_tasks)
    btn_start.pack(side="left", padx=4)
    ttk.Button(btn_bar, text="停止任务", command=executor.stop).pack(side="left", padx=4)

    # ---------- 右侧 ----------
    right = ttk.Labelframe(root, text="实时日志")
    right.pack(side="right", fill="both", expand=True, padx=8, pady=5)
    log_text = scrolledtext.ScrolledText(right, height=18, font=("Consolas", 10))
    log_text.pack(fill="both", expand=True, padx=4, pady=4)

    # 日志重定向
    import builtins
    orig_print = builtins.print
    builtins.print = lambda *a, **k: (log_q.put(" ".join(map(str, a))), orig_print(*a, **k))

    poll_log()
    root.mainloop()


if __name__ == "__main__":
    run_gui()