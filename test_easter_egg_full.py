#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整的彩蛋测试脚本
模拟用户操作并测试完整的彩蛋触发流程
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入所有需要的模块
from modules.resume_module import ResumeModule
from modules.easter_egg_module import EasterEggDialog

# 创建一个简单的测试类来模拟DebateHacker的行为
class EasterEggTester:
    def __init__(self):
        self.easter_egg_triggered = False
        self.resume_module = ResumeModule()
        
        # 连接信号
        self.resume_module.resume_changed.connect(self.onResumeChanged)
        
        print("🎯 彩蛋测试环境准备完成")
        print("🔗 resume_changed 信号已连接到 onResumeChanged")
    
    def onResumeChanged(self):
        """处理履历更新"""
        print(f"\n🔍 onResumeChanged 被调用")
        print(f"🔍 easter_egg_triggered: {self.easter_egg_triggered}")
        
        if not self.easter_egg_triggered:
            resume_data = self.resume_module.getResumeData()
            print(f"🔍 当前履历数据: {resume_data}")
            
            total_a = sum(resume_data[category]['a'] for category in resume_data)
            total_b = sum(resume_data[category]['b'] for category in resume_data)
            total_c = sum(resume_data[category]['c'] for category in resume_data)
            
            print(f"🔍 计算结果：total_a={total_a}, total_b={total_b}, total_c={total_c}")
            print(f"🔍 触发条件：{total_a == 10} && {total_b == 5} && {total_c == 1}")
            
            if total_a == 10 and total_b == 5 and total_c == 1:
                print("🎉 触发条件满足，准备显示彩蛋")
                self.easter_egg_triggered = True
                self.triggerEasterEgg()
            elif total_a >= 10 and total_b >= 5 and total_c >= 1:
                print(f"⚠️  已超过彩蛋触发条件：{total_a}/{total_b}/{total_c}，请尝试调整到10/5/1")
    
    def triggerEasterEgg(self):
        """触发彩蛋"""
        print("🎊 触发彩蛋！")
        # 创建彩蛋弹窗
        dialog = EasterEggDialog()
        
        # 设置定时器自动关闭弹窗
        QTimer.singleShot(2000, dialog.accept)
        
        # 显示弹窗
        result = dialog.exec_()
        print(f"🎊 彩蛋弹窗关闭，结果：{result}")
        
        # 退出应用程序
        QTimer.singleShot(1000, QApplication.instance().quit)

def test_easter_egg_full():
    """完整的彩蛋测试"""
    print("🎯 开始完整的彩蛋测试")
    
    # 创建应用程序实例
    app = QApplication(sys.argv)
    
    # 创建测试器
    tester = EasterEggTester()
    
    # 模拟用户点击增加履历
    print("\n🧪 开始模拟用户点击：")
    
    # 点击5次普通履历（+a）
    print("1. 点击5次普通履历（+a）")
    for i in range(5):
        tester.resume_module.addNormalResume('国际赛')
    
    # 点击4次佳辩履历（+a,+b）
    print("2. 点击4次佳辩履历（+a,+b）")
    for i in range(4):
        tester.resume_module.addExcellentResume('国际赛')
    
    # 点击1次全程履历（+a,+b,+c）
    print("3. 点击1次全程履历（+a,+b,+c）")
    tester.resume_module.addFullResume('国际赛')
    
    # 开始事件循环
    print("\n🔄 进入事件循环，等待彩蛋触发...")
    sys.exit(app.exec_())

if __name__ == '__main__':
    test_easter_egg_full()
