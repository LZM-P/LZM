#!/usr/bin/env python3
import re

def validate_html_structure(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for required p5.js CDN
    if 'cdnjs.cloudflare.com/ajax/libs/p5.js' in content:
        print("✓ p5.js CDN found")
    else:
        print("✗ p5.js CDN missing")
    
    # Check for setup() function
    if 'function setup()' in content:
        print("✓ setup() function found")
    else:
        print("✗ setup() function missing")
    
    # Check for draw() function
    if 'function draw()' in content:
        print("✓ draw() function found")
    else:
        print("✗ draw() function missing")
    
    # Check for Particle class
    if 'class Particle' in content:
        print("✓ Particle class found")
    else:
        print("✗ Particle class missing")
    
    # Check for canvas container
    if 'canvas-container' in content:
        print("✓ Canvas container found")
    else:
        print("✗ Canvas container missing")
    
    # Check for seed controls
    if 'seed-input' in content and 'updateSeed()' in content:
        print("✓ Seed control UI found")
    else:
        print("✗ Seed control UI missing")
    
    # Check for parameter controls
    if 'particleCount' in content and 'flowSpeed' in content:
        print("✓ Parameter controls found")
    else:
        print("✗ Parameter controls missing")
    
    # Check for color controls
    if 'colorPalette' in content and 'updateColor' in content:
        print("✓ Color controls found")
    else:
        print("✗ Color controls missing")
    
    # Check for download function
    if 'downloadCanvas' in content:
        print("✓ Download function found")
    else:
        print("✗ Download function missing")
    
    # Check HTML structure
    if '<!DOCTYPE html>' in content:
        print("✓ DOCTYPE declaration found")
    else:
        print("✗ DOCTYPE declaration missing")
    
    if '<html' in content and '</html>' in content:
        print("✓ HTML tags found")
    else:
        print("✗ HTML tags missing")
    
    if '<head>' in content and '</head>' in content:
        print("✓ HEAD section found")
    else:
        print("✗ HEAD section missing")
    
    if '<body>' in content and '</body>' in content:
        print("✓ BODY section found")
    else:
        print("✗ BODY section missing")
    
    # Check for Google Fonts
    if 'fonts.googleapis.com' in content:
        print("✓ Google Fonts loaded")
    else:
        print("✗ Google Fonts missing")
    
    # Check for CSS styles
    if '<style>' in content and '</style>' in content:
        print("✓ CSS styles found")
    else:
        print("✗ CSS styles missing")
    
    # Check for JavaScript
    if '<script>' in content and '</script>' in content:
        print("✓ JavaScript found")
    else:
        print("✗ JavaScript missing")
    
    # Count lines
    lines = content.split('\n')
    print(f"\n✓ Total lines: {len(lines)}")
    print(f"✓ Total characters: {len(content)}")
    
    print("\n✅ HTML file validation complete!")

if __name__ == '__main__':
    validate_html_structure('/workspace/stellar-flow.html')
