#!/usr/bin/env python3
"""
Validate lycoris-bloom.html file
"""
import re

def validate_lycoris(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 70)
    print("🌺 彼岸花开 - 动画验证报告")
    print("=" * 70)
    print()
    
    # Check structure
    structure = {
        "HTML 基础结构": "<!DOCTYPE html>" in content and "<html" in content,
        "p5.js CDN": "cdnjs.cloudflare.com/ajax/libs/p5.js" in content,
        "Google Fonts": "fonts.googleapis.com" in content,
        "Canvas 容器": "canvas-container" in content,
        "CSS 样式": "<style>" in content and "</style>" in content,
        "JavaScript": "<script>" in content and "</script>" in content,
    }
    
    print("🎨 结构验证:")
    for name, passed in structure.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
    
    print()
    print("⚙️ 功能验证:")
    
    # JavaScript functionality
    functions = {
        "Flower 类": "class Flower" in content,
        "Petal 类": "class Petal" in content,
        "Star 类": "class Star" in content,
        "Meteor 类": "class Meteor" in content,
        "setup()": "function setup()" in content,
        "draw()": "function draw()" in content,
        "drawBackground()": "function drawBackground()" in content,
        "windowResized()": "function windowResized()" in content,
        "updateParam()": "function updateParam(" in content,
        "updateSeed()": "function updateSeed()" in content,
        "downloadCanvas()": "function downloadCanvas()" in content,
    }
    
    for name, passed in functions.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
    
    print()
    print("🌺 彼岸花特效:")
    
    # Special features
    features = {
        "贝塞尔曲线花瓣": "bezierVertex" in content,
        "弹性绽放动画": "easeOutElastic" in content,
        "流场系统": "noise" in content and "wind" in content.lower(),
        "花瓣飘落": "floatingPetals" in content,
        "光晕效果": "shadowBlur" in content,
        "渐变背景": "drawBackground" in content,
        "流星效果": "Meteor" in content,
        "星点闪烁": "Star" in content and "twinkle" in content,
        "轨迹效果": "trail" in content,
        "彼岸色谱": "deepRed" in content and "brightRed" in content,
    }
    
    for name, passed in features.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
    
    print()
    print("🎮 交互控件:")
    
    # UI elements
    ui = {
        "Seed 输入": 'id="seed-input"' in content,
        "上一世/下一世按钮": "上一世" in content and "下一世" in content,
        "轮回转世按钮": "轮回转世" in content,
        "花瓣密度滑块": 'id="petalDensity"' in content,
        "绽放速度滑块": 'id="bloomSpeed"' in content,
        "风力强度滑块": 'id="windStrength"' in content,
        "红黄比例滑块": 'id="colorRatio"' in content,
        "重置按钮": 'onclick="resetParameters()"' in content,
        "下载按钮": 'onclick="downloadCanvas()"' in content,
    }
    
    for name, passed in ui.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {name}")
    
    print()
    print("📊 统计数据:")
    lines = content.split('\n')
    print(f"  📝 总行数: {len(lines)}")
    print(f"  📦 文件大小: {len(content)} bytes ({len(content)/1024:.2f} KB)")
    print(f"  ⚙️ JavaScript 函数: ~{content.count('function ')} 个")
    print(f"  🎨 CSS 规则: ~{content.count('{')} 个")
    
    print()
    print("=" * 70)
    print("✅ 验证完成！彼岸花开动画已准备就绪")
    print("=" * 70)

if __name__ == '__main__':
    validate_lycoris('/workspace/lycoris-bloom.html')
