import time
import subprocess
from getpass import getpass
from session import adb_path
from config import lock_nums
from methods import *

try:
    from token_phone import phone_pass
    # password = input('Password: ') or password
    phone_pass = phone_pass or getpass('Phone Password: ')
except ImportError:
    phone_pass = getpass() or '123456'


def unlock():
    power()
    time.sleep(0.5)
    wakeup()
    time.sleep(0.5)
    swipe_home()
    time.sleep(1)
    for digit in list(phone_pass):
        subprocess.run(f'{adb_path} shell input tap {lock_nums[digit][0]} {lock_nums[digit][1]}'.split())
        time.sleep(0.1)
    return True
