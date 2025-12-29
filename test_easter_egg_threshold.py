import sys
from PyQt5.QtWidgets import QApplication
from debate_hacker import DebateHacker

# 创建应用程序实例
app = QApplication(sys.argv)

# 创建主窗口实例
hacker = DebateHacker()

# 测试情况1：精确达到10+5+1
print("测试情况1：精确达到10+5+1")
# 设置履历数据为精确的触发条件
hacker.resume_module.resume_data = {
    "国际赛": {"a": 5, "b": 3, "c": 1},
    "无限制级": {"a": 3, "b": 1, "c": 0},
    "限制级": {"a": 2, "b": 1, "c": 0}
}
# 触发履历变化信号
hacker.onResumeChanged()

# 测试情况2：超过触发条件
print("\n测试情况2：超过触发条件")
# 重置触发状态（用于测试）
hacker.easter_egg_triggered = False
# 设置履历数据超过触发条件
hacker.resume_module.resume_data = {
    "国际赛": {"a": 6, "b": 3, "c": 1},
    "无限制级": {"a": 4, "b": 2, "c": 0},
    "限制级": {"a": 3, "b": 1, "c": 0}
}
# 触发履历变化信号
hacker.onResumeChanged()

# 测试情况3：未达到触发条件
print("\n测试情况3：未达到触发条件")
# 重置触发状态
hacker.easter_egg_triggered = False
# 设置履历数据未达到触发条件
hacker.resume_module.resume_data = {
    "国际赛": {"a": 4, "b": 2, "c": 1},
    "无限制级": {"a": 3, "b": 1, "c": 0},
    "限制级": {"a": 2, "b": 1, "c": 0}
}
# 触发履历变化信号
hacker.onResumeChanged()

print("\n测试完成")