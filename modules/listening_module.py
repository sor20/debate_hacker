#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
评委听感模块
提供评委听感调节功能
"""

from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class ListeningModule(QGroupBox):
    """
    评委听感模块
    
    Signals:
        listening_settings_changed: 当听感设置变化时发出，包含设置内容
    """
    
    listening_settings_changed = pyqtSignal(dict)
    
    def __init__(self):
        """初始化评委听感模块"""
        super().__init__('👂 评委听感')
        self.initUI()
        self.initConnections()
    
    def initUI(self):
        """初始化UI组件"""
        group_layout = QVBoxLayout()
        
        # 漏听对方内容模块
        miss_listening_group = QGroupBox('漏听对方内容')
        miss_listening_layout = QVBoxLayout()
        
        # 创建漏听对方内容的复选框
        self.miss_data_checkbox = QCheckBox('漏听对方数据')
        self.miss_examples_checkbox = QCheckBox('漏听对方例子')
        self.miss_reasoning_checkbox = QCheckBox('漏听对方推论')
        
        # 设置字体
        font = QFont('微软雅黑', 12)
        self.miss_data_checkbox.setFont(font)
        self.miss_examples_checkbox.setFont(font)
        self.miss_reasoning_checkbox.setFont(font)
        
        miss_listening_layout.addWidget(self.miss_data_checkbox)
        miss_listening_layout.addWidget(self.miss_examples_checkbox)
        miss_listening_layout.addWidget(self.miss_reasoning_checkbox)
        miss_listening_group.setLayout(miss_listening_layout)
        
        # 提升我方内容模块
        enhance_listening_group = QGroupBox('提升我方内容')
        enhance_listening_layout = QVBoxLayout()
        
        # 创建提升我方内容的复选框
        self.enhance_data_checkbox = QCheckBox('提升我方数据')
        self.enhance_reasoning_checkbox = QCheckBox('提升我方推论')
        self.enhance_examples_checkbox = QCheckBox('提升我方例子')
        
        # 设置字体
        self.enhance_data_checkbox.setFont(font)
        self.enhance_reasoning_checkbox.setFont(font)
        self.enhance_examples_checkbox.setFont(font)
        
        enhance_listening_layout.addWidget(self.enhance_data_checkbox)
        enhance_listening_layout.addWidget(self.enhance_reasoning_checkbox)
        enhance_listening_layout.addWidget(self.enhance_examples_checkbox)
        enhance_listening_group.setLayout(enhance_listening_layout)
        
        # 将子模块添加到主布局
        group_layout.addWidget(miss_listening_group)
        group_layout.addWidget(enhance_listening_group)
        
        self.setLayout(group_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        # 为所有复选框添加信号连接
        self.miss_data_checkbox.stateChanged.connect(self.onSettingsChanged)
        self.miss_examples_checkbox.stateChanged.connect(self.onSettingsChanged)
        self.miss_reasoning_checkbox.stateChanged.connect(self.onSettingsChanged)
        self.enhance_data_checkbox.stateChanged.connect(self.onSettingsChanged)
        self.enhance_reasoning_checkbox.stateChanged.connect(self.onSettingsChanged)
        self.enhance_examples_checkbox.stateChanged.connect(self.onSettingsChanged)
    
    def onSettingsChanged(self):
        """当设置变化时发出信号"""
        settings = self.getListeningSettings()
        self.listening_settings_changed.emit(settings)
    
    def getListeningSettings(self):
        """
        获取当前的听感设置
        
        Returns:
            dict: 包含漏听对方内容和提升我方内容的设置
        """
        return {
            'miss_listening': {
                'data': self.miss_data_checkbox.isChecked(),
                'examples': self.miss_examples_checkbox.isChecked(),
                'reasoning': self.miss_reasoning_checkbox.isChecked()
            },
            'enhance_listening': {
                'data': self.enhance_data_checkbox.isChecked(),
                'reasoning': self.enhance_reasoning_checkbox.isChecked(),
                'examples': self.enhance_examples_checkbox.isChecked()
            }
        }
    
    def setListeningSettings(self, settings):
        """
        设置听感设置
        
        Args:
            settings: 包含漏听对方内容和提升我方内容的设置
        """
        if 'miss_listening' in settings:
            miss_settings = settings['miss_listening']
            if 'data' in miss_settings:
                self.miss_data_checkbox.setChecked(miss_settings['data'])
            if 'examples' in miss_settings:
                self.miss_examples_checkbox.setChecked(miss_settings['examples'])
            if 'reasoning' in miss_settings:
                self.miss_reasoning_checkbox.setChecked(miss_settings['reasoning'])
        
        if 'enhance_listening' in settings:
            enhance_settings = settings['enhance_listening']
            if 'data' in enhance_settings:
                self.enhance_data_checkbox.setChecked(enhance_settings['data'])
            if 'reasoning' in enhance_settings:
                self.enhance_reasoning_checkbox.setChecked(enhance_settings['reasoning'])
            if 'examples' in enhance_settings:
                self.enhance_examples_checkbox.setChecked(enhance_settings['examples'])
