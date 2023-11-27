import requests
import json
import math
import uuid

from core.settings import settings

CLIENT_SECRET = settings.bots.gpt_client_secret
AUTH_DATA = settings.bots.gpt_auth_data


def get_answer():
    info_msg = ''
    
    url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
    headers = {
        'Authorization': f'Bearer {AUTH_DATA}',
        'RqUID': str(uuid.uuid4()),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'scope': 'GIGACHAT_API_PERS'
    }
    
    try:
        response = requests.get(url, headers=headers, json=payload)

        if response.status_code == 200:
            info_msg = f'OK'
        else:
            info_msg = f'not OK'
    except:
        info_msg = 'Мррр мяяу!'
    
    return info_msg

