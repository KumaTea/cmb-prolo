import os
import time
import subprocess
from ocr import recognize
from session import adb_path

screenshot_path = '/storage/emulated/0/Download/cmb.png'
local_path = 'cmb.png'


def get_profit():
    subprocess.run(f'{adb_path} shell input tap 540 775'.split())  # profit details
    time.sleep(2)

    subprocess.run(f'{adb_path} shell screencap -p {screenshot_path}'.split())
    time.sleep(1)
    subprocess.run(f'{adb_path} pull {screenshot_path}'.split())
    time.sleep(1)
    assert os.path.isfile(local_path)
    subprocess.run(f'{adb_path} shell rm {screenshot_path}'.split())

    profit = recognize(local_path)
    os.remove(local_path)
    return profit
