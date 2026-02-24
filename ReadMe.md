🚀 MATLAB Vibe Coding 1-Click Installer
English | 中文说明

An automated setup tool to seamlessly integrate MATLAB with Claude Desktop via the Model Context Protocol (MCP). Escape the dependency hell and start AI-powered engineering and "Vibe Coding" in minutes!

🇬🇧 English
💡 What is this?
Setting up the official MathWorks MCP server requires manual cloning, building Node.js packages, binding Python engines, and safely editing hidden JSON configurations. This script automates the entire pipeline for Windows users.

With a single click, it:

Auto-locates your newest MATLAB installation.

Installs the MATLAB Engine API for Python.

Clones and builds the matlab-mcp-server.

Safely backs up and injects the configuration into Claude Desktop.

📋 Prerequisites
Before running the installer, ensure you have the following installed and added to your system PATH:

MATLAB (R2024b or newer recommended)

Node.js & npm (v18 or newer)

Git

🚀 Quick Start
Option A: The Easy Way (For general users)
Go to the Releases page and download setup_matlab_vibe.exe.

Right-click the .exe file and select "Run as administrator".

Wait for the green ✅ checkmarks to complete.

Completely restart Claude Desktop.

Look for the 🔨 (hammer/tool) icon in your Claude chat window!

Option B: For Developers (Run from source)
If you prefer to run the Python script directly:
git clone https://github.com/bitsym/MATLAB-Vibe-Installer.git
cd MATLAB-Vibe-Installer
python setup_matlab_vibe.py
🛡️ Troubleshooting
Error: Permission Denied: The script modifies files in C:\Program Files\MATLAB\.... You MUST run it as an Administrator.

Antivirus Warning: Executables compiled with PyInstaller might trigger false positives. Please allow it through your antivirus or run the Python script directly.

No Hammer Icon in Claude: Ensure you completely closed Claude Desktop (check your system tray/taskbar) and restarted it. Check your %APPDATA%\Claude\claude_desktop_config.json to ensure the syntax is correct.

🇨🇳 中文说明
💡 简介
配置官方的 MathWorks MCP 服务器需要经历繁琐的步骤：克隆源码、编译 Node 项目、绑定 Python 引擎、修改隐藏的 JSON 配置文件。这个工具专为 Windows 用户设计，将所有流程自动化，帮你彻底告别“依赖地狱”。

它会自动完成：

自动寻找本机最新的 MATLAB 安装路径。

安装 MATLAB 引擎 Python 接口。

自动下载并编译 matlab-mcp-server。

安全备份并向 Claude Desktop 注入 JSON 配置。

📋 环境要求
在运行本工具前，请确保你的电脑已安装以下软件，并配置了系统环境变量：

MATLAB (建议 R2024b 及以上版本)

Node.js 与 npm (v18 及以上)

Git

🚀 使用方法
方案 A：小白专属（一键运行）
前往右侧的 Releases 页面，下载 setup_matlab_vibe.exe。

右键点击该文件，选择“以管理员身份运行”。

等待黑框中所有的步骤执行完毕（亮起绿色的 ✅）。

彻底关闭并重启 Claude Desktop。

在对话框中看到 🔨 (小锤子) 图标，即可开始你的 Vibe Coding！

方案 B：极客/开发者（运行源码）
如果你懂 Python，可以直接运行源码：

Bash
git clone https://github.com/bitsym/MATLAB-Vibe-Installer.git
cd MATLAB-Vibe-Installer
python setup_matlab_vibe.py
🛡️ 避坑指南
拒绝访问 / 权限报错：脚本需要读写 C:\Program Files 下的 MATLAB 目录。请务必以管理员身份运行。

杀毒软件报毒：由于使用了 PyInstaller 打包为单文件，部分杀毒软件（如 360 或 Windows Defender）可能会产生误报。请放心添加信任，或直接运行 Python 源码。

Claude 里没有出现小锤子：请确保你在右下角托盘处彻底退出了 Claude。如果依然没有，请按 Win+R 输入 %APPDATA%\Claude，检查 claude_desktop_config.json 文件的格式是否正确。

Disclaimer: This is an unofficial community tool. MATLAB is a registered trademark of The MathWorks, Inc.
