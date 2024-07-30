import os

def capture_screenshot(file_path):
    os.system(f"adb exec-out screencap -p > {file_path}")
