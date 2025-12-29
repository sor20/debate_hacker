#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 DebateHacker 类的彩蛋功能
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 直接导入 DebateHacker 类
from debate_hacker import DebateHacker

def test_debate_hacker_easter_egg():
    """测试 DebateHacker 类的彩蛋功能"""
    print("🎯 开始测试 DebateHacker 类的彩蛋功能")
    
    # 创建应用程序实例
    app = QApplication(sys.argv)
    
    # 创建 DebateHacker 实例
    print("📦 创建 DebateHacker 实例...")
    window = DebateHacker()
    
    # 模拟用户点击增加履历
    print("\n🧪 开始模拟用户点击：")
    
    # 点击5次普通履历（+a）
    print("1. 点击5次普通履历（+a）")
    for i in range(5):
        window.resume_module.addNormalResume('国际赛')
    
    # 点击4次佳辩履历（+a,+b）
    print("2. 点击4次佳辩履历（+a,+b）")
    for i in range(4):
        window.resume_module.addExcellentResume('国际赛')
    
    # 点击1次全程履历（+a,+b,+c）
    print("3. 点击1次全程履历（+a,+b,+c）")
    window.resume_module.addFullResume('国际赛')
    
    # 开始事件循环
    print("\n🔄 进入事件循环，等待彩蛋触发...")
    sys.exit(app.exec_())

if __name__ == '__main__':
    test_debate_hacker_easter_egg()
