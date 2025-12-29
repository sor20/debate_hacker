#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
履历修改器模块
提供辩论履历的修改和统计功能
"""

from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal


class ResumeModule(QGroupBox):
    """
    履历修改器模块
    
    Signals:
        resume_changed: 当履历数据变化时发出
        resume_cleared: 当履历被清空时发出
    """
    
    resume_changed = pyqtSignal()
    resume_cleared = pyqtSignal()
    
    def __init__(self):
        """初始化履历修改器模块"""
        super().__init__('📋 履历修改器')
        self.resume_data = {
            '国际赛': {'a': 0, 'b': 0, 'c': 0},
            '无限制级': {'a': 0, 'b': 0, 'c': 0},
            '限制级': {'a': 0, 'b': 0, 'c': 0}
        }
        self.resume_controls = {}
        self.initUI()
        self.initConnections()
    
    def initUI(self):
        """初始化UI组件"""
        group_layout = QVBoxLayout()
        
        categories = ['国际赛', '无限制级', '限制级']
        
        for category in categories:
            category_group = QGroupBox(category)
            category_layout = QVBoxLayout()
            
            # 创建加一按钮布局
            add_buttons_layout = QHBoxLayout()
            
            # 普通履历加1：仅在统计值a上增加1
            add_normal_btn = QPushButton('普通履历 +1')
            add_normal_btn.setObjectName('btn-primary')
            
            # 佳辩履历：在统计值a和b上分别增加1
            add_excellent_btn = QPushButton('佳辩履历 +1')
            add_excellent_btn.setObjectName('btn-primary')
            
            # 全程履历：在统计值a、b和c上分别增加1
            add_full_btn = QPushButton('全程履历 +1')
            add_full_btn.setObjectName('btn-primary')
            
            add_buttons_layout.addWidget(add_normal_btn)
            add_buttons_layout.addWidget(add_excellent_btn)
            add_buttons_layout.addWidget(add_full_btn)
            add_buttons_layout.addStretch()
            
            category_layout.addLayout(add_buttons_layout)
            category_group.setLayout(category_layout)
            group_layout.addWidget(category_group)
            
            # 保存引用
            self.resume_controls[category] = {
                'add_normal': add_normal_btn,
                'add_excellent': add_excellent_btn,
                'add_full': add_full_btn
            }
        
        # 全局控制按钮
        global_buttons = QHBoxLayout()
        self.clear_resume = QPushButton('清空所有履历')
        self.clear_resume.setObjectName('btn-reset')
        
        global_buttons.addWidget(self.clear_resume)
        global_buttons.addStretch()
        
        # 统计显示
        self.resume_count_label = QLabel('')
        self.resume_count_label.setFont(QFont('微软雅黑', 12, QFont.Bold))
        self.resume_count_label.setStyleSheet('padding: 10px; border: 2px solid #555; border-radius: 5px;')
        
        group_layout.addLayout(global_buttons)
        group_layout.addWidget(self.resume_count_label)
        
        self.setLayout(group_layout)
        
        # 初始更新统计
        self.updateResumeStats()
    
    def initConnections(self):
        """初始化信号连接"""
        for category in self.resume_controls:
            controls = self.resume_controls[category]
            controls['add_normal'].clicked.connect(lambda checked, cat=category: self.addNormalResume(cat))
            controls['add_excellent'].clicked.connect(lambda checked, cat=category: self.addExcellentResume(cat))
            controls['add_full'].clicked.connect(lambda checked, cat=category: self.addFullResume(cat))
        
        self.clear_resume.clicked.connect(self.clearAllResume)
    
    def addNormalResume(self, category):
        """
        增加普通履历
        
        Args:
            category: 履历分类
        """
        if category in self.resume_data:
            self.resume_data[category]['a'] += 1
            self.updateResumeStats()
            self.resume_changed.emit()
    
    def addExcellentResume(self, category):
        """
        增加佳辩履历
        
        Args:
            category: 履历分类
        """
        if category in self.resume_data:
            self.resume_data[category]['a'] += 1
            self.resume_data[category]['b'] += 1
            self.updateResumeStats()
            self.resume_changed.emit()
    
    def addFullResume(self, category):
        """
        增加全程履历
        
        Args:
            category: 履历分类
        """
        if category in self.resume_data:
            self.resume_data[category]['a'] += 1
            self.resume_data[category]['b'] += 1
            self.resume_data[category]['c'] += 1
            self.updateResumeStats()
            self.resume_changed.emit()
    
    def clearAllResume(self):
        """清空所有履历数据"""
        for category in self.resume_data:
            self.resume_data[category] = {'a': 0, 'b': 0, 'c': 0}
        
        self.updateResumeStats()
        self.resume_cleared.emit()
        self.resume_changed.emit()
    
    def updateResumeStats(self):
        """更新履历统计显示"""
        total_a = sum(self.resume_data[category]['a'] for category in self.resume_data)
        total_b = sum(self.resume_data[category]['b'] for category in self.resume_data)
        total_c = sum(self.resume_data[category]['c'] for category in self.resume_data)
        
        stats_text = (f"当前统计情况：\n"  
                     f"普通履历总数：{total_a} 份\n" 
                     f"佳辩履历总数：{total_b} 份\n" 
                     f"全程履历总数：{total_c} 份\n\n" 
                     f"分类统计：\n")
        
        for category in self.resume_data:
            a = self.resume_data[category]['a']
            b = self.resume_data[category]['b']
            c = self.resume_data[category]['c']
            stats_text += f"{category}：普通{a} / 佳辩{b} / 全程{c}\n"
        
        self.resume_count_label.setText(stats_text)
    
    def getResumeData(self):
        """
        获取当前履历数据
        
        Returns:
            dict: 当前履历数据
        """
        return self.resume_data
