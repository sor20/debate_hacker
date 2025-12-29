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
        
        # 统一间距设置
        group_layout.setSpacing(20)
        group_layout.setContentsMargins(10, 10, 10, 10)
        
        # 好感度控制区域
        favor_group = QGroupBox('好感度控制')
        favor_layout = QVBoxLayout()
        favor_layout.setSpacing(15)
        favor_layout.setContentsMargins(15, 15, 15, 15)
        
        # 滑块和输入框
        slider_layout = QHBoxLayout()
        slider_layout.setSpacing(10)
        
        self.favor_slider = QSlider(Qt.Horizontal)
        self.favor_slider.setRange(0, 100)
        self.favor_slider.setValue(self.favor_value)
        
        self.favor_input = QLineEdit(str(self.favor_value))
        self.favor_input.setMaximumWidth(60)
        self.favor_input.setAlignment(Qt.AlignCenter)
        self.favor_input.setFont(QFont('微软雅黑', 12))
        
        self.favor_value_label = QLabel(f'当前好感度: {self.favor_value}')
        self.favor_value_label.setFont(QFont('微软雅黑', 14, QFont.Bold))
        self.favor_value_label.setAlignment(Qt.AlignCenter)
        
        slider_layout.addWidget(self.favor_slider)
        slider_layout.addWidget(self.favor_input)
        slider_layout.addWidget(self.favor_value_label)
        
        # 按钮组
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.max_favor = QPushButton('拉满 (100)')
        self.max_favor.setObjectName('btn-primary')
        self.max_favor.setFont(QFont('微软雅黑', 12))
        
        self.clear_favor = QPushButton('清空 (0)')
        self.clear_favor.setObjectName('btn-reset')
        self.clear_favor.setFont(QFont('微软雅黑', 12))
        
        self.add_favor_50 = QPushButton('+50')
        self.add_favor_50.setObjectName('btn-secondary')
        self.add_favor_50.setFont(QFont('微软雅黑', 12))
        
        button_layout.addWidget(self.max_favor)
        button_layout.addWidget(self.clear_favor)
        button_layout.addWidget(self.add_favor_50)
        
        favor_layout.addLayout(slider_layout)
        favor_layout.addLayout(button_layout)
        favor_group.setLayout(favor_layout)
        
        # 评委心证调节区域
        bias_group = QGroupBox('评委心证调节')
        bias_layout = QVBoxLayout()
        bias_layout.setSpacing(10)  # 减小内部控件间距
        bias_layout.setContentsMargins(15, 10, 15, 10)  # 减小外边距
        
        # 心证滑块
        bias_slider_layout = QHBoxLayout()
        bias_slider_layout.setSpacing(10)
        
        # 反方标签
        anti_label = QLabel('反方')
        anti_label.setFont(QFont('微软雅黑', 12))
        anti_label.setAlignment(Qt.AlignCenter)
        anti_label.setMinimumWidth(40)
        
        # 心证滑块
        self.bias_slider = QSlider(Qt.Horizontal)
        self.bias_slider.setRange(0, 100)
        self.bias_slider.setValue(50)  # 默认中立
        self.bias_slider.setSingleStep(1)  # 步长为1
        self.bias_slider.setFixedHeight(20)  # 设置合适的滑块高度
        
        # 正方标签
        pro_label = QLabel('正方')
        pro_label.setFont(QFont('微软雅黑', 12))
        pro_label.setAlignment(Qt.AlignCenter)
        pro_label.setMinimumWidth(40)
        
        bias_slider_layout.addWidget(anti_label)
        bias_slider_layout.addWidget(self.bias_slider)
        bias_slider_layout.addWidget(pro_label)
        
        # 心证状态显示
        self.bias_status_label = QLabel('中立')
        self.bias_status_label.setFont(QFont('微软雅黑', 14, QFont.Bold))
        self.bias_status_label.setAlignment(Qt.AlignCenter)
        self.bias_status_label.setFixedHeight(30)  # 设置合适的标签高度
        
        bias_layout.addLayout(bias_slider_layout)
        bias_layout.addWidget(self.bias_status_label)
        bias_group.setLayout(bias_layout)
        
        group_layout.addWidget(favor_group)
        group_layout.addWidget(bias_group)
        
        self.setLayout(group_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        self.favor_slider.valueChanged.connect(self.updateFavorFromSlider)
        self.favor_input.textChanged.connect(self.updateFavorFromInput)
        self.max_favor.clicked.connect(lambda: self.setFavor(100))
        self.clear_favor.clicked.connect(lambda: self.setFavor(0))
        self.add_favor_50.clicked.connect(lambda: self.addFavor(50))
        
        # 评委心证滑块信号连接
        self.bias_slider.valueChanged.connect(self.updateBiasStatus)
    
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
    
    def updateBiasStatus(self):
        """根据心证滑块位置更新状态显示"""
        bias_value = self.bias_slider.value()
        
        if bias_value == 0:
            status_text = "心证在反"
        elif 0 < bias_value < 50:
            status_text = f"偏向反方({bias_value}%)"
        elif bias_value == 50:
            status_text = "中立"
        elif 50 < bias_value < 100:
            status_text = f"偏向正方({bias_value}%)"
        else:  # bias_value == 100
            status_text = "心证在正"
        
        self.bias_status_label.setText(status_text)
    
    def getBiasValue(self) -> int:
        """
        获取当前心证值
        
        Returns:
            int: 当前心证值(0-100)
        """
        return self.bias_slider.value()