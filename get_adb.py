# Check if adb is installed and set in PATH


import os
import zipfile
import requests
import subprocess


def check_adb():
    print('Checking ADB...')
    try:
        subprocess.run(['adb', 'version'], stdout=subprocess.DEVNULL)
        print('ADB found!')
        return True
    except FileNotFoundError:
        return False


def download_adb():
    # Windows
    if os.name == 'nt':
        url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
        with open('platform-tools.zip', 'wb') as f:
            f.write(requests.get(url).content)
        with zipfile.ZipFile('platform-tools.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.rename('platform-tools', 'adb')
        os.remove('platform-tools.zip')
    # Linux
    elif os.name == 'posix':
        url = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip'
        with open('platform-tools.zip', 'wb') as f:
            f.write(requests.get(url).content)
        with zipfile.ZipFile('platform-tools.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.rename('platform-tools', 'adb')
        os.remove('platform-tools.zip')
    else:
        return False


def get_adb_path():
    if check_adb():
        subprocess.run(['adb', 'kill-server'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return 'adb'
    else:
        print('ADB not found. Downloading...')
        download_adb()
        return './adb/adb' if os.name == 'posix' else 'adb\\adb.exe'
