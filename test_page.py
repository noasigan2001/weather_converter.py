from pathlib import Path
from playwright.sync_api  import sync_playwright, expect
with sync_playwright() as p:
 browser = p.chromium.launch()