import requests
import time
import random
import pub

#  get token from tocken.txt
with open('token.txt', 'r') as file:
    token = file.read().strip()

def get_balence():
    url = 'https://api.neurochain.ai/tasks/get-aggregated-ncns'
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
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Balance:", data['userNcn'])
    else:
        print(f"Error: Unable to fetch balance. Status code: {response.status_code}")


def get_question_id():
    url = 'https://api.neurochain.ai/tasks/get-question'
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
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.ok:
        data = response.json()
        question_id = data['_id']
        return question_id
    else:
        print(f"Error: Unable to fetch question ID. Status code: {response.status_code}") 
        return None


# question_id = get_question_id()
# if question_id:
#     print("Question ID:", question_id)
# else:
#     print("Failed to retrieve question ID.")


def validate_id():
    question_id = get_question_id()
    if question_id:
        #print("Question ID:", question_id)
        flag = True
        url = 'https://api.neurochain.ai/tasks/validate-question'
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
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
        body = {
            "questionId": question_id,
            "validated": flag
        }
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 201:
            data = response.json()
            #print("Response:", data['validation']['status'])
        else:
            print(f"Error: Unable to validate question ID. Status code: {response.status_code}")

    else:
        print("Failed to retrieve question ID.")


while True:
    get_balence()
    validate_id()
    time.sleep(random.randint(5, 10))