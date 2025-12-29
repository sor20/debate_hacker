#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
常量定义模块
包含应用中使用的所有常量值
"""

# 应用信息
APP_NAME = "辩论修改器"
APP_VERSION = "v1.0.2"
APP_TITLE = f"{APP_NAME} - Debate Hacker Pro"

# 窗口配置
DEFAULT_WINDOW_WIDTH = 900
DEFAULT_WINDOW_HEIGHT = 700
WINDOW_POSITION_X = 100
WINDOW_POSITION_Y = 100

# 时间模块配置
DEFAULT_SPEECH_TIME = 0
DEFAULT_QUESTION_TIME = 0
TIME_INCREMENTS = {
    "small": 10,
    "large": 999
}

# 好感度模块配置
DEFAULT_FAVOR_VALUE = 50
FAVOR_MIN = 0
FAVOR_MAX = 100
FAVOR_INCREMENT = 50

# 票型透视模块配置
REFRESH_INTERVAL = 2000  # 2秒
JUDGE_COUNT = 3
VOTE_TYPES = ["印象票", "环节票", "决胜票"]
VOTE_OPTIONS = ["正", "平", "反"]

# 无敌模式配置
INVINCIBLE_MODES = [
    "无敌申论",
    "无敌结辩", 
    "无敌质询"
]

# 履历修改器配置
RESUME_CATEGORIES = ["国际赛", "无限制级", "限制级"]
RESUME_TYPES = [
    "普通履历",
    "佳辩履历",
    "全程履历"
]

# 彩蛋触发条件
EASTER_EGG_CONDITIONS = {
    "categories": ["国际赛", "无限制级"],
    "min_counts": [10, 5, 1]  # [普通履历, 佳辩履历, 全程履历]
}

# 音乐文件配置
MUSIC_FILES = [
    "M800004Wxqxk3oWPnp.mp3",
    "celebration.wav",
    "celebration.mp3"
]
MUSIC_VOLUME = 0.5  # 50%

# UI配置
DEFAULT_FONT = "微软雅黑"
DEFAULT_FONT_SIZE = 12
DEFAULT_BOLD_FONT_SIZE = 14
TITLE_FONT_SIZE = 24
SECTION_TITLE_FONT_SIZE = 16

# 状态信息
DEFAULT_STATUS = {
    "修改器状态:": "就绪",
    "当前模式:": "正常模式",
    "最后操作:": "无",
    "系统时间:": ""
}

# 辩手立场
DEBATER_SIDES = {
    "positive": "正方",
    "negative": "反方"
}