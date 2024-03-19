from datasets import load_dataset
import random
import requests

dataset = load_dataset("flytech/python-codes-25k")
#print(dataset['train'][0]['instruction'])
#print(dataset['train'][0]['output'])

index = random.randint(0, len(dataset['train']))

instruction = dataset['train'][index]['instruction']
output = dataset['train'][index]['output']

with open('token.txt', 'r') as file:
    token = file.read().strip()

def publish():
    url = 'https://api.neurochain.ai/tasks/submit-question'
    headers = {
        'authority': 'api.neurochain.ai',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en',
        'authorization': token,
        'content-type': 'application/json; charset=utf-8',
        'if-none-match': 'W/"24c-bLBCWU6vyoJtqqh8yB+yvVpv8Q0"',
        'origin': 'https://app.neurochain.ai',
        'referer': 'https://app.neurochain.ai/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    }
    data = {
        "question": instruction,
        "answer": output,
        "topic" : "Python"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(response.json())
    else:
        print(f"Error: Unable to publish. Status code: {response.status_code}")


