import requests


def create_folder(folder):
    token = 'AQAAAAARJ0BAAADLW4fnBdNTr0m8taVtPKSy6bY'
    url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + folder
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(url, headers=headers)
    return response


if __name__ == '__main__':
    folder = 'Netology'
    create_folder(folder)
