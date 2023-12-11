import requests
import urllib3
import sys
import telegram
import os
from dotenv import load_dotenv



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_assignments(devman_token):
    path = 'https://dvmn.org/api/user_reviews/'
    headers = {
        'Authorization': devman_token,
    }
    response = requests.get(path, headers=headers)
    response.raise_for_status()
    return response.json()


def get_assigns_thr_longpolling(devman_token):
    path = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': devman_token,
    }
    response = requests.get(path, headers=headers, timeout=90)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    devman_token = os.environ['DEVMAN_TOKEN']
    token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token)
    chat_id = int(input('Введите свой chat id:'))
    while True:
        try:
            answer = get_assigns_thr_longpolling(devman_token)
            if answer:
                if answer['new_attempts'][0]['is_negative']:
                    bot.send_message(chat_id=chat_id,
                                     text=f"Преподаватель проверил работу '{answer['new_attempts'][0]['lesson_title']}'. К сожалению в работе нашлись ошибки. {answer['new_attempts'][0]['lesson_url']}")
                else:
                    bot.send_message(chat_id=chat_id,
                                     text=f"Преподаватель проверил работу '{answer['new_attempts'][0]['lesson_title']}'! Преподавателю все понравилось, можно приступать к другому уроку!")
        except requests.exceptions.ReadTimeout:
            print('Timeout occured', file=sys.stderr)
        except requests.ConnectionError:
            print('Connection error', file=sys.stderr)


if __name__ == '__main__':
    main()