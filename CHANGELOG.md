# 更新日志

## 2025-12-29

### ✨ 新功能
- 优化打包配置，运行时不再显示命令行窗口

### 🔧 修复
- 解决了 `vote_module.py` 中 `QHBoxLayout` 导入问题
- 修复了 `InvincibleModule` 中 `mode_changed` 信号名错误（改为 `mode_toggled`）

### 📦 打包优化
- 配置PyInstaller，确保音乐文件 `M800004Wxqxk3oWPnp.mp3` 正确打包
- 使用 `console=False` 参数隐藏命令行窗口

### 🧹 清理
- 删除了不再需要的 `cleanup.py` 清理脚本
- 精简了工作目录结构

### 📄 文档
- 更新了项目文档，包括使用说明和功能介绍
