import requests
from pprint import pprint
import json

class YaUpload():
  def __init__(self, token: str):
    self.token = token
    self.header = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
    self.get_url = 'v1/disk/resources/upload'

  def look_file(self):
    domen = 'cloud-api.yandex.net/'
    get_resources = 'v1/disk/resources/files'

    header = self.header
    # parametrs = {'path': self.path_to_file, 'overwrite': 'true'}
    parametrs = {'media_type' : 'image', 'offset'  : '30', 'limit' : '100'}
    protocol = 'https://'

    upl = requests.get(protocol + domen + get_resources, headers=header, params=parametrs)
    print(upl.status_code)
    # pprint(upl.json())
    return upl

  def get_link(self, path : str):
    self.path_to_file = path
    print(f'''self.path_to_file: {self.path_to_file}''')
    domen = 'cloud-api.yandex.net/'
    protocol = 'https://'
    parametrs = {'path' : self.path_to_file, 'overwrite'  : 'true'}

    upl = requests.get(protocol + domen + self.get_url, headers=self.header, params=parametrs)
    print(upl.status_code)
    # print(upl.json()['href'])
    return upl.json()['href']

  def get_upload_file(self, path : str):
    print(f'YaUpload.look_file(self): {YaUpload.get_link(self, path)}')
    t = requests.put(YaUpload.get_link(self, path))
    pprint(t.status_code)
    # pprint(t.json())


if __name__ ==  '__main__':
  my_token = (open('../token.txt', 'r', encoding= 'utf-8')).read()
  # user_path = 'E:/%D0%A5%D0%9B%D0%90%D0%9C/%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0/Screenshot_7.png'
  user_path = 'E%3A%2F%D0%A5%D0%9B%D0%90%D0%9C%2F%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%2FScreenshot_10.png'

  u = YaUpload(my_token)
  u.look_file()
  u.get_link(user_path)
  u.get_upload_file(user_path)
  pprint(u)
