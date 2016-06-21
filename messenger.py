import requests

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('thread')
parser.add_argument('-c', '--colour')
args = parser.parse_args()

def colour(t, c):
    headers = {
        'origin': 'https://www.messenger.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.messenger.com/t/' + t,
        'authority': 'www.messenger.com',
        'cookie': 'YOUR COOKIE HERE',
    }
    data = 'color_choice=%23' + c + '&thread_or_other_fbid=' + t + '&__user=... [insert that stuff here]'
    r = requests.post('https://www.messenger.com/messaging/save_thread_color/?source=thread_settings&dpr=1', headers=headers, data=data)
    print(r.status_code)
    print(r.reason)

if args.colour:
    colour(args.thread, args.colour)
