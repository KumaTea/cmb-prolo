import time
import subprocess
from getpass import getpass
from session import adb_path
from config import cmb_nums

try:
    from token_cmb import cmb_pass
    # password = input('Password: ') or password
    cmb_pass = cmb_pass or getpass('CMB Password: ')
except ImportError:
    cmb_pass = getpass() or '123456'


def login():
    for digit in list(cmb_pass):
        subprocess.run(f'{adb_path} shell input tap {cmb_nums[digit][0]} {cmb_nums[digit][1]}'.split())
        time.sleep(0.1)

    subprocess.run(f'{adb_path} shell input tap 540 1020'.split())  # login
    return True
