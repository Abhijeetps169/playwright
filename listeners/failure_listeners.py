def capture_failure(page, test_name):
    page.screenshot(path=f"reports/screenshots/{test_name}.png")