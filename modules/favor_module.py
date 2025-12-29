#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
评委好感度模块
提供评委好感度的调整和显示功能
"""

from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QSlider, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class FavorModule(QGroupBox):
    """
    评委好感度模块
    
    Signals:
        favor_changed: 当好感度变化时发出，包含新的好感度值
    """
    
    favor_changed = pyqtSignal(int)
    
    def __init__(self):
        """初始化好感度模块"""
        super().__init__('❤️ 评委好感度')
        self.favor_value = 50  # 默认好感度为50
        self.initUI()
        self.initConnections()
    
    def initUI(self):
        """初始化UI组件"""
        group_layout = QVBoxLayout()
        
        # 滑块和输入框
        slider_layout = QHBoxLayout()
        self.favor_slider = QSlider(Qt.Horizontal)
        self.favor_slider.setRange(0, 100)
        self.favor_slider.setValue(self.favor_value)
        
        self.favor_input = QLineEdit(str(self.favor_value))
        self.favor_input.setMaximumWidth(60)
        self.favor_input.setAlignment(Qt.AlignCenter)
        
        self.favor_value_label = QLabel(f'当前好感度: {self.favor_value}')
        self.favor_value_label.setFont(QFont('微软雅黑', 14, QFont.Bold))
        
        slider_layout.addWidget(self.favor_slider)
        slider_layout.addWidget(self.favor_input)
        slider_layout.addWidget(self.favor_value_label)
        
        # 按钮组
        button_layout = QHBoxLayout()
        self.max_favor = QPushButton('拉满 (100)')
        self.max_favor.setObjectName('btn-primary')
        self.clear_favor = QPushButton('清空 (0)')
        self.clear_favor.setObjectName('btn-reset')
        self.add_favor_50 = QPushButton('+50')
        self.add_favor_50.setObjectName('btn-secondary')
        
        button_layout.addWidget(self.max_favor)
        button_layout.addWidget(self.clear_favor)
        button_layout.addWidget(self.add_favor_50)
        
        group_layout.addLayout(slider_layout)
        group_layout.addLayout(button_layout)
        
        self.setLayout(group_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        self.favor_slider.valueChanged.connect(self.updateFavorFromSlider)
        self.favor_input.textChanged.connect(self.updateFavorFromInput)
        self.max_favor.clicked.connect(lambda: self.setFavor(100))
        self.clear_favor.clicked.connect(lambda: self.setFavor(0))
        self.add_favor_50.clicked.connect(lambda: self.addFavor(50))
    
    def updateFavorFromSlider(self):
        """从滑块更新好感度"""
        self.favor_value = self.favor_slider.value()
        self.favor_input.setText(str(self.favor_value))
        self.favor_value_label.setText(f'当前好感度: {self.favor_value}')
        self.favor_changed.emit(self.favor_value)
    
    def updateFavorFromInput(self):
        """从输入框更新好感度"""
        try:
            value = int(self.favor_input.text())
            if 0 <= value <= 100:
                self.favor_value = value
                self.favor_slider.setValue(value)
                self.favor_value_label.setText(f'当前好感度: {self.favor_value}')
                self.favor_changed.emit(self.favor_value)
        except ValueError:
            pass
    
    def setFavor(self, value):
        """
        设置好感度为指定值
        
        Args:
            value: 目标好感度值
        """
        self.favor_value = max(0, min(100, value))  # 确保在0-100范围内
        self.favor_slider.setValue(self.favor_value)
        self.favor_input.setText(str(self.favor_value))
        self.favor_value_label.setText(f'当前好感度: {self.favor_value}')
        self.favor_changed.emit(self.favor_value)
    
    def addFavor(self, value):
        """
        增加好感度
        
        Args:
            value: 增加的好感度值
        """
        self.setFavor(self.favor_value + value)
    
    def getFavorValue(self) -> int:
        """
        获取当前好感度值
        
        Returns:
            int: 当前好感度值
        """
        return self.favor_value