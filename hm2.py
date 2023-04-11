from pprint import pprint

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path: str):
        url = 'https://cloud-api.yandex.net:443'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        result = self._get_upload_link(disk_file_path=disk_file_path)
        url = result.get('href')
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Зачисленно')

if __name__ == '__main__':
    path_to_file = 'https://yandex.ru/dev/disk/poligon/'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(disk_file_path='netology/test23.txt', filename='text.txt')

print(result)