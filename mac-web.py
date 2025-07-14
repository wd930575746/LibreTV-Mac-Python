import webview
import os
import json
import sys

CONFIG_FILE = os.path.expanduser('~/.mac_web_app_config.json')

# 用于与前端交互的API类
class Api:
    def get_url(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                data = json.load(f)
                return data.get('url')
        return None

    def set_url(self, url):
        if not url.startswith('http'):
            return {'success': False, 'msg': '请输入有效的网址（以http或https开头）'}
        with open(CONFIG_FILE, 'w') as f:
            json.dump({'url': url}, f)
        restart_app()
        return {'success': True}

    def reset_config(self):
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        restart_app()
        return {'success': True}

    def restart_to_setting(self):
        # 先删除配置文件，再重启应用
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        restart_app()
        return {'success': True}

    def open_url(self, url):
        if not url.startswith('http'):
            return {'success': False, 'msg': '请输入有效的网址（以http或https开头）'}
        with open(CONFIG_FILE, 'w') as f:
            json.dump({'url': url}, f)
        restart_app()
        return {'success': True}

# HTML模板
HTML = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Jeffern影视设置页</title>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'PingFang SC', Arial, sans-serif;
        }
        body {
            background-color: #f0f4f8;
            background-image: url('http://img.netbian.com/file/2024/0614/003651lvurh.jpg');
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #333;
        }
        .container {
            background: rgba(255,255,255,0.92);
            border-radius: 24px;
            box-shadow: 0 8px 32px rgba(44,62,80,0.13);
            padding: 72px 80px 64px 80px;
            min-width: 700px;
            display: flex;
            flex-direction: column;
            align-items: center;
            backdrop-filter: blur(18px);
            max-width: 90vw;
        }
        h2 {
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 38px;
            color: #2c3e50;
            letter-spacing: 1px;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.7);
        }
        input[type=text] {
            width: 440px;
            padding: 18px 24px;
            font-size: 1.15rem;
            border: 1.5px solid #ccc;
            border-radius: 10px;
            margin-bottom: 32px;
            outline: none;
            transition: border 0.2s, box-shadow 0.2s;
            background: #fff;
            box-shadow: 0 2px 8px rgba(44,62,80,0.06);
        }
        input[type=text]:focus {
            border: 1.5px solid #2980b9;
            box-shadow: 0 0 0 3px rgba(41,128,185,0.13);
        }
        .btn-main {
            background: #2980b9;
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 16px 56px;
            font-size: 1.15rem;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.2s, box-shadow 0.2s, transform 0.2s;
            box-shadow: 0 4px 10px rgba(44,62,80,0.10);
            margin-bottom: 0;
        }
        .btn-main:hover {
            background: #1c5980;
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(44,62,80,0.15);
        }
        .msg {
            color: #e53935;
            margin-top: 22px;
            min-height: 24px;
            font-size: 1.08rem;
        }
        @media (max-width: 900px) {
            .container { min-width: 90vw; padding: 32px 10vw; }
            input[type=text] { width: 80vw; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>⬇视频网址⬇</h2>
        <input id="url" type="text" placeholder="如 https://www.bilibili.com" />
        <button class="btn-main" onclick="setUrl()">起飞</button>
        <div class="msg" id="msg"></div>
    </div>
    <script>
        async function setUrl() {
            const url = document.getElementById('url').value.trim();
            const res = await window.pywebview.api.open_url(url);
            if (!res.success) {
                document.getElementById('msg').innerText = res.msg;
            }
        }
        window.onload = async function() {
            const url = await window.pywebview.api.get_url();
            if (url) {
                window.location.href = url;
            }
        }
    </script>
</body>
</html>
'''

def restart_app():
    python = sys.executable
    os.execv(python, [python] + sys.argv)

if __name__ == '__main__':
    api = Api()
    url = api.get_url()
    user_data_dir = os.path.expanduser('~/.mac_web_app_webview_data')
    if url:
        def on_loaded(window):
            js = '''
                if (!document.getElementById('resetBtn')) {
                    let btn = document.createElement('button');
                    btn.id = 'resetBtn';
                    btn.title = '恢复出厂设置';
                    btn.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1976d2" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 1 9 9"/><polyline points="3 7 3 12 8 12"/></svg>`;
                    btn.style.position = 'fixed';
                    btn.style.left = '50%';
                    btn.style.bottom = '32px';
                    btn.style.transform = 'translateX(-50%)';
                    btn.style.zIndex = 99999;
                    btn.style.background = 'rgba(255,255,255,0.18)';
                    btn.style.border = 'none';
                    btn.style.borderRadius = '24px';
                    btn.style.padding = '10px 16px';
                    btn.style.boxShadow = '0 2px 12px rgba(0,0,0,0.08)';
                    btn.style.backdropFilter = 'blur(6px)';
                    btn.style.cursor = 'pointer';
                    btn.style.transition = 'all 0.2s';
                    btn.onmouseenter = function() {
                        btn.style.background = 'rgba(255,255,255,0.32)';
                    };
                    btn.onmouseleave = function() {
                        btn.style.background = 'rgba(255,255,255,0.18)';
                    };
                    btn.onclick = function() { window.pywebview.api.restart_to_setting(); };
                    document.body.appendChild(btn);
                }
            '''
            try:
                window.evaluate_js(js)
            except:
                pass
        window = webview.create_window('Jeffern影视平台', url, width=1200, height=800, js_api=api)
        webview.start(on_loaded, window)
    else:
        window = webview.create_window('Jeffern影视设置页', html=HTML, width=1100, height=700, js_api=api, resizable=False)
        webview.start()
