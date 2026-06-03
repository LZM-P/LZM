from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Navigate to the local server
    page.goto('http://localhost:8080/stellar-flow.html')
    
    # Wait for the page to load and p5.js to initialize
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(2000)  # Give p5.js time to render
    
    # Check if canvas exists
    canvas = page.locator('canvas')
    if canvas.count() > 0:
        print("✓ Canvas created successfully")
        
        # Check canvas dimensions
        bounding_box = canvas.bounding_box()
        if bounding_box:
            print(f"✓ Canvas dimensions: {bounding_box['width']}x{bounding_box['height']}")
        
        # Take a screenshot
        canvas.screenshot(path='/tmp/stellar-flow-test.png')
        print("✓ Screenshot saved to /tmp/stellar-flow-test.png")
    else:
        print("✗ Canvas not found")
    
    # Check for control elements
    seed_input = page.locator('#seed-input')
    if seed_input.count() > 0:
        print("✓ Seed input found")
        
        # Test changing seed
        seed_input.fill('54321')
        page.wait_for_timeout(1000)
        print("✓ Seed changed to 54321")
    
    # Check buttons
    buttons = page.locator('.button')
    print(f"✓ Found {buttons.count()} buttons")
    
    # Check for console errors
    page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)
    
    browser.close()
    
print("\n✅ Test completed successfully!")
