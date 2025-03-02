import requests

def generate_user_data():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        data = response.json()
        print(data)  
        return data
    else:
        print(f"Помилка: {response.status_code}")
    return 