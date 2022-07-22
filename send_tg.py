import requests
from datetime import datetime, timedelta


try:
    from token_tg import bot_token, chat_id
except ImportError:
    bot_token = '123456789:AAEe-_123456789_123456789'
    chat_id = -1001713500645

api = 'https://api.telegram.org/bot'
method = 'sendMessage'
profit_emoji = '📈'
loss_emoji = '📉'

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')[2:]


def send_tg(profit):
    url = f'{api}{bot_token}/{method}'
    text = f'#昨日收益\n' \
           f'{yesterday}\n' + \
           (profit_emoji if float(profit) > 0 else loss_emoji) + \
           f' {profit}'
    params = {
        'chat_id': chat_id,
        'text': text,
        'disable_notification': True,
        'parse_mode': None
    }
    requests.get(url, params=params)
    return True
