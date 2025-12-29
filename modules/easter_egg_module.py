#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
彩蛋模块
提供程序的彩蛋功能
"""

import sys
import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class EasterEggDialog(QDialog):
    """彩蛋弹窗类"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('🎉 恭喜你达到10+5+1成就！')
        self.resize(600, 400)
        self.setStyleSheet("background-color: #282830;")
        
        # 布局
        main_layout = QVBoxLayout(self)
        
        # 标题
        title_label = QLabel('🎉 恭喜你达到10+5+1成就！🎉')
        title_label.setFont(QFont('微软雅黑', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('color: #00ff00; margin: 20px 0;')
        main_layout.addWidget(title_label)
        
        # 播放庆祝音乐
        self.playCelebrationMusic()
        
        # 庆祝信息
        celebration_label = QLabel('🎵 正在播放庆祝音乐 🎵')
        celebration_label.setFont(QFont('微软雅黑', 18))
        celebration_label.setAlignment(Qt.AlignCenter)
        celebration_label.setStyleSheet('color: #ffff00; margin: 20px 0;')
        main_layout.addWidget(celebration_label)
        
        # 用户输入区域
        input_layout = QHBoxLayout()
        name_label = QLabel('请输入你的名字:')
        name_label.setFont(QFont('微软雅黑', 14))
        name_label.setStyleSheet('color: #ffffff;')
        
        self.name_input = QLineEdit()
        self.name_input.setFont(QFont('微软雅黑', 14))
        self.name_input.setPlaceholderText('输入你的名字...')
        self.name_input.setStyleSheet('''
            QLineEdit {
                background-color: #333;
                color: #fff;
                border: 2px solid #555;
                border-radius: 5px;
                padding: 8px;
                min-width: 200px;
            }
        ''')
        
        submit_btn = QPushButton('确定')
        submit_btn.setFont(QFont('微软雅黑', 14, QFont.Bold))
        submit_btn.setStyleSheet('''
            QPushButton {
                background-color: #00ff00;
                color: #000;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #00cc00;
            }
        ''')
        submit_btn.clicked.connect(self.submitName)
        
        input_layout.addWidget(name_label)
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(submit_btn)
        input_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(input_layout)
        
        # 信息显示区域
        self.message_label = QLabel()
        self.message_label.setFont(QFont('微软雅黑', 18, QFont.Bold))
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet('color: #ff6b6b; margin-top: 30px; padding: 10px;')
        main_layout.addWidget(self.message_label)
        
        # 添加装饰性元素
        decor_label = QLabel('🏆 无敌辩手 🏆')
        decor_label.setFont(QFont('微软雅黑', 20, QFont.Bold))
        decor_label.setAlignment(Qt.AlignCenter)
        decor_label.setStyleSheet('color: #ffd700; margin-top: 20px;')
        main_layout.addWidget(decor_label)
    
    def playCelebrationMusic(self):
        """播放庆祝音乐"""
        # 简化音乐播放逻辑，避免影响弹窗显示
        try:
            # 创建媒体播放器实例
            self.media_player = QMediaPlayer()
            self.media_player.setVolume(50)  # 设置音量为50%
            
            # 获取程序运行目录
            if hasattr(sys, '_MEIPASS'):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath('.')
            
            # 优先使用用户提供的音乐文件，然后是默认文件名
            music_files = ["M800004Wxqxk3oWPnp.mp3", "celebration.wav", "celebration.mp3"]
            
            for file in music_files:
                try:
                    file_path = os.path.join(base_path, file)
                    if os.path.exists(file_path):
                        media_content = QMediaContent(QUrl.fromLocalFile(file_path))
                        self.media_player.setMedia(media_content)
                        self.media_player.play()
                        break
                except Exception:
                    # 忽略音乐播放错误，确保弹窗正常显示
                    pass
        except Exception:
            # 完全忽略音乐播放错误，不影响弹窗功能
            pass
    
    def submitName(self):
        """提交用户名并显示恭喜信息"""
        name = self.name_input.text().strip()
        if not name:
            name = '辩手'
        
        message = f'恭喜你伟大的{name}你已经成为无敌的10+5+1辩手'
        self.message_label.setText(message)
        
        # 禁用输入框和按钮
        self.name_input.setEnabled(False)
        self.sender().setEnabled(False)
