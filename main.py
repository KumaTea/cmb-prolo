import time
import subprocess
from login import login
from unlock import unlock
from send_tg import send_tg
from session import adb_path
from methods import swipe_home
from get_profit import get_profit


def main():
    # starting adb
    print('Starting ADB...')
    subprocess.run(f'{adb_path} start-server'.split())

    # unlock the phone
    unlock()
    time.sleep(1)

    # open app
    with open('open-app.sh', 'r') as f:
        open_app_cmd = f.read()
    for line in open_app_cmd.split('\n'):
        if line and not line.startswith('#'):
            command = f'{adb_path} shell {line}'
            # print(f'Running: {command}')
            subprocess.call(command.split(), stdout=subprocess.DEVNULL)
            # time.sleep(1)
    print('App opened')

    # login
    login()
    print('Logged in')
    time.sleep(3)

    # get profit
    profit = get_profit()
    print(f'Profit: {profit}')

    # close app
    swipe_home()
    subprocess.run(f'{adb_path} shell am force-stop cmb.pb'.split())

    # quit adb
    subprocess.run(f'{adb_path} kill-server'.split())

    # send profit
    send_tg(profit)


if __name__ == '__main__':
    main()
