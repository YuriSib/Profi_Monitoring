import requests
import re


def get_code():
    code = 0
    headers = {
        'authority': 'sms-activate.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://sms-activate.org',
        'referer': 'https://sms-activate.org/ru/freeNumbers',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'act': 'manageFreeNumbers',
        'asc': 'getSmsByRentId',
        'rentId': '14457164',
        'csrf': '',
    }

    response = (requests.post('https://sms-activate.org/api/api.php', headers=headers, data=data)).json()

    pattern = r'\d{3,}'
    list_values = response.get('data').get('values')
    for value in list_values:
        phone_from = value.get('phoneFrom')
        if phone_from == "PROFI":
            dirty_code = value.get('text')
            code = re.search(pattern, dirty_code).group()
            break
    return code
