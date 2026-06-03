#!/usr/bin/env python3
"""
Simple HTTP server for previewing the stellar-flow animation
with validation checks
"""
import http.server
import socketserver
import os

PORT = 9500
DIRECTORY = "/workspace"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        # Log the request
        print(f"📥 Request: {self.path}")
        super().do_GET()
    
    def end_headers(self):
        # Add CORS headers for p5.js CDN
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)
    
    print("=" * 60)
    print("🌟 星河流淌 - 动画预览服务器")
    print("=" * 60)
    print()
    print(f"📂 服务目录: {DIRECTORY}")
    print(f"🌐 访问地址: http://localhost:{PORT}")
    print(f"🎨 动画文件: http://localhost:{PORT}/stellar-flow.html")
    print()
    print("=" * 60)
    print("📋 验证检查:")
    print("=" * 60)
    
    # Check file existence
    html_file = os.path.join(DIRECTORY, "stellar-flow.html")
    if os.path.exists(html_file):
        size = os.path.getsize(html_file)
        print(f"✅ stellar-flow.html 存在 ({size} bytes)")
        
        # Check for key components
        with open(html_file, 'r') as f:
            content = f.read()
            
        checks = [
            ("p5.js CDN", "cdnjs.cloudflare.com/ajax/libs/p5.js" in content),
            ("Canvas 容器", "canvas-container" in content),
            ("Particle 类", "class Particle" in content),
            ("setup() 函数", "function setup()" in content),
            ("draw() 函数", "function draw()" in content),
            ("Seed 控制", "seed-input" in content),
            ("参数控制", "particleCount" in content and "flowSpeed" in content),
            ("色彩控制", "colorPalette" in content),
            ("下载功能", "downloadCanvas" in content),
        ]
        
        for name, result in checks:
            status = "✅" if result else "❌"
            print(f"{status} {name}")
        
        print()
        print("=" * 60)
        print("🚀 启动服务器中...")
        print("=" * 60)
        
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"✨ 服务器已启动！")
            print(f"🎨 请在浏览器中打开: http://localhost:{PORT}/stellar-flow.html")
            print(f"📖 按 Ctrl+C 停止服务器")
            print()
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n\n👋 服务器已停止")
    else:
        print(f"❌ stellar-flow.html 不存在于 {DIRECTORY}")
        return

if __name__ == "__main__":
    main()
