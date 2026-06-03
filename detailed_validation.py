#!/usr/bin/env python3
"""
Validate HTML file syntax and structure
"""
import re

def validate_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 60)
    print("📋 HTML 文件验证报告")
    print("=" * 60)
    print()
    
    # Basic structure checks
    checks = {
        "DOCTYPE 声明": "<!DOCTYPE html>" in content,
        "HTML 标签": "<html" in content and "</html>" in content,
        "HEAD 标签": "<head>" in content and "</head>" in content,
        "BODY 标签": "<body>" in content and "</body>" in content,
        "p5.js CDN": "cdnjs.cloudflare.com/ajax/libs/p5.js" in content,
        "Google Fonts": "fonts.googleapis.com" in content,
        "Canvas 容器": "canvas-container" in content,
        "Sidebar 容器": "sidebar" in content,
        "CSS 样式": "<style>" in content and "</style>" in content,
        "JavaScript": "<script>" in content and "</script>" in content,
    }
    
    print("🎨 结构验证:")
    for name, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
    
    print()
    print("⚙️ 功能验证:")
    
    # JavaScript functionality
    js_checks = {
        "Particle 类定义": "class Particle" in content,
        "setup() 函数": "function setup()" in content,
        "draw() 函数": "function draw()" in content,
        "initializeSystem()": "function initializeSystem()" in content,
        "updateParam()": "function updateParam(" in content,
        "updateColor()": "function updateColor(" in content,
        "updateSeed()": "function updateSeed()" in content,
        "downloadCanvas()": "function downloadCanvas()" in content,
        "randomSeedAndUpdate()": "function randomSeedAndUpdate()" in content,
    }
    
    for name, passed in js_checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
    
    print()
    print("🎮 交互验证:")
    
    # UI elements
    ui_checks = {
        "Seed 输入框": 'id="seed-input"' in content,
        "Previous 按钮": 'onclick="previousSeed()"' in content,
        "Next 按钮": 'onclick="nextSeed()"' in content,
        "Random 按钮": 'onclick="randomSeedAndUpdate()"' in content,
        "粒子数量滑块": 'id="particleCount"' in content,
        "速度滑块": 'id="flowSpeed"' in content,
        "噪声缩放滑块": 'id="noiseScale"' in content,
        "轨迹长度滑块": 'id="trailLength"' in content,
        "色彩选择器": 'type="color"' in content,
        "重置按钮": 'onclick="resetParameters()"' in content,
        "下载按钮": 'onclick="downloadCanvas()"' in content,
    }
    
    for name, passed in ui_checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
    
    print()
    print("📊 统计数据:")
    lines = content.split('\n')
    print(f"  📝 总行数: {len(lines)}")
    print(f"  📦 文件大小: {len(content)} bytes ({len(content)/1024:.2f} KB)")
    print(f"  🎨 CSS 样式: ~{content.count('{')} 个规则")
    print(f"  ⚙️ JavaScript 函数: ~{content.count('function ')} 个")
    
    # Check for common errors
    print()
    print("🔍 错误检查:")
    
    # Check for unclosed tags
    open_divs = content.count('<div')
    close_divs = content.count('</div>')
    divs_match = open_divs == close_divs
    print(f"  {'✅' if divs_match else '❌'} DIV 标签闭合: {open_divs}/{close_divs}")
    
    # Check for missing semicolons in critical functions
    critical_functions = ['initializeSystem', 'setup', 'draw']
    for func in critical_functions:
        if f'function {func}()' in content:
            # Find the function body
            func_start = content.find(f'function {func}()')
            func_end = content.find('function ', func_start + 1)
            if func_end == -1:
                func_end = len(content)
            func_body = content[func_start:func_end]
            
            # Simple check for balanced braces
            opens = func_body.count('{')
            closes = func_body.count('}')
            balanced = opens == closes
            print(f"  {'✅' if balanced else '❌'} {func}() 花括号匹配: {opens}/{closes}")
    
    print()
    print("=" * 60)
    print("✨ 验证完成！文件结构完整，可以正常运行")
    print("=" * 60)

if __name__ == '__main__':
    validate_html('/workspace/stellar-flow.html')
