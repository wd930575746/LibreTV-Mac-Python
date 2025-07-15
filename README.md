---

# Jeffern影视平台（LibreTV） MAC端 -（Python版）

Jeffern影视平台是一个基于 **Python + PyWebview** 的桌面端影视封装软件，支持自定义视频源，界面美观，操作简单。  
软件主要为 [LibreTV](https://github.com/jeffernn/LibreTV) 项目制作（本人并非引用项目相关制作人员，制作本软件的初心是方便本人使用）

---

## 软件截图

**设置页：**  
<img width="560" alt="设置页" src="https://github.com/user-attachments/assets/c240d0b2-ec7e-40b4-b8b2-9bd0a0044f17" />

**主界面：**  
<img width="650" alt="主界面" src="https://github.com/user-attachments/assets/077ee0eb-0b43-4252-ad54-802d8642b07f" />

---

## 功能简介

- 支持自定义视频源网址（如LibreTV,B站、豆瓣等）
- 影视聚合浏览与搜索（基于视频网站的功能实现）
- 恢复默认设置（即重新封装影视网站，点击主界面下方居中位置透明色的按钮）
---

## 依赖的第三方包

本项目主要依赖以下第三方库：

- [pywebview](https://github.com/r0x0r/pywebview)  
  用于创建原生桌面窗口并嵌入网页内容。

相关依赖：

```bash
pip install pywebview
```

---

## 打包为独立应用

推荐使用 [PyInstaller](https://www.pyinstaller.org/) 进行打包：

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
4. 可使用github action自动打包（打包后的为通用类型即M芯片与Intel均可运行，打包后运行.app结尾应用，其他文件均可删除）。
---

## 配置文件说明

- 配置文件路径：`~/.mac_web_app_config.json`（默认情况下隐藏显示）
- 用于保存自定义视频源网址（首次输入的网站地址）

---

## 其他说明

- 本项目仅供学习与交流，禁止用于任何商业用途。
- 如有问题或建议，欢迎提交 Issue。
- 若要分支项目请引用本项目为出处，喜欢的话欢迎给个Star～
- 目前软件有两个小BUG欢迎大佬fork修复（无法保存网站的cookies缓存和全屏后右侧滑动条无法自动隐藏）
- 目前已经修复两个已知BUG，请移步https://github.com/jeffernn/LibreTV-Mac-Objective-C
---
