import requests

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('thread')
parser.add_argument('-c', '--colour')
parser.add_argument('-e', '--emoji')
args = parser.parse_args()


def emoji(t, e):
    headers = {
        'origin': 'https://www.messenger.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.messenger.com/t/1515962548694749',
        'authority': 'www.messenger.com',
        'cookie': 'datr=LjYtV85dWvJ_w4TSEQm1AxU7; lu=ggUOTBPMiVnWDrIq3HYc8kMg; p=-2; c_user=100009563164658; xs=177%3A2Cwo-nhRLi-QAg%3A2%3A1462934121%3A2850; csm=2; s=Aa5wNSGGY1G6IdxW; sb=NzYtV8wsvAFbhFKmkz_aFoo8; presence=EDvF3EtimeF1465977997EuserFA21B09563164658A2EstateFDutF1465977997219CEchFDp_5f1B09563164658F4806CC; act=1465978011416%2F193',
    }

    data = 'emoji_choice='+e+'&thread_or_other_fbid='+t+'&__user=100009563164658&__a=1&__dyn=7AzkXh8OAcAxd2u6W85k2m3m8GAdy8-S-C11xG3F6xybxu13wFGEcVojyR88wPGi7VXDG4UiwExW14DwPxSFEW2O7EOEixu1jyoCcyUW48hxG&__req=a&__be=0&__pc=PHASED%3Amessengerdotcom_pkg&fb_dtsg=AQE07U8O_RsN%3AAQEIpeaXCLgM&ttstamp=2658169485585567995821157858658169731121019788677610377&__rev=2382617'

    r = requests.post('https://www.messenger.com/messaging/save_thread_emoji/?source=thread_settings&dpr=1', headers=headers, data=data)
    print(r.status_code)
    print(r.reason)
    # print(r.content)


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
        'cookie': 'datr=LjYtV85dWvJ_w4TSEQm1AxU7; lu=ggUOTBPMiVnWDrIq3HYc8kMg; p=-2; c_user=100009563164658; xs=177%3A2Cwo-nhRLi-QAg%3A2%3A1462934121%3A2850; csm=2; s=Aa5wNSGGY1G6IdxW; sb=NzYtV8wsvAFbhFKmkz_aFoo8; presence=EDvF3EtimeF1465977997EuserFA21B09563164658A2EstateFDutF1465977997219CEchFDp_5f1B09563164658F4806CC; act=1465978011416%2F193',
    }
    data = 'color_choice=%23' + c + '&thread_or_other_fbid=' + t + '&__user=100009563164658&__a=1&__dyn=7AzkXh8OAcAxd2u6W85k2m3m8GAdy8-S-C11xG3F6xybxu13wFGEcVojyR88wPGi7VXDG4UiwExW14DwPxSFEW2O9xicG4EnwkUC9z8qx24oqw&__req=1f3&__be=0&__pc=PHASED%3Amessengerdotcom_pkg&fb_dtsg=AQGi9cHQD2SA%3AAQGlKx2Ewb5s&ttstamp=26581711055799728168508365586581711087512050691199853115&__rev=2392291'
    r = requests.post('https://www.messenger.com/messaging/save_thread_color/?source=thread_settings&dpr=1', headers=headers, data=data)
    print(r.status_code)
    print(r.reason)

if args.emoji:
    print(args.emoji)
    colour(args.thread, args.emoji)

if args.colour:
    colour(args.thread, args.colour)
