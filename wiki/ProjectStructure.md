# 项目结构

## 1. 目录结构

```
dibetexiugaiq/
├── debate_hacker.py     # 主应用程序文件
├── debate_hacker.spec   # PyInstaller构建配置文件
├── .gitignore          # Git忽略文件列表
├── README.md           # 项目说明文档
├── CHANGELOG.md        # 更新日志文件
├── LICENSE             # MIT许可证文件
├── VERSIONING.md       # 版本号命名规则文件
├── M800004Wxqxk3oWPnp.mp3  # 彩蛋音效文件
├── wiki/               # Wiki文档目录
│   ├── UsageGuide.md   # 使用指南
│   ├── FAQ.md          # 常见问题解答
│   └── ProjectStructure.md  # 项目结构文档
├── modules/            # 功能模块目录
│   ├── debater_selector.py  # 辩手选择模块
│   ├── easter_egg_module.py  # 彩蛋模块
│   ├── favor_module.py  # 好感度模块
│   ├── invincible_module.py  # 无敌模式模块
│   ├── listening_module.py  # 听感模块
│   ├── resume_module.py  # 履历模块
│   ├── status_module.py  # 状态模块
│   ├── time_module.py  # 时间模块
│   └── vote_module.py  # 票型模块
├── utils/              # 工具类目录
│   ├── constants.py    # 常量定义
│   ├── logger.py       # 日志工具
│   └── ui_utils.py     # UI工具
├── test_*.py           # 测试文件
├── build/              # PyInstaller构建目录
├── dist/               # 生成的可执行文件目录
└── v1.2.2/             # 版本归档目录
```

## 2. 文件说明

### 2.1 核心文件

#### debate_hacker.py
主应用程序文件，包含应用程序的主框架和主要逻辑：
- 界面设计与布局
- 各模块的集成与协调
- 事件处理与信号连接
- 彩蛋触发逻辑

#### debate_hacker.spec
PyInstaller构建配置文件，用于生成可执行文件：
- 指定入口点
- 配置打包选项
- 设置资源文件（包括音效文件）

#### CHANGELOG.md
更新日志文件，记录项目的所有版本更新：
- 版本号
- 更新日期
- 新增功能
- 修复问题
- 打包优化

#### VERSIONING.md
版本号命名规则文件，定义项目的版本号管理规范：
- 版本号核心结构
- 状态标识规范
- 版本递增规则
- 版本命名示例

#### M800004Wxqxk3oWPnp.mp3
彩蛋功能的音效文件，用于在彩蛋触发时播放。

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

### 2.4 模块目录

#### modules/
功能模块目录，包含应用程序的所有功能模块：

##### debater_selector.py
辩手选择模块，用于选择辩手阵营和姓名。

##### easter_egg_module.py
彩蛋模块，包含彩蛋对话框的实现和音效播放功能。

##### favor_module.py
评委好感度模块，实现好感度的调整和状态显示。

##### invincible_module.py
无敌模式模块，实现无敌申论、结辩和质询功能。

##### listening_module.py
评委听感模块，实现漏听对方内容和提升我方内容功能。

##### resume_module.py
履历修改器模块，实现履历数据的管理和统计。

##### status_module.py
状态模块，用于管理和显示应用程序的状态信息。

##### time_module.py
时间调整模块，实现陈词时间和质询时间的调整功能。

##### vote_module.py
票型透视模块，实现三位评委投票的显示和统计。

#### utils/
工具类目录，包含应用程序的通用工具：

##### constants.py
常量定义文件，包含应用程序中使用的所有常量。

##### logger.py
日志工具，实现应用程序的日志记录功能。

##### ui_utils.py
UI工具，提供UI相关的通用功能和组件。

### 2.5 测试文件

测试文件目录，包含应用程序的测试代码：
- `test_easter_egg.py`：彩蛋功能测试
- `test_debate_hacker_easter_egg.py`：主程序彩蛋测试
- `test_easter_egg_threshold.py`：彩蛋触发条件测试

### 2.6 构建目录

#### build/
PyInstaller构建过程中生成的临时文件目录，包含：
- 编译后的Python文件
- 依赖库
- 资源文件

#### dist/
PyInstaller生成的可执行文件目录，包含最终的`debate_hacker.exe`文件。

#### v1.2.2/
版本归档目录，用于存放特定版本的可执行文件和相关资源。

## 3. 代码结构

### 3.1 主类

#### DebateHacker(QMainWindow)
主应用程序类，继承自PyQt5的QMainWindow，包含：
- 数据初始化方法
- UI初始化方法
- 事件连接方法
- 各功能模块的集成

### 3.2 核心方法

#### 初始化方法
- `__init__()`: 初始化应用程序
- `initData()`: 初始化应用数据
- `initUI()`: 初始化用户界面
- `initConnections()`: 连接模块间的信号与槽

#### 模块管理方法
- 各功能模块的实例化和集成
- 模块间通信的处理

#### 事件处理方法
- `onResumeChanged()`: 处理履历更新事件（包含彩蛋触发逻辑）
- `onFavorChanged()`: 处理好感度变化事件
- `onVotesUpdated()`: 处理票型更新事件
- `onTimeChanged()`: 处理时间变化事件

#### 彩蛋功能方法
- `onResumeChanged()`: 监听履历变化，检查彩蛋触发条件
- `triggerEasterEgg()`: 触发彩蛋对话框

#### 状态管理方法
- `updateStatus()`: 更新状态栏信息

### 3.3 模块间通信

采用PyQt5的信号与槽机制实现模块间通信：
- 各模块定义自己的信号
- 主程序连接信号与处理槽
- 实现松耦合的模块架构

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