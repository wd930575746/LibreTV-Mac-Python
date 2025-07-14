---

# Jeffern影视平台 MAC端

Jeffern影视平台是一个基于 Python + PyWebview 的桌面端影视聚合浏览器，支持自定义视频源，界面美观，操作简单。  
主要是为https://github.com/jeffernn/LibreTV此项目制作（本人并未此项目相关人员，此软件仅为本人自用播放器）
下方为软件主要界面截图：

## 软件截图

设置页：
<img width="1126" height="715" alt="image" src="https://github.com/user-attachments/assets/c240d0b2-ec7e-40b4-b8b2-9bd0a0044f17" />



主界面：
<img width="1296" height="843" alt="image" src="https://github.com/user-attachments/assets/077ee0eb-0b43-4252-ad54-802d8642b07f" />



---

## 功能简介

- 支持自定义视频源网址（如B站、豆瓣等）
- 影视聚合浏览与搜索
- 简洁美观的UI界面
- 一键恢复出厂设置

---

## 依赖的第三方包

本项目主要依赖以下第三方库：

- [pywebview](https://github.com/r0x0r/pywebview)  
  用于创建原生桌面窗口并嵌入网页内容。

安装依赖：

```bash
pip install pywebview
```

---

## 运行方式

直接运行主程序：

```bash
python mac-web.py
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

3. 打包完成后，在 `dist` 目录下会生成可执行文件。

---

## 配置文件说明

- 配置文件路径：`~/.mac_web_app_config.json`
- 用于保存自定义视频源网址

---

## 其他说明

- 本项目仅供学习与交流，禁止用于任何商业用途。
- 如有问题或建议，欢迎提交 Issue。

---
