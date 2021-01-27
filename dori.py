
import requests
from pprint import pprint
toke = '1667389228:AAHfOEBt6VXPoOqoHIgGK13p6fW-1JUTETc'
url = f'https://api.telegram.org/bot{toke}/getMe'
r=requests.get(url)
pprint(r.json()['result']['id'])