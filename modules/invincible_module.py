#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
无敌模式模块
提供各种辩论无敌模式的开关控制功能
"""

from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal


class InvincibleModule(QGroupBox):
    """
    无敌模式模块
    
    Signals:
        mode_toggled: 当某个无敌模式状态变化时发出，包含模式名称和新状态
        all_enabled: 当全部开启按钮被点击时发出
        all_disabled: 当全部关闭按钮被点击时发出
    """
    
    mode_toggled = pyqtSignal(str, bool)
    all_enabled = pyqtSignal()
    all_disabled = pyqtSignal()
    
    def __init__(self):
        """初始化无敌模式模块"""
        super().__init__('💪 无敌模式')
        self.initUI()
        self.initConnections()
    
    def initUI(self):
        """初始化UI组件"""
        group_layout = QVBoxLayout()
        
        # 复选框
        checkbox_layout = QVBoxLayout()
        self.invincible_speech = QCheckBox('无敌申论')
        self.invincible_summary = QCheckBox('无敌结辩')
        self.invincible_question = QCheckBox('无敌质询')
        self.invincible_all = QCheckBox('全模式无敌')
        
        checkbox_layout.addWidget(self.invincible_speech)
        checkbox_layout.addWidget(self.invincible_summary)
        checkbox_layout.addWidget(self.invincible_question)
        checkbox_layout.addWidget(self.invincible_all)
        
        # 按钮组
        button_layout = QHBoxLayout()
        self.enable_all = QPushButton('全部开启')
        self.enable_all.setObjectName('btn-primary')
        self.disable_all = QPushButton('全部关闭')
        self.disable_all.setObjectName('btn-reset')
        
        button_layout.addWidget(self.enable_all)
        button_layout.addWidget(self.disable_all)
        button_layout.addStretch()
        
        group_layout.addLayout(checkbox_layout)
        group_layout.addLayout(button_layout)
        
        self.setLayout(group_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        self.invincible_speech.stateChanged.connect(lambda state: self.mode_toggled.emit('无敌申论', state == Qt.Checked))
        self.invincible_summary.stateChanged.connect(lambda state: self.mode_toggled.emit('无敌结辩', state == Qt.Checked))
        self.invincible_question.stateChanged.connect(lambda state: self.mode_toggled.emit('无敌质询', state == Qt.Checked))
        self.invincible_all.stateChanged.connect(self.toggleAllInvincible)
        self.enable_all.clicked.connect(self.enableAllInvincible)
        self.disable_all.clicked.connect(self.disableAllInvincible)
    
    def toggleAllInvincible(self, state):
        """
        切换所有无敌模式的状态
        
        Args:
            state: 新的状态（Qt.Checked 或 Qt.Unchecked）
        """
        checked = (state == Qt.Checked)
        self.invincible_speech.setChecked(checked)
        self.invincible_summary.setChecked(checked)
        self.invincible_question.setChecked(checked)
    
    def enableAllInvincible(self):
        """开启所有无敌模式"""
        self.invincible_speech.setChecked(True)
        self.invincible_summary.setChecked(True)
        self.invincible_question.setChecked(True)
        self.invincible_all.setChecked(True)
        self.all_enabled.emit()
    
    def disableAllInvincible(self):
        """关闭所有无敌模式"""
        self.invincible_speech.setChecked(False)
        self.invincible_summary.setChecked(False)
        self.invincible_question.setChecked(False)
        self.invincible_all.setChecked(False)
        self.all_disabled.emit()
    
    def getModeStatus(self, mode_name) -> bool:
        """
        获取指定无敌模式的状态
        
        Args:
            mode_name: 模式名称
            
        Returns:
            bool: 模式是否开启
        """
        mode_map = {
            '无敌申论': self.invincible_speech,
            '无敌结辩': self.invincible_summary,
            '无敌质询': self.invincible_question,
            '全模式无敌': self.invincible_all
        }
        
        if mode_name in mode_map:
            return mode_map[mode_name].isChecked()
        return False