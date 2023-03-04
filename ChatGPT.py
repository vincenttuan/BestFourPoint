import requests
import json

api_key = "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"
url = "https://api.openai.com/v1/completions"

def get_message(keyword):
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    payload = """{
        "model": "text-davinci-003",
        "prompt": "請問台灣與中國會開戰嗎",
        "max_tokens": 100,
        "temperature": 0,
        "n": 1
    }"""
    payload = payload.strip()
    resp = requests.post(url=url, headers=headers, data=payload.encode())
    return resp.text


if __name__ == '__main__':
    json_str = get_message('')
    print(type(json_str), json_str)
    json_obj = json.loads(json_str)
    print(type(json_obj), json_obj["choices"][0]['text'])

