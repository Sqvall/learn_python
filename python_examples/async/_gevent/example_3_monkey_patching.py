import gevent
from gevent import monkey
import time

# import requests

monkey.patch_all()

import requests

urls = [
    'https://docs.python.org/3/library/asyncio-future.html',
    'https://www.google.com/',
    'https://devpython.ru/',
    'https://www.python.org/'
]


def fetch_url(url):
    print('Starting %s' % url)
    data = requests.get(url).text
    print('{} done'.format(url))


def sync_executor():
    for url in urls:
        data = requests.get(url).text


jobs = [
    gevent.spawn(fetch_url, _url)
    for _url in urls
]

started = time.time()
gevent.wait(jobs)
print('Spent: {}'.format(time.time() - started))
