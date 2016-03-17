import random
import re
import tkinter as tk
from tkinter.colorchooser import askcolor

import requests

root = tk.Tk()
root.resizable(False, False)
root.title('Colours')
c = '000000'
selected_color = tk.StringVar(value='#' + c)
selected_color.set('#' + c)

status = tk.StringVar(value='Waiting for input')


def get_color():
    global c
    c = askcolor()[1][1:]
    selected_color.set('#' + c.upper())
    color_select_label.update()


def get_uid(s):
    headers = {
        'Origin': 'http://findmyfbid.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623'
                      '.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'http://findmyfbid.com/',
        'Connection': 'keep-alive',
    }

    data = 'url=' + s

    r = requests.post('http://findmyfbid.com/', headers=headers, data=data)
    return re.search(r'<code>\d+</code>', r.text).group()[6:-7]


def send_data():
    e = emoji_input.get()
    ts = random.randint(0, 10 ** 60 - 1)
    my_id = your_id_input.get()
    if your_is_id.get():
        my_id = get_uid(my_id)
        print('your id:', my_id)
        status.set('Found your ID: ' + my_id)
        status_label.update()

    thread_id = thread_id_input.get()
    if thread_is_id.get():
        thread_id = get_uid(thread_id)
        print('thread id:', thread_id)
        status.set('Found thread ID: ' + thread_id)
        status_label.update()

    if c:

        data = 'color_choice=%23{0}&thread_or_other_fbid={1}&__user={3}&__a=1&__dyn=7AzkXh8Z38ogDxKy1' \
               'l0BwRyaF3oyfJLFwgoqwWhEoyUnwgU9GGEcVovkwy3eE99XDG4UiwExW14wXxumFEW2O9xifxa5U&__req=11&fb_dtsg=AQEUx' \
               'N8vTec6%3AAQGG9e2hzCgE&ttstamp={2}&__rev=2231853'.format(c, thread_id, ts, my_id)
        from context import headers  # , data
        # data = data[:16] + c + data[16+6:]
        r = requests.post(
            'https://www.messenger.com/messaging/save_thread_color/?source=thread_settings&__pc=EXP1%3Amessengerdot'
            'com_pkg&dpr=1',
            headers=headers, data=data)
        if r.status_code == 200:
            print('color: done:', r.text)
            status.set('Color: done: 200')
            status_label.update()
        else:
            print('color: nope:', r.status_code, r.text)
            status.set('Color: nope: ' + str(r.status_code))
            status_label.update()
    if e[:3] == '\\t ':
        e = ' E2 80 89 '.join(['F0 9F 87 ' + str(hex(ord(x) + 69))[2:].lower() for x in e[3:]])
    if e:
        e = '%' + e
        ts = random.randint(0, 10 ** 60 - 1)
        e = e.replace(' ', '%')
        # headers = {
        #     'origin': 'https://www.messenger.com',
        #     'accept-encoding': 'gzip, deflate',
        #     'accept-language': 'en-US,en;q=0.8',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.'
        #                   '2623.87 Safari/537.36',
        #     'content-type': 'application/x-www-form-urlencoded',
        #     'accept': '*/*',
        #     'referer': 'https://www.messenger.com/t/' + str(thread_id),
        #     'authority': 'www.messenger.com',
        #     'cookie': 'datr=5f6uVqVsvp1VLKVMSvJ6kxr4; lu=gA9hlnwpWNBUMX8aSQZi1SXg; __lfcc=1; __lncc_l.facebook.com='
        #               '1; c_user={0}; xs=127%3AQNC_6NFGhIcvYg%3A2%3A1454309099%3A2850; csm=2; s=Aa7-vIs'
        #               'lzkDs2ekP; p=-2; act=1458120929814%2F49; presence=EDvF3EtimeF1458120934EuserFA21B{1}'
        #               'A2EstateFDutF1458120934028CEchFDp_5f1B{1}F939CC'.format(my_id, my_id[-11:]),
        # }
        #
        data = 'emoji_choice={0}&thread_or_other_fbid={1}&__user={3}&__a=1&__dyn=7AzkXh8Z38ogDxKy1l0BwR' \
               'yaF3oyfJLFwgoqwWhEoyUnwgU9GGEcVovkwy3eE99XDG4UiwExW14wXxumFEW2O9xifxa5U&__req=7j&fb_dtsg=AQE1qaTJNP' \
               'ee%3AAQHAHmiowgV4&ttstamp={2}&__rev=2231853'.format(e, thread_id, ts, my_id)

        from context import headers

        r = requests.post(
            'https://www.messenger.com/messaging/save_thread_emoji/?source=thread_settings&__pc=EXP1%3Amessengerdot'
            'com_pkg&dpr=1',
            headers=headers, data=data)
        if r.status_code == 200:
            print('emoji: done: 200')
            status.set('Emoji: done: 200')
            status_label.update()
        else:
            print('emoji: nope:', r.text)
            status.set('Emoji: nope: ' + str(r.status_code))
            status_label.update()
    status.set('Waiting for input.')


your_is_id = tk.BooleanVar()
your_id_label = tk.Label(root, text='Your ID:')
your_id_input = tk.Entry(root)
your_id_is_id = tk.Checkbutton(root, variable=your_is_id)

thread_is_id = tk.BooleanVar()
thread_id_label = tk.Label(root, text='Thread ID:')
thread_id_input = tk.Entry(root)
thread_id_is_id = tk.Checkbutton(root, variable=thread_is_id)

color_select_button = tk.Button(root, text='Select Colour', command=get_color)
color_select_label = tk.Label(root, textvariable=selected_color)

emoji_input = tk.Entry(root)
emoji_input_label = tk.Label(root, text='Emoji code:')

send_button = tk.Button(root, text="Set", command=send_data, width=20)

status_label = tk.Label(root, textvariable=status)

your_id_label.grid(row=0, column=0)
your_id_input.grid(row=0, column=2)
your_id_is_id.grid(row=0, column=1)

thread_id_label.grid(row=1, column=0)
thread_id_input.grid(row=1, column=2)
thread_id_is_id.grid(row=1, column=1)

color_select_button.grid(row=2, column=0)
color_select_label.grid(row=2, column=1, columnspan=2)

emoji_input_label.grid(row=3, column=0)
emoji_input.grid(row=3, column=1, columnspan=2)

send_button.grid(row=4, columnspan=3)

status_label.grid(row=5, columnspan=3)

tk.mainloop()
