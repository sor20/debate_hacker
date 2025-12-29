#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统状态模块
提供系统状态信息的显示功能
"""

from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, pyqtSignal
import time


class StatusModule(QGroupBox):
    """
    系统状态模块
    
    Signals:
        status_updated: 当系统状态更新时发出
    """
    
    status_updated = pyqtSignal()
    
    def __init__(self):
        """初始化系统状态模块"""
        super().__init__('📊 系统状态')
        self.status_labels = {}
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1秒更新一次系统时间
        self.initUI()
        self.initConnections()
        self.startTimer()
    
    def initUI(self):
        """初始化UI组件"""
        group_layout = QGridLayout()
        
        status_items = [
            ('修改器状态:', '就绪'),
            ('当前模式:', '正常模式'),
            ('最后操作:', '无'),
            ('系统时间:', '')
        ]
        
        for i, (label, value) in enumerate(status_items):
            group_layout.addWidget(QLabel(label), i, 0)
            status_label = QLabel(value)
            status_label.setStyleSheet('font-weight: bold;')
            group_layout.addWidget(status_label, i, 1)
            self.status_labels[label] = status_label
        
        self.setLayout(group_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        self.timer.timeout.connect(self.updateSystemTime)
    
    def startTimer(self):
        """启动系统时间更新定时器"""
        self.timer.start()
        self.updateSystemTime()
    
    def stopTimer(self):
        """停止系统时间更新定时器"""
        self.timer.stop()
    
    def updateSystemTime(self):
        """更新系统时间显示"""
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.setStatus('系统时间:', current_time)
    
    def setStatus(self, status_name, value):
        """
        设置指定状态的值
        
        Args:
            status_name: 状态名称
            value: 状态值
        """
        if status_name in self.status_labels:
            self.status_labels[status_name].setText(value)
            self.status_updated.emit()
    
    def getStatus(self, status_name):
        """
        获取指定状态的值
        
        Args:
            status_name: 状态名称
            
        Returns:
            str: 状态值
        """
        if status_name in self.status_labels:
            return self.status_labels[status_name].text()
        return ''

    def updateLastOperation(self, operation):
        """
        更新最后操作记录
        
        Args:
            operation: 操作描述
        """
        self.setStatus('最后操作:', operation)
