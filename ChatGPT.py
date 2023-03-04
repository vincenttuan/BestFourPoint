import requests
import json
from datetime import datetime

api_key = "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"
url = "https://api.openai.com/v1/completions"

def get_message(today, index_value, target_day):
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    payload = """{
        "model": "text-davinci-003",
        "prompt": "今天是 %s, 台灣加權股價指數目前是 %s 點, 請問在 %s 的指數會到多少? 一定要寫出, 會上漲還是下跌? 一定要回答, 請可以隨意發想",
        "max_tokens": 200,
        "temperature": 1,
        "n": 5
    }"""
    payload = payload.strip() % (today, index_value, target_day)
    resp = requests.post(url=url, headers=headers, data=payload.encode())
    json_str = resp.text
    json_obj = json.loads(json_str)
    print(json_obj)
    text = json_obj["choices"][0]['text']
    text = text.strip()
    timstamp =  datetime.fromtimestamp(json_obj["created"]).strftime("%Y-%m-%d %H:%M:%S")
    return text + "\n" + timstamp


if __name__ == '__main__':
    print(get_message('2023/03/04', '15608', '2023/03/06'))
    # json_str = get_message('')
    # print(type(json_str), json_str)
    # json_obj = json.loads(json_str)
    # print(type(json_obj), json_obj["choices"][0]['text'])

