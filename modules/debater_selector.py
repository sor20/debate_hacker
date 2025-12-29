#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
辩手选择器模块
提供辩手立场选择和姓名输入功能
"""

from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal


class DebaterSelector(QGroupBox):
    """
    辩手选择器组件
    
    Signals:
        positive_selected: 当选择正方时发出
        negative_selected: 当选择反方时发出
        name_changed: 当姓名输入变化时发出，包含新的姓名
    """
    
    positive_selected = pyqtSignal()
    negative_selected = pyqtSignal()
    name_changed = pyqtSignal(str)
    
    def __init__(self):
        """初始化辩手选择器"""
        super().__init__('👤 辩手选择')
        self.initUI()
        self.initConnections()
    
    def initUI(self):
        """初始化UI组件"""
        selector_layout = QHBoxLayout()
        
        # 正方/反方选择
        side_layout = QHBoxLayout()
        side_label = QLabel('选择立场:')
        self.positive_button = QPushButton('正方')
        self.positive_button.setObjectName('btn-primary')
        self.negative_button = QPushButton('反方')
        self.negative_button.setObjectName('btn-reset')
        
        side_layout.addWidget(side_label)
        side_layout.addWidget(self.positive_button)
        side_layout.addWidget(self.negative_button)
        
        # 姓名输入框
        name_layout = QHBoxLayout()
        name_label = QLabel('辩手姓名:')
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('请输入辩手姓名')
        self.name_input.setMaximumWidth(200)
        
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        
        # 将布局添加到选择器布局
        selector_layout.addLayout(side_layout)
        selector_layout.addLayout(name_layout)
        selector_layout.addStretch()
        
        self.setLayout(selector_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        self.positive_button.clicked.connect(self._onPositiveSelected)
        self.negative_button.clicked.connect(self._onNegativeSelected)
        self.name_input.textChanged.connect(self.name_changed)
    
    def _onPositiveSelected(self):
        """处理正方选择"""
        self.positive_button.setStyleSheet('background-color: #00ff00; color: #000000; border-color: #00ff00;')
        self.negative_button.setStyleSheet('background-color: #555; color: #ffffff; border-color: #555;')
        self.positive_selected.emit()
    
    def _onNegativeSelected(self):
        """处理反方选择"""
        self.negative_button.setStyleSheet('background-color: #ff0000; color: #ffffff; border-color: #ff0000;')
        self.positive_button.setStyleSheet('background-color: #555; color: #ffffff; border-color: #555;')
        self.negative_selected.emit()
    
    def getDebaterName(self) -> str:
        """
        获取当前输入的辩手姓名
        
        Returns:
            str: 辩手姓名
        """
        return self.name_input.text().strip()
    
    def setDebaterName(self, name: str):
        """
        设置辩手姓名
        
        Args:
            name: 辩手姓名
        """
        self.name_input.setText(name)