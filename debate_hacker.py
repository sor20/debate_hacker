import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QPushButton, QLineEdit, QSlider, QCheckBox,
    QGroupBox, QScrollArea, QFrame, QDialog, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer, QPoint, QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QFont, QPalette, QColor, QPainter
# 不再使用QSound，改为在方法内导入QSoundEffect

# 导入自定义模块
from modules.debater_selector import DebaterSelector
from modules.time_module import TimeModule
from modules.favor_module import FavorModule
from modules.vote_module import VoteModule
from modules.invincible_module import InvincibleModule
from modules.resume_module import ResumeModule
from modules.status_module import StatusModule
from modules.easter_egg_module import EasterEggDialog
from modules.listening_module import ListeningModule

# 导入工具模块
from utils.logger import setup_logger
from utils.ui_utils import UIUtils
from utils.constants import *

class DebateHacker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initData()
        self.initUI()
        self.initConnections()
        
    def initUI(self):
        # 设置窗口
        self.setWindowTitle(APP_NAME)
        self.setGeometry(100, 100, DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 添加标题
        title_label = QLabel('⚔️ 辩论修改�?- Debate Hacker Pro')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('微软雅黑', 24, QFont.Bold))
        main_layout.addWidget(title_label)
        
        # 添加辩手选择器组�?
        self.debater_selector = DebaterSelector()
        main_layout.addWidget(self.debater_selector)
        
        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        
        # 滚动区域布局
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(20)
        
        # 1. 时间修改模块
        self.time_module = TimeModule()
        scroll_layout.addWidget(self.time_module)
        
        # 2. 评委好感度模�?
        self.favor_module = FavorModule()
        scroll_layout.addWidget(self.favor_module)
        
        # 3. 票型透视模块
        self.vote_module = VoteModule()
        scroll_layout.addWidget(self.vote_module)
        
        # 4. 无敌模式模块
        self.invincible_module = InvincibleModule()
        scroll_layout.addWidget(self.invincible_module)
        
        # 5. 履历修改器模�?
        self.resume_module = ResumeModule()
        scroll_layout.addWidget(self.resume_module)
        
        # 6. 评委听感模块
        self.listening_module = ListeningModule()
        scroll_layout.addWidget(self.listening_module)
        
        # 7. 状态显示
        self.status_module = StatusModule()
        scroll_layout.addWidget(self.status_module)
        
        main_layout.addWidget(scroll_area)
        
        # 应用深色主题
        UIUtils.applyDarkTheme(self)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def initData(self):
        # 初始化数据（模块已处理大部分，这里仅保留主应用必要的数据）
        self.easter_egg_triggered = False  # 彩蛋是否已触发的标志
    
    def initConnections(self):
        # 辩手选择器信号连接
        self.debater_selector.name_changed.connect(self.onNameChanged)
        
        # 时间模块信号连接
        self.time_module.time_changed.connect(self.onTimeChanged)
        self.time_module.time_reset.connect(self.onTimeReset)
        
        # 好感度模块信号连接
        self.favor_module.favor_changed.connect(self.onFavorChanged)
        
        # 票型透视模块信号连接
        self.vote_module.votes_updated.connect(self.onVotesUpdated)
        self.vote_module.refresh_toggled.connect(self.onRefreshToggled)
        
        # 无敌模块信号连接
        self.invincible_module.mode_toggled.connect(self.onInvincibleModeChanged)
        
        # 履历模块信号连接
        self.resume_module.resume_changed.connect(self.onResumeChanged)
        
        # 评委听感模块信号连接
        self.listening_module.listening_settings_changed.connect(self.onListeningSettingsChanged)
    
    # 新的信号处理方法
    def onNameChanged(self, name):
        """处理辩手姓名变化"""
        self.updateStatus('最后操作', f'修改辩手姓名为 {name}')
    
    def onFavorChanged(self, value):
        """处理好感度变化"""
        self.updateStatus('最后操作', f'好感度调整为 {value}')
    
    def onVotesUpdated(self):
        """处理票型更新"""
        pass  # 可以添加额外的处理逻辑
    
    def onRefreshToggled(self, is_refreshing):
        """处理实时刷新状态变化"""
        if is_refreshing:
            self.updateStatus('最后操作', '开启票型实时刷新')
        else:
            self.updateStatus('最后操作', '关闭票型实时刷新')
    
    def onTimeChanged(self, time_type, new_time):
        """处理时间变化"""
        if time_type == 'speech':
            self.updateStatus('最后操作', f'陈词时间调整为 {new_time} 秒')
        elif time_type == 'question':
            self.updateStatus('最后操作', f'质询时间调整为 {new_time} 秒')
    
    def onTimeReset(self, time_type):
        """处理时间重置"""
        if time_type == 'speech':
            self.updateStatus('最后操作', '陈词时间已重置')
        elif time_type == 'question':
            self.updateStatus('最后操作', '质询时间已重置')
    
    def onInvincibleModeChanged(self, mode_name, is_enabled):
        """处理无敌模式变化"""
        if is_enabled:
            self.updateStatus('最后操作', f'开启{mode_name}')
        else:
            self.updateStatus('最后操作', f'关闭{mode_name}')
    
    def onListeningSettingsChanged(self, settings):
        """处理评委听感设置变化"""
        self.updateStatus('最后操作', '评委听感设置已更新')
    
    def onResumeChanged(self):
        """处理履历更新"""
        self.updateStatus('最后操作', '履历已更新')
        
        if not self.easter_egg_triggered:
            resume_data = self.resume_module.getResumeData()
            total_a = sum(resume_data[category]['a'] for category in resume_data)
            total_b = sum(resume_data[category]['b'] for category in resume_data)
            total_c = sum(resume_data[category]['c'] for category in resume_data)
            
            # 添加用户友好的状态提示
            status_text = f"当前进度：{total_a}/10, {total_b}/5, {total_c}/1"
            self.updateStatus('彩蛋进度', status_text)
            
            if total_a >= 10 and total_b >= 5 and total_c >= 1:
                self.easter_egg_triggered = True
                self.triggerEasterEgg()
    
    # 时间模块方法
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    def updateStatus(self, label, value):
        self.status_module.setStatus(label, value)
    
    def triggerEasterEgg(self):
        """触发彩蛋"""
        # 创建彩蛋弹窗
        dialog = EasterEggDialog(self)
        dialog.exec_()



if __name__ == '__main__':
    # 启用高DPI支持
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    window = DebateHacker()
    window.show()
    sys.exit(app.exec_())
