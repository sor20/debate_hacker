# 项目结构

## 1. 目录结构

```
dibetexiugaiq/
├── debate_hacker.py     # 主应用程序文件
├── debate_hacker.spec   # PyInstaller构建配置文件
├── .gitignore          # Git忽略文件列表
├── README.md           # 项目说明文档
├── LICENSE             # MIT许可证文件
├── wiki/               # Wiki文档目录
│   ├── UsageGuide.md   # 使用指南
│   ├── FAQ.md          # 常见问题解答
│   └── ProjectStructure.md  # 项目结构文档
├── build/              # PyInstaller构建目录
└── dist/               # 生成的可执行文件目录
```

## 2. 文件说明

### 2.1 核心文件

#### debate_hacker.py
主应用程序文件，包含所有功能的实现：
- 界面设计与布局
- 时间调整模块
- 评委好感度模块
- 票型透视模块
- 无敌模式模块
- 履历修改器模块
- 数据处理与存储

#### debate_hacker.spec
PyInstaller构建配置文件，用于生成可执行文件：
- 指定入口点
- 配置打包选项
- 设置资源文件

### 2.2 文档文件

#### .gitignore
Git版本控制忽略文件列表，包含：
- Python编译文件
- 构建产物
- 测试文件
- 日志文件
- 环境配置文件

#### README.md
项目说明文档，包含：
- 项目简介
- 功能特性
- 安装要求
- 使用方法
- 界面说明
- 票型计算规则
- 项目结构

#### LICENSE
MIT许可证文件，定义了项目的使用权限和限制。

### 2.3 Wiki文档

#### UsageGuide.md
详细的使用指南，包含：
- 快速开始
- 功能详解
- 高级功能
- 常见问题
- 更新日志

#### FAQ.md
常见问题解答，包含：
- 基本问题
- 安装与运行
- 功能使用
- 技术问题
- 法律与道德
- 联系与支持

#### ProjectStructure.md
项目结构文档，即当前文件，详细说明了项目的目录结构和文件作用。

### 2.4 构建目录

#### build/
PyInstaller构建过程中生成的临时文件目录，包含：
- 编译后的Python文件
- 依赖库
- 资源文件

#### dist/
PyInstaller生成的可执行文件目录，包含最终的`debate_hacker.exe`文件。

## 3. 代码结构

### 3.1 主类

#### DebateHacker(QMainWindow)
主应用程序类，继承自PyQt5的QMainWindow，包含：
- 数据初始化方法
- UI初始化方法
- 事件连接方法
- 各功能模块的实现方法

### 3.2 核心方法

#### 初始化方法
- `__init__()`: 初始化应用
- `initData()`: 初始化数据
- `initUI()`: 初始化界面
- `initConnections()`: 连接事件

#### 时间调整方法
- `addSpeechTime()`: 增加陈词时间
- `addQuestionTime()`: 增加质询时间
- `updateTimeDisplay()`: 更新时间显示

#### 好感度方法
- `setFavor()`: 设置好感度
- `addFavor()`: 增加好感度

#### 票型透视方法
- `showVotePerspective()`: 显示票型透视
- `updateVoteDisplay()`: 更新投票显示
- `judgeWinner()`: 判定赢家

#### 无敌模式方法
- `toggleAllModes()`: 切换所有无敌模式

#### 履历修改器方法
- `addResume()`: 增加履历
- `updateResumeDisplay()`: 更新履历显示
- `updateResumeStats()`: 更新履历统计

## 4. 依赖关系

### 4.1 Python库
- `sys`: 系统功能
- `random`: 随机数生成
- `PyQt5`: GUI框架
  - `QtWidgets`: 界面组件
  - `QtCore`: 核心功能
  - `QtGui`: 图形功能

### 4.2 外部工具
- `PyInstaller`: 打包工具，用于生成EXE文件

## 5. 构建流程

1. 安装依赖: `pip install pyqt5 pyinstaller`
2. 构建EXE文件: `pyinstaller --onefile --windowed debate_hacker.py`
3. 在dist目录中找到生成的debate_hacker.exe文件

## 6. 开发规范

### 6.1 编码风格
- 使用4个空格缩进
- 遵循PEP8编码规范
- 变量名使用小写字母和下划线
- 方法名使用小写字母和下划线
- 类名使用驼峰命名法

### 6.2 文档规范
- 每个方法添加文档字符串
- 复杂逻辑添加注释
- 更新README.md和Wiki文档

### 6.3 版本控制
- 使用Git进行版本控制
- 提交信息简洁明了
- 定期更新版本号

## 7. 贡献指南

1. Fork项目仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 8. 联系方式

如有问题或建议，请通过GitHub Issues提交反馈。