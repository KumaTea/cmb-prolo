import subprocess
from session import adb_path


def power():
    return subprocess.run(
        f'{adb_path} shell '
        f'input keyevent '
        f'KEYCODE_POWER'.split())


def wakeup():
    return subprocess.run(
        f'{adb_path} shell '
        f'input keyevent '
        f'KEYCODE_WAKEUP'.split())


def swipe_home():
    return subprocess.run(
        f'{adb_path} shell '
        f'input swipe '
        f'540 2380 540 1500 100'.split())  # go home
