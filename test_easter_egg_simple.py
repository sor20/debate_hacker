#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的彩蛋测试脚本
只检查触发条件的计算是否正确
"""

import sys
import os
from PyQt5.QtWidgets import QApplication

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入resume_module来测试数据计算
from modules.resume_module import ResumeModule

def test_easter_egg_condition():
    """测试彩蛋触发条件的计算"""
    print("🎯 测试彩蛋触发条件的计算")
    
    # 创建履历模块实例
    resume_module = ResumeModule()
    
    # 测试用例1：直接设置数据为10+5+1
    print("\n测试用例1：直接设置数据为10+5+1")
    resume_module.resume_data = {
        '国际赛': {'a': 5, 'b': 5, 'c': 1},
        '无限制级': {'a': 3, 'b': 0, 'c': 0},
        '限制级': {'a': 2, 'b': 0, 'c': 0}
    }
    
    # 手动计算total_a, total_b, total_c
    total_a = sum(resume_module.resume_data[category]['a'] for category in resume_module.resume_data)
    total_b = sum(resume_module.resume_data[category]['b'] for category in resume_module.resume_data)
    total_c = sum(resume_module.resume_data[category]['c'] for category in resume_module.resume_data)
    
    print(f"计算结果：total_a={total_a}, total_b={total_b}, total_c={total_c}")
    print(f"触发条件：{total_a == 10} && {total_b == 5} && {total_c == 1}")
    
    # 测试用例2：模拟用户点击增加履历
    print("\n测试用例2：模拟用户点击增加履历")
    resume_module.clearAllResume()  # 清空数据
    
    # 点击5次普通履历（+a）
    print("1. 点击5次普通履历（+a）")
    for i in range(5):
        resume_module.addNormalResume('国际赛')
    
    # 点击4次佳辩履历（+a,+b）
    print("2. 点击4次佳辩履历（+a,+b）")
    for i in range(4):
        resume_module.addExcellentResume('国际赛')
    
    # 点击1次全程履历（+a,+b,+c）
    print("3. 点击1次全程履历（+a,+b,+c）")
    resume_module.addFullResume('国际赛')
    
    # 手动计算total_a, total_b, total_c
    total_a = sum(resume_module.resume_data[category]['a'] for category in resume_module.resume_data)
    total_b = sum(resume_module.resume_data[category]['b'] for category in resume_module.resume_data)
    total_c = sum(resume_module.resume_data[category]['c'] for category in resume_module.resume_data)
    
    print(f"计算结果：total_a={total_a}, total_b={total_b}, total_c={total_c}")
    print(f"触发条件：{total_a == 10} && {total_b == 5} && {total_c == 1}")

if __name__ == '__main__':
    # 创建QApplication实例
    app = QApplication(sys.argv)
    test_easter_egg_condition()
    # 不需要执行app.exec_()，因为我们不需要显示GUI

