#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
时间控制模块
提供发言时间和质询时间的管理功能
"""

from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class TimeModule(QGroupBox):
    """
    时间控制模块
    
    Signals:
        time_changed: 当时间变化时发出，包含时间类型和新的时间值
        time_reset: 当时间重置时发出，包含时间类型
    """
    
    time_changed = pyqtSignal(str, int)
    time_reset = pyqtSignal(str)
    
    def __init__(self):
        """初始化时间控制模块"""
        super().__init__('⏱️ 时间控制')
        self.speech_time = 0
        self.question_time = 0
        self.initUI()
        self.initConnections()
    
    def initUI(self):
        """初始化UI组件"""
        group_layout = QGridLayout()
        
        # 陈词时间
        speech_label = QLabel('陈词时间:')
        self.speech_time_label = QLabel('0')
        self.speech_time_label.setFont(QFont('微软雅黑', 18, QFont.Bold))
        self.speech_time_label.setMinimumWidth(100)
        self.speech_time_label.setAlignment(Qt.AlignCenter)
        
        self.add_speech_10 = QPushButton('+10秒')
        self.add_speech_10.setObjectName('btn-primary')
        self.add_speech_999 = QPushButton('+999秒')
        self.add_speech_999.setObjectName('btn-secondary')
        self.reset_speech = QPushButton('重置')
        self.reset_speech.setObjectName('btn-reset')
        
        # 质询时间
        question_label = QLabel('质询时间:')
        self.question_time_label = QLabel('0')
        self.question_time_label.setFont(QFont('微软雅黑', 18, QFont.Bold))
        self.question_time_label.setMinimumWidth(100)
        self.question_time_label.setAlignment(Qt.AlignCenter)
        
        self.add_question_10 = QPushButton('+10秒')
        self.add_question_10.setObjectName('btn-primary')
        self.add_question_999 = QPushButton('+999秒')
        self.add_question_999.setObjectName('btn-secondary')
        self.reset_question = QPushButton('重置')
        self.reset_question.setObjectName('btn-reset')
        
        # 添加到布局
        group_layout.addWidget(speech_label, 0, 0, 1, 1)
        group_layout.addWidget(self.speech_time_label, 0, 1, 1, 1)
        group_layout.addWidget(self.add_speech_10, 0, 2, 1, 1)
        group_layout.addWidget(self.add_speech_999, 0, 3, 1, 1)
        group_layout.addWidget(self.reset_speech, 0, 4, 1, 1)
        
        group_layout.addWidget(question_label, 1, 0, 1, 1)
        group_layout.addWidget(self.question_time_label, 1, 1, 1, 1)
        group_layout.addWidget(self.add_question_10, 1, 2, 1, 1)
        group_layout.addWidget(self.add_question_999, 1, 3, 1, 1)
        group_layout.addWidget(self.reset_question, 1, 4, 1, 1)
        
        self.setLayout(group_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        self.add_speech_10.clicked.connect(lambda: self.addTime('speech', 10))
        self.add_speech_999.clicked.connect(lambda: self.addTime('speech', 999))
        self.reset_speech.clicked.connect(lambda: self.resetTime('speech'))
        self.add_question_10.clicked.connect(lambda: self.addTime('question', 10))
        self.add_question_999.clicked.connect(lambda: self.addTime('question', 999))
        self.reset_question.clicked.connect(lambda: self.resetTime('question'))
    
    def addTime(self, time_type, seconds):
        """
        增加指定类型的时间
        
        Args:
            time_type: 时间类型 ('speech' 或 'question')
            seconds: 增加的秒数
        """
        if time_type == 'speech':
            self.speech_time += seconds
            self.speech_time_label.setText(str(self.speech_time))
        else:
            self.question_time += seconds
            self.question_time_label.setText(str(self.question_time))
        
        self.time_changed.emit(time_type, seconds)
    
    def resetTime(self, time_type):
        """
        重置指定类型的时间
        
        Args:
            time_type: 时间类型 ('speech' 或 'question')
        """
        if time_type == 'speech':
            self.speech_time = 0
            self.speech_time_label.setText('0')
        else:
            self.question_time = 0
            self.question_time_label.setText('0')
        
        self.time_reset.emit(time_type)
    
    def getSpeechTime(self) -> int:
        """
        获取当前陈词时间
        
        Returns:
            int: 当前陈词时间（秒）
        """
        return self.speech_time
    
    def getQuestionTime(self) -> int:
        """
        获取当前质询时间
        
        Returns:
            int: 当前质询时间（秒）
        """
        return self.question_time