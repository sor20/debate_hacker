#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
彩蛋测试脚本
模拟用户点击来增加履历，更接近真实使用场景
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QTimer

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入主程序类
from debate_hacker import DebateHacker

def simulate_user_clicks(window):
    """模拟用户点击来增加履历"""
    print("🎯 模拟用户点击来增加履历，目标：10+5+1")
    
    # 增加履历达到10+5+1
    # 策略：点击9次普通履历（+a），4次佳辩履历（+a,+b），1次全程履历（+a,+b,+c）
    # 总计：9+4+1=14次点击 → a=14, b=5, c=1？不，应该调整为：
    
    # 正确的组合：
    # - 点击5次普通履历：a+5, b+0, c+0
    # - 点击4次佳辩履历：a+4, b+4, c+0
    # - 点击1次全程履历：a+1, b+1, c+1
    # 总计：a=10, b=5, c=1
    
    print("\n1. 点击5次普通履历（+a）")
    for i in range(5):
        window.resume_module.addNormalResume('国际赛')
        print(f"   第{i+1}次普通履历点击，当前数据：{window.resume_module.resume_count_label.text()}")
    
    print("\n2. 点击4次佳辩履历（+a,+b）")
    for i in range(4):
        window.resume_module.addExcellentResume('国际赛')
        print(f"   第{i+1}次佳辩履历点击，当前数据：{window.resume_module.resume_count_label.text()}")
    
    print("\n3. 点击1次全程履历（+a,+b,+c） - 这应该触发彩蛋！")
    window.resume_module.addFullResume('国际赛')
    print(f"   全程履历点击后，当前数据：{window.resume_module.resume_count_label.text()}")

if __name__ == '__main__':
    # 启用高DPI支持
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    window = DebateHacker()
    window.show()
    
    # 使用定时器延迟执行点击模拟，确保界面完全初始化
    QTimer.singleShot(1000, lambda: simulate_user_clicks(window))
    
    sys.exit(app.exec_())
