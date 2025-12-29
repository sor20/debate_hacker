#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
票型透视模块
提供评委投票情况的显示和实时更新功能
"""

import random
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QFont


class VoteModule(QGroupBox):
    """
    票型透视模块
    
    Signals:
        votes_updated: 当票型数据更新时发出
        refresh_toggled: 当实时刷新状态变化时发出，包含新的状态
    """
    
    votes_updated = pyqtSignal()
    refresh_toggled = pyqtSignal(bool)
    
    def __init__(self):
        """初始化票型透视模块"""
        super().__init__('👁️ 票型透视')
        self.judge_labels = []
        self.refresh_timer = QTimer()
        self.refresh_timer.setInterval(2000)  # 2秒刷新一次
        self.initUI()
        self.initConnections()
    
    def initUI(self):
        """初始化UI组件"""
        group_layout = QVBoxLayout()
        
        # 评委信息显示区域
        judges_layout = QGridLayout()
        
        # 创建三位评委的显示区域
        for i in range(3):
            judge_group = QGroupBox(f'评委{i+1}')
            judge_group.setMinimumHeight(200)
            judge_group.setMinimumWidth(250)
            judge_layout = QVBoxLayout()
            
            # 创建印象票、环节票、决胜票标签
            impression_label = QLabel('印象票: -')
            section_label = QLabel('环节票: -')
            decisive_label = QLabel('决胜票: -')
            
            # 设置字体和样式
            font = QFont('微软雅黑', 14)
            impression_label.setFont(font)
            section_label.setFont(font)
            decisive_label.setFont(font)
            
            judge_layout.addWidget(impression_label)
            judge_layout.addWidget(section_label)
            judge_layout.addWidget(decisive_label)
            
            judge_group.setLayout(judge_layout)
            judges_layout.addWidget(judge_group, 0, i)
            
            # 保存标签引用
            self.judge_labels.append((impression_label, section_label, decisive_label))
        
        # 统计结果显示
        self.stats_display = QLabel('正方比反方=0:0')
        self.stats_display.setAlignment(Qt.AlignCenter)
        self.stats_display.setFont(QFont('微软雅黑', 16, QFont.Bold))
        self.stats_display.setStyleSheet('padding: 10px; border: 2px solid #555; border-radius: 5px;')
        
        # 胜负判定显示
        self.result_display = QLabel('等待统计...')
        self.result_display.setAlignment(Qt.AlignCenter)
        self.result_display.setFont(QFont('微软雅黑', 18, QFont.Bold))
        self.result_display.setStyleSheet('padding: 10px; color: #00ff00;')
        
        # 强制数据验证区域
        validation_group = QGroupBox('强制数据验证')
        validation_layout = QVBoxLayout()
        
        # 创建单选按钮组
        self.validation_radio1 = QRadioButton('检证对方重要数据')
        self.validation_radio2 = QRadioButton('检证对方大部分数据')
        self.validation_radio3 = QRadioButton('检证对方全部数据')
        
        # 设置默认选中第一个选项
        self.validation_radio1.setChecked(True)
        
        # 设置字体
        font = QFont('微软雅黑', 11)
        self.validation_radio1.setFont(font)
        self.validation_radio2.setFont(font)
        self.validation_radio3.setFont(font)
        
        validation_layout.addWidget(self.validation_radio1)
        validation_layout.addWidget(self.validation_radio2)
        validation_layout.addWidget(self.validation_radio3)
        validation_group.setLayout(validation_layout)
        
        # 控制按钮
        control_layout = QHBoxLayout()
        self.show_votes_btn = QPushButton('开启票型透视')
        self.show_votes_btn.setObjectName('btn-primary')
        
        self.refresh_checkbox = QCheckBox('实时刷新')
        
        control_layout.addWidget(self.show_votes_btn)
        control_layout.addWidget(self.refresh_checkbox)
        control_layout.addStretch()
        
        group_layout.addLayout(judges_layout)
        group_layout.addWidget(self.stats_display)
        group_layout.addWidget(self.result_display)
        group_layout.addWidget(validation_group)
        group_layout.addLayout(control_layout)
        
        self.setLayout(group_layout)
    
    def initConnections(self):
        """初始化信号连接"""
        self.show_votes_btn.clicked.connect(self.updateVoteDisplay)
        self.refresh_checkbox.stateChanged.connect(self.toggleRefresh)
        self.refresh_timer.timeout.connect(self.updateVoteDisplay)
    
    def updateVoteDisplay(self):
        """更新投票显示"""
        # 初始化统计变量
        total_positive = 0
        total_negative = 0
        decisive_counts = {'正': 0, '反': 0}
        
        # 为每位评委生成投票数据
        for i in range(3):
            # 生成印象票 (正/平/反)
            impression_vote = random.choice(['正', '平', '反'])
            
            # 生成环节票 (正/平/反)
            section_vote = random.choice(['正', '平', '反'])
            
            # 生成决胜票 (正/反)
            decisive_vote = random.choice(['正', '反'])
            
            # 更新评委标签
            impression_label, section_label, decisive_label = self.judge_labels[i]
            impression_label.setText(f'印象票: {impression_vote}')
            section_label.setText(f'环节票: {section_vote}')
            decisive_label.setText(f'决胜票: {decisive_vote}')
            
            # 计算统计数据 - 确保总票数为9（3位评委×3种票型）
            # 印象票统计：正=1分（正方），反=1分（反方），平=0.5分（双方）
            if impression_vote == '正':
                total_positive += 1
            elif impression_vote == '反':
                total_negative += 1
            else:  # 平
                total_positive += 0.5
                total_negative += 0.5
            
            # 环节票统计：正=1分（正方），反=1分（反方），平=0.5分（双方）
            if section_vote == '正':
                total_positive += 1
            elif section_vote == '反':
                total_negative += 1
            else:  # 平
                total_positive += 0.5
                total_negative += 0.5
            
            # 决胜票统计：正=1分（正方），反=1分（反方）
            if decisive_vote == '正':
                total_positive += 1
                decisive_counts['正'] += 1
            else:  # 反
                total_negative += 1
                decisive_counts['反'] += 1
        
        # 确保总和为9票
        total_positive = round(total_positive, 1)
        total_negative = round(total_negative, 1)
        
        # 强制确保总和为9票，处理浮点数精度问题
        total = total_positive + total_negative
        if abs(total - 9) > 0.001:
            # 如果总和不是9，调整其中一个值
            if total_positive > total_negative:
                total_negative = 9 - total_positive
            else:
                total_positive = 9 - total_negative
        
        # 更新统计显示
        self.stats_display.setText(f'正方比反方={total_positive}:{total_negative}')
        
        # 判定胜负
        if total_positive > total_negative:
            self.result_display.setText('正方胜')
            self.result_display.setStyleSheet('padding: 10px; color: #00ff00;')
        elif total_positive < total_negative:
            self.result_display.setText('反方胜')
            self.result_display.setStyleSheet('padding: 10px; color: #ff0000;')
        else:  # 4.5:4.5
            self.result_display.setText(f'正方比反方为4.5:4.5\n决胜票为{decisive_counts["正"]}:{decisive_counts["反"]}\n')
            
            # 根据决胜票判定胜负
            if decisive_counts['正'] > decisive_counts['反']:
                self.result_display.setText(self.result_display.text() + '正方胜')
                self.result_display.setStyleSheet('padding: 10px; color: #00ff00;')
            else:
                self.result_display.setText(self.result_display.text() + '反方胜')
                self.result_display.setStyleSheet('padding: 10px; color: #ff0000;')
        
        self.votes_updated.emit()
    
    def toggleRefresh(self, state):
        """切换实时刷新状态"""
        if state == Qt.Checked:
            self.refresh_timer.start()
            self.refresh_toggled.emit(True)
        else:
            self.refresh_timer.stop()
            self.refresh_toggled.emit(False)
    
    def getCurrentStats(self) -> tuple:
        """
        获取当前的投票统计数据
        
        Returns:
            tuple: (正方分数, 反方分数, 胜负结果)
        """
        stats_text = self.stats_display.text()
        # 解析统计文本获取分数
        if '=' in stats_text:
            score_part = stats_text.split('=')[1]
            if ':' in score_part:
                pos_score, neg_score = score_part.split(':')
                return float(pos_score), float(neg_score), self.result_display.text()
        return 0.0, 0.0, '等待统计...'