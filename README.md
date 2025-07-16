---

# Jeffern影视平台（LibreTV） MAC端 -（Python版）
- 欢迎访问本项目，请优先移步到[Objective-C版本 - MAC端](https://github.com/jeffernn/LibreTV-Mac-Objective-C) 此版本修复所有已知BUG极其优化运行效率。
- 安卓端、windows端、TV端的部署可参考本版本后自行修改及其打包后使用，Python是一门跨平台的语言，效率虽不高但编程简单及有极强的跨平台性。
- Jeffern影视平台是一个基于 **Python + PyWebview** 的桌面端影视封装软件，支持自定义视频源。  
- 软件主要为 [LibreTV](https://github.com/jeffernn/LibreTV) 项目制作（本人并非引用项目相关制作人员，制作本软件的初心是方便本人使用）

---

## 软件截图

**设置页：**  
<img width="560" alt="设置页" src="https://github.com/user-attachments/assets/c240d0b2-ec7e-40b4-b8b2-9bd0a0044f17" />

**主界面：**  
<img width="650" alt="主界面" src="https://github.com/user-attachments/assets/077ee0eb-0b43-4252-ad54-802d8642b07f" />

---

## 功能简介

- 🚀 支持自定义视频源网址（已完美支持LibreTV，其他平台自行测试）
- 🚀 恢复默认设置（即重新封装影视网站，点击主界面下方居中位置透明色的按钮）
- 🚀 开箱即用: 无需复杂的部署过程，直接下载安装包即可使用，告别配置烦恼。
- 🔐 开源与安全: 项目完全开源，代码透明，无任何跟踪或广告
---

## 依赖的第三方包

相关依赖：

```bash
pip install pywebview
```

---

## 打包为独立应用

- 推荐使用 [PyInstaller](https://www.pyinstaller.org/) 进行打包：

1. 安装 PyInstaller：

   ```bash
   pip install pyinstaller
   ```

2. 打包命令（以 macOS 为例）：

   ```bash
   pyinstaller --noconfirm --onefile --windowed --name "Jeffern影视平台" mac-web.py
   ```

   - `--onefile`：打包为单一可执行文件
   - `--windowed`：不显示命令行窗口（适用于GUI应用）
   - `--name`：指定应用名称

3. 打包完成后，在 `dist` 目录下会生成可执行文件（.app结尾）。
- 可使用github action自动打包（打包后的为通用类型即M芯片与Intel均可运行，打包后运行.app结尾应用，其他文件均可删除）。
---

## 配置文件说明

- 配置文件路径：`~/.mac_web_app_config.json`（默认情况下隐藏显示）
- 用于保存自定义视频源网址（首次输入的网站地址）

---

## 其他说明

- 本项目仅供学习与交流，禁止用于任何商业用途。
- 如有问题或建议，欢迎提交 Issue。
- 若要分支项目请引用本项目为出处。
- 喜欢的话欢迎 Star🌟🌟🌟 支持～
- 此版本在MAC端有两个小BUG，欢迎大佬fork修复（无法保存网站的cookies缓存和全屏后右侧滑动条无法自动隐藏）
- 目前已经修复两个已知BUG，请移步[Objective-C版本 - MAC端](https://github.com/jeffernn/LibreTV-Mac-Objective-C) 
---
