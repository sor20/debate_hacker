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

class DebateHacker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initData()
        self.initUI()
        self.initConnections()
        
    def initUI(self):
        # 设置窗口
        self.setWindowTitle('辩论修改器 v1.0.2')
        self.setGeometry(100, 100, 900, 700)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 添加标题
        title_label = QLabel('⚔️ 辩论修改器 - Debate Hacker Pro')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('微软雅黑', 24, QFont.Bold))
        main_layout.addWidget(title_label)
        
        # 添加辩手选择器组件
        self.createDebaterSelector(main_layout)
        
        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        
        # 滚动区域布局
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(20)
        
        # 1. 时间修改模块
        self.createTimeModule(scroll_layout)
        
        # 2. 评委好感度模块
        self.createFavorModule(scroll_layout)
        
        # 3. 票型透视模块
        self.createVoteModule(scroll_layout)
        
        # 4. 无敌模式模块
        self.createInvincibleModule(scroll_layout)
        
        # 5. 履历修改器模块
        self.createResumeModule(scroll_layout)
        
        # 6. 状态显示
        self.createStatusModule(scroll_layout)
        
        main_layout.addWidget(scroll_area)
        
        # 应用深色主题
        self.applyDarkTheme()
    
    def createDebaterSelector(self, layout):
        """创建辩手选择器组件"""
        selector_group = QGroupBox('👤 辩手选择')
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
        
        selector_group.setLayout(selector_layout)
        layout.addWidget(selector_group)
    
    def applyDarkTheme(self):
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
        
        # 应用调色板到所有组件
        self.setPalette(palette)
        self.centralWidget().setPalette(palette)
        
        # 设置全局样式
        self.setStyleSheet("""
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
        """)
    
    def createTimeModule(self, layout):
        group = QGroupBox('⏱️ 时间控制')
        group_layout = QGridLayout()
        
        # 陈词时间
        speech_label = QLabel('陈词时间:')
        self.speech_time_label = QLabel('0')
        self.speech_time_label.setFont(QFont('微软雅黑', 18, QFont.Bold))
        self.speech_time_label.setMinimumWidth(100)
        self.speech_time_label.setAlignment(Qt.AlignCenter)
        
        add_speech_10 = QPushButton('+10秒')
        add_speech_10.setObjectName('btn-primary')
        add_speech_999 = QPushButton('+999秒')
        add_speech_999.setObjectName('btn-secondary')
        reset_speech = QPushButton('重置')
        reset_speech.setObjectName('btn-reset')
        
        # 质询时间
        question_label = QLabel('质询时间:')
        self.question_time_label = QLabel('0')
        self.question_time_label.setFont(QFont('微软雅黑', 18, QFont.Bold))
        self.question_time_label.setMinimumWidth(100)
        self.question_time_label.setAlignment(Qt.AlignCenter)
        
        add_question_10 = QPushButton('+10秒')
        add_question_10.setObjectName('btn-primary')
        add_question_999 = QPushButton('+999秒')
        add_question_999.setObjectName('btn-secondary')
        reset_question = QPushButton('重置')
        reset_question.setObjectName('btn-reset')
        
        # 添加到布局
        group_layout.addWidget(speech_label, 0, 0, 1, 1)
        group_layout.addWidget(self.speech_time_label, 0, 1, 1, 1)
        group_layout.addWidget(add_speech_10, 0, 2, 1, 1)
        group_layout.addWidget(add_speech_999, 0, 3, 1, 1)
        group_layout.addWidget(reset_speech, 0, 4, 1, 1)
        
        group_layout.addWidget(question_label, 1, 0, 1, 1)
        group_layout.addWidget(self.question_time_label, 1, 1, 1, 1)
        group_layout.addWidget(add_question_10, 1, 2, 1, 1)
        group_layout.addWidget(add_question_999, 1, 3, 1, 1)
        group_layout.addWidget(reset_question, 1, 4, 1, 1)
        
        group.setLayout(group_layout)
        layout.addWidget(group)
        
        # 保存按钮引用
        self.add_speech_10 = add_speech_10
        self.add_speech_999 = add_speech_999
        self.reset_speech = reset_speech
        self.add_question_10 = add_question_10
        self.add_question_999 = add_question_999
        self.reset_question = reset_question
    
    def createFavorModule(self, layout):
        group = QGroupBox('❤️ 评委好感度')
        group_layout = QVBoxLayout()
        
        # 滑块和输入框
        slider_layout = QHBoxLayout()
        self.favor_slider = QSlider(Qt.Horizontal)
        self.favor_slider.setRange(0, 100)
        self.favor_slider.setValue(50)
        
        self.favor_input = QLineEdit('50')
        self.favor_input.setMaximumWidth(60)
        self.favor_input.setAlignment(Qt.AlignCenter)
        
        self.favor_value_label = QLabel('当前好感度: 50')
        self.favor_value_label.setFont(QFont('微软雅黑', 14, QFont.Bold))
        
        slider_layout.addWidget(self.favor_slider)
        slider_layout.addWidget(self.favor_input)
        slider_layout.addWidget(self.favor_value_label)
        
        # 按钮组
        button_layout = QHBoxLayout()
        max_favor = QPushButton('拉满 (100)')
        max_favor.setObjectName('btn-primary')
        clear_favor = QPushButton('清空 (0)')
        clear_favor.setObjectName('btn-reset')
        add_favor_50 = QPushButton('+50')
        add_favor_50.setObjectName('btn-secondary')
        
        button_layout.addWidget(max_favor)
        button_layout.addWidget(clear_favor)
        button_layout.addWidget(add_favor_50)
        
        group_layout.addLayout(slider_layout)
        group_layout.addLayout(button_layout)
        
        group.setLayout(group_layout)
        layout.addWidget(group)
        
        # 保存按钮引用
        self.max_favor = max_favor
        self.clear_favor = clear_favor
        self.add_favor_50 = add_favor_50
    
    def createVoteModule(self, layout):
        group = QGroupBox('👁️ 票型透视')
        group_layout = QVBoxLayout()
        
        # 评委信息显示区域
        judges_layout = QGridLayout()
        self.judge_labels = []
        
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
        group_layout.addLayout(control_layout)
        
        group.setLayout(group_layout)
        layout.addWidget(group)
    
    def createInvincibleModule(self, layout):
        group = QGroupBox('💪 无敌模式')
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
        enable_all = QPushButton('全部开启')
        enable_all.setObjectName('btn-primary')
        disable_all = QPushButton('全部关闭')
        disable_all.setObjectName('btn-reset')
        
        button_layout.addWidget(enable_all)
        button_layout.addWidget(disable_all)
        button_layout.addStretch()
        
        group_layout.addLayout(checkbox_layout)
        group_layout.addLayout(button_layout)
        
        group.setLayout(group_layout)
        layout.addWidget(group)
        
        # 保存按钮引用
        self.enable_all = enable_all
        self.disable_all = disable_all
    
    def createResumeModule(self, layout):
        group = QGroupBox('📋 履历修改器')
        group_layout = QVBoxLayout()
        
        # 分类组
        categories = ['国际赛', '无限制级', '限制级']
        
        self.resume_controls = {}
        
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
        
        # 初始更新统计
        self.updateResumeStats()
        
        group_layout.addLayout(global_buttons)
        group_layout.addWidget(self.resume_count_label)
        group.setLayout(group_layout)
        layout.addWidget(group)
    
    def createStatusModule(self, layout):
        group = QGroupBox('📊 系统状态')
        group_layout = QGridLayout()
        
        status_items = [
            ('修改器状态:', '就绪'),
            ('当前模式:', '正常模式'),
            ('最后操作:', '无'),
            ('系统时间:', '')
        ]
        
        self.status_labels = {}
        
        for i, (label, value) in enumerate(status_items):
            group_layout.addWidget(QLabel(label), i, 0)
            status_label = QLabel(value)
            status_label.setStyleSheet('font-weight: bold;')
            group_layout.addWidget(status_label, i, 1)
            self.status_labels[label] = status_label
        
        group.setLayout(group_layout)
        layout.addWidget(group)
    
    def initData(self):
        # 初始化数据
        self.speech_time = 0
        self.question_time = 0
        self.favor_value = 50
        
        # 实时刷新定时器
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.updateVoteDisplay)
        
        # 履历数据初始化
        self.resume_data = {}
        categories = ['国际赛', '无限制级', '限制级']
        for category in categories:
            # 0:不含佳辩和全程的条数, 1:含佳辩的条数, 2:含全程最佳辩手的条数
            self.resume_data[category] = [0, 0, 0]
    
    def initConnections(self):
        # 时间模块连接
        self.add_speech_10.clicked.connect(lambda: self.addTime('speech', 10))
        self.add_speech_999.clicked.connect(lambda: self.addTime('speech', 999))
        self.reset_speech.clicked.connect(lambda: self.resetTime('speech'))
        self.add_question_10.clicked.connect(lambda: self.addTime('question', 10))
        self.add_question_999.clicked.connect(lambda: self.addTime('question', 999))
        self.reset_question.clicked.connect(lambda: self.resetTime('question'))
        
        # 辩手选择器连接
        self.positive_button.clicked.connect(self.selectPositive)
        self.negative_button.clicked.connect(self.selectNegative)
        
        # 好感度模块连接
        self.favor_slider.valueChanged.connect(self.updateFavorFromSlider)
        self.favor_input.textChanged.connect(self.updateFavorFromInput)
        self.max_favor.clicked.connect(lambda: self.setFavor(100))
        self.clear_favor.clicked.connect(lambda: self.setFavor(0))
        self.add_favor_50.clicked.connect(lambda: self.addFavor(50))
        
        # 票型透视模块连接
        self.show_votes_btn.clicked.connect(self.showVotePerspective)
        self.refresh_checkbox.stateChanged.connect(self.toggleRefresh)
        
        # 无敌模式模块连接
        self.invincible_all.stateChanged.connect(self.toggleAllInvincible)
        self.enable_all.clicked.connect(self.enableAllInvincible)
        self.disable_all.clicked.connect(self.disableAllInvincible)
        
        # 履历修改器模块连接
        for category, data in self.resume_controls.items():
            # 加一按钮连接
            data['add_normal'].clicked.connect(lambda checked, cat=category: self.addResumeCount(cat, 0))
            data['add_excellent'].clicked.connect(lambda checked, cat=category: self.addResumeCount(cat, 1))
            data['add_full'].clicked.connect(lambda checked, cat=category: self.addResumeCount(cat, 2))
        
        self.clear_resume.clicked.connect(self.clearResumeStats)
    
    # 时间模块方法
    def addTime(self, time_type, seconds):
        if time_type == 'speech':
            self.speech_time += seconds
            self.speech_time_label.setText(str(self.speech_time))
        else:
            self.question_time += seconds
            self.question_time_label.setText(str(self.question_time))
        self.updateStatus('最后操作:', f'增加{time_type}时间 {seconds}秒')
    
    def resetTime(self, time_type):
        if time_type == 'speech':
            self.speech_time = 0
            self.speech_time_label.setText('0')
        else:
            self.question_time = 0
            self.question_time_label.setText('0')
        self.updateStatus('最后操作:', f'重置{time_type}时间')
    
    # 好感度模块方法
    def updateFavorFromSlider(self):
        self.favor_value = self.favor_slider.value()
        self.favor_input.setText(str(self.favor_value))
        self.favor_value_label.setText(f'当前好感度: {self.favor_value}')
        self.updateStatus('最后操作:', '调整好感度滑块')
    
    def updateFavorFromInput(self):
        try:
            value = int(self.favor_input.text())
            if 0 <= value <= 100:
                self.favor_value = value
                self.favor_slider.setValue(value)
                self.favor_value_label.setText(f'当前好感度: {self.favor_value}')
        except:
            pass
    
    def setFavor(self, value):
        self.favor_value = value
        self.favor_slider.setValue(value)
        self.favor_input.setText(str(value))
        self.favor_value_label.setText(f'当前好感度: {self.favor_value}')
        self.updateStatus('最后操作:', f'设置好感度为 {value}')
    
    def addFavor(self, value):
        self.setFavor(min(100, self.favor_value + value))
    
    # 票型透视模块方法
    def showVotePerspective(self):
        self.updateVoteDisplay()
        self.updateStatus('最后操作:', '开启票型透视')
    
    def updateVoteDisplay(self):
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
    
    def toggleRefresh(self, state):
        if state == Qt.Checked:
            self.refresh_timer.start(2000)  # 2秒刷新一次
            self.updateStatus('最后操作:', '开启票型实时刷新')
        else:
            self.refresh_timer.stop()
            self.updateStatus('最后操作:', '关闭票型实时刷新')
    
    # 辩手选择器方法
    def selectPositive(self):
        """选择正方"""
        self.positive_button.setStyleSheet('background-color: #00ff00; color: #000000; border-color: #00ff00;')
        self.negative_button.setStyleSheet('background-color: #555; color: #ffffff; border-color: #555;')
        self.updateStatus('最后操作:', '选择正方')
    
    def selectNegative(self):
        """选择反方"""
        self.negative_button.setStyleSheet('background-color: #ff0000; color: #ffffff; border-color: #ff0000;')
        self.positive_button.setStyleSheet('background-color: #555; color: #ffffff; border-color: #555;')
        self.updateStatus('最后操作:', '选择反方')
    
    # 无敌模式模块方法
    def toggleAllInvincible(self, state):
        checked = (state == Qt.Checked)
        self.invincible_speech.setChecked(checked)
        self.invincible_summary.setChecked(checked)
        self.invincible_question.setChecked(checked)
        
    def enableAllInvincible(self):
        self.invincible_speech.setChecked(True)
        self.invincible_summary.setChecked(True)
        self.invincible_question.setChecked(True)
        self.invincible_all.setChecked(True)
        self.updateStatus('最后操作:', '开启全无敌模式')
    
    def disableAllInvincible(self):
        self.invincible_speech.setChecked(False)
        self.invincible_summary.setChecked(False)
        self.invincible_question.setChecked(False)
        self.invincible_all.setChecked(False)
        self.updateStatus('最后操作:', '关闭全无敌模式')
    
    # 履历修改器模块方法
    def addResumeCount(self, category, index):
        """增加履历数据的特定类型计数"""
        if category in self.resume_data and 0 <= index < len(self.resume_data[category]):
            self.resume_data[category][index] += 1
            self.updateResumeStats()
            self.updateStatus('最后操作:', f'{category}增加履历 +1')
    
    def updateResumeStats(self):
        """更新履历统计显示"""
        total = 0
        
        # 格式化显示统计结果
        status_text = ''
        for category, counts in self.resume_data.items():
            category_total = sum(counts)
            total += category_total
            # 使用+符号连接三个数字
            status_text += f'{category}: {counts[0]}+{counts[1]}+{counts[2]} (共{category_total})\n'
        
        status_text += f'\n总履历条数: {total}'
        
        self.resume_count_label.setText(status_text.strip())
        
        # 检查彩蛋触发条件：无限制级或国际赛达到10+5+1或以上
        for category in ['国际赛', '无限制级']:
            counts = self.resume_data[category]
            if counts[0] >= 10 and counts[1] >= 5 and counts[2] >= 1:
                # 触发彩蛋
                self.triggerEasterEgg()
                break
    
    def clearResumeStats(self):
        """清空所有履历数据"""
        for category in self.resume_data:
            self.resume_data[category] = [0, 0, 0]
        self.updateResumeStats()
        self.updateStatus('最后操作:', '清空所有履历数据')
    
    # 状态更新方法
    def updateStatus(self, label, value):
        if label in self.status_labels:
            self.status_labels[label].setText(value)
    
    def triggerEasterEgg(self):
        """触发彩蛋"""
        # 创建彩蛋弹窗
        dialog = EasterEggDialog(self)
        dialog.exec_()

class EasterEggDialog(QDialog):
    """彩蛋弹窗类"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('🎉 恭喜你达成10+5+1成就！')
        self.resize(600, 400)
        self.setStyleSheet("background-color: #282830;")
        
        # 布局
        main_layout = QVBoxLayout(self)
        
        # 标题
        title_label = QLabel('🎉 恭喜你达成10+5+1成就！🎉')
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
        try:
            # 尝试播放音乐文件
            # 使用QSoundEffect替代QSound，提供更好的兼容性
            import sys
            import os
            from PyQt5.QtMultimedia import QSoundEffect
            from PyQt5.QtCore import QUrl
            
            # 获取程序运行目录
            if hasattr(sys, '_MEIPASS'):
                # 如果是打包后的exe文件
                base_path = sys._MEIPASS
            else:
                # 如果是直接运行的Python脚本
                base_path = os.path.abspath('.')
            
            # 优先使用用户提供的音乐文件，然后是默认文件名
            music_files = ["M800004Wxqxk3oWPnp.mp3", "celebration.wav", "celebration.mp3"]
            music_played = False
            
            for file in music_files:
                try:
                    # 构建完整的文件路径
                    file_path = os.path.join(base_path, file)
                    sound_effect = QSoundEffect()
                    sound_effect.setSource(QUrl.fromLocalFile(file_path))
                    sound_effect.setVolume(0.5)  # 设置音量为50%
                    sound_effect.play()
                    music_played = True
                    break
                except Exception:
                    continue
            
            if not music_played:
                # 如果没有找到音乐文件，打印提示信息
                print("未找到庆祝音乐文件，请确保M800004Wxqxk3oWPnp.mp3与程序放在同一目录")
        except Exception as e:
            # 如果发生其他错误，不影响程序运行
            print(f"播放音乐时发生错误: {e}")
    
    def submitName(self):
        """提交用户名并显示恭喜信息"""
        name = self.name_input.text().strip()
        if not name:
            name = '辩手'
        
        message = f'恭喜你伟大的{name}你已经成为无敌的10+5+1！'
        self.message_label.setText(message)
        
        # 禁用输入框和按钮
        self.name_input.setEnabled(False)
        self.sender().setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DebateHacker()
    window.show()
    sys.exit(app.exec_())