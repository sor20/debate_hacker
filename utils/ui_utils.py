#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI工具模块
提供UI相关的工具函数和主题管理
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt


class UIUtils:
    """UI工具类，提供主题管理和UI辅助功能"""
    
    @staticmethod
    def applyDarkTheme(widget: QWidget) -> None:
        """
        应用深色主题到指定窗口部件
        
        Args:
            widget: 需要应用主题的窗口部件
        """
        # 创建深色调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 40))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(40, 40, 50))
        palette.setColor(QPalette.AlternateBase, QColor(50, 50, 60))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(50, 50, 60))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.Highlight, QColor(255, 0, 0))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(128, 128, 128))
        palette.setColor(QPalette.Disabled, QPalette.Text, QColor(128, 128, 128))
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(128, 128, 128))
        
        # 应用调色板
        widget.setPalette(palette)
        if hasattr(widget, 'centralWidget') and widget.centralWidget():
            widget.centralWidget().setPalette(palette)
        
        # 设置全局样式
        widget.setStyleSheet(UIUtils.getDarkThemeStyleSheet())
    
    @staticmethod
    def getDarkThemeStyleSheet() -> str:
        """
        获取深色主题的样式表
        
        Returns:
            str: Qt样式表字符串
        """
        return """
            * {
                color: #ffffff;
                background-color: transparent;
                font-family: '微软雅黑';
            }
            
            QMainWindow, QWidget, QScrollArea, QGroupBox {
                background-color: #282830;
            }
            
            QPushButton {
                padding: 10px 15px;
                border-radius: 5px;
                font-weight: bold;
                border: 2px solid;
                font-size: 12px;
            }
            
            QPushButton:hover {
                opacity: 0.9;
            }
            
            QPushButton:pressed {
                opacity: 0.8;
            }
            
            .btn-primary {
                background-color: #00ff00;
                color: #000000;
                border-color: #00ff00;
            }
            
            .btn-secondary {
                background-color: #ffff00;
                color: #000000;
                border-color: #ffff00;
            }
            
            .btn-reset {
                background-color: #ff0000;
                color: #ffffff;
                border-color: #ff0000;
            }
            
            QGroupBox {
                border: 2px solid #555;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                font-weight: bold;
                color: #ffffff;
                font-size: 16px;
            }
            
            QSlider::groove:horizontal {
                border: 1px solid #555;
                height: 10px;
                background: #333;
                border-radius: 5px;
            }
            
            QSlider::handle:horizontal {
                background: #00ff00;
                border: 1px solid #00ff00;
                width: 20px;
                margin: -5px 0;
                border-radius: 10px;
            }
            
            QLineEdit {
                padding: 8px;
                border: 2px solid #555;
                border-radius: 5px;
                background-color: #333;
                color: #fff;
                font-size: 12px;
            }
            
            QCheckBox {
                spacing: 8px;
                color: #ffffff;
                font-size: 12px;
            }
            
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                background-color: #333;
                border: 2px solid #555;
                border-radius: 4px;
            }
            
            QCheckBox::indicator:checked {
                background-color: #00ff00;
                border-color: #00ff00;
            }
            
            QLabel {
                color: #ffffff;
                font-size: 12px;
            }
            
            QScrollArea {
                border: none;
            }
            
            QScrollBar:vertical {
                background-color: #333;
                width: 10px;
                border-radius: 5px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #555;
                border-radius: 5px;
            }
            
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
            }
            
            QFrame {
                background-color: #282830;
            }
        """
    
    @staticmethod
    def createBoldFont(size: int = 12, family: str = "微软雅黑") -> QFont:
        """
        创建粗体字体
        
        Args:
            size: 字体大小
            family: 字体家族
            
        Returns:
            QFont: 粗体字体对象
        """
        font = QFont(family, size)
        font.setBold(True)
        return font