import requests
from pprint import pprint
from urllib.parse import urlparse
token = 'AQAAAAAEHsPoAADLW4SZ-XnrG0fgq7H0CmynvHw'

# Task # 1
class get_request():

  def __init__(self, url_):
    self.url_adress = url_
    self.response = ''
    self.id = 0
    self.name = ''
    self.group_affiliation = ''''''
    self.relatives = ''' '''

  def url_(self):
    response = requests.get(self.url_adress)

    if response.status_code != 200 and response.status_code < 300:
      pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))

    elif response.status_code >= 300:
      pprint(response.status_code)
    else:
      pprint(f'Чувак, ты крут! Всё Ок! Код: {response.status_code}')

    return response

  def url_params(self):


    # Hulk = 'intelligence': '88',
    # Captain America = 'intelligence': '69'
    # Thanos  = 'intelligence': '100',
    path = '2619421814940190' + '/' + str(self.id)
    # path = '2619421814940190' + '/' + 'search/Thanos'
    url_adress = self.url_adress

    response = requests.get(url=url_adress + path)

    if response.status_code != 200 and response.status_code < 300:
      pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))

    elif response.status_code >= 300:
      pprint(response.status_code)
    else:
      pprint('Чувак, ты крут! Всё Ок!')

    return response

# Task # 2
class Keys_host():
  def __init__(self):
    self.connect_type = ''
    self.autorization = ''

  def open_door(self):

    self.jsn = {
      'Conntent-Type' : self.connect_type,
      'Authorization' : self.autorization
    }
    return self.jsn

class Task2_look_files(get_request):

  def __init__(self, url):
    self.url_adress = url
    self.header = {}
    self.params = {}
    self.path = ''

  def look_list_files_of_disk(self):
    # pprint(f'self.url_adress {self.url_adress}, self.path {self.path}, self.header {self.header}')
    disk_url_ = self.url_adress + self.path
    response = requests.get(url = disk_url_, headers = self.header, params = self.params)
    if response.status_code != 200 and response.status_code < 300:
      pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))

    elif response.status_code >= 300:
      pprint(response.status_code)
    else:
      pprint('Чувак, ты крут! Всё Ок!')
      pprint("""This's a file's list when sorted by days. 5 files in total open by default """)

    return response.json()
  # def files_list(self):
  #

class Task2_Upload_file():
  def __init__(self,host):
    # self.name_file = name_file
    self.host = host
    self.path = ''
    self.connect_type = ''
    self.autorization = ''

    self.file_of_local_disk = ''
    self.folder = ''





  def Upload_file(self):

    params_upload = {'path': self.host + self.path, "overwrite" : "true"}
    # params = {'path': self.path, 'url': self.file_of_local_disk}
    # pprint('Keys_host.open_door(): ', Keys_host.open_door(self=self))

    get_upload_link = requests.get(self.host + self.path, Keys_host.open_door(self), )

    response = requests.put(get_upload_link, headers= Keys_host.open_door(self), params=params_upload)
    if response.status_code != 200 and response.status_code < 300:
      pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))

    elif response.status_code >= 300:
      pprint(response.status_code)
    else:
      pprint('Чувак, ты крут! Всё Ок!')



if __name__ == '__main__':
  # data_ = {"response": "success", "id": "70", "name": "Batman"


  # url = 'http://httpbin.org/'
  # url = 'https://www.superheroapi.com/api.php/№/'

  # url_ = 'https://superheroapi.com/api/'
  # start_test_request = get_request(url_)
  # start_test_request.id = 655

  # start_test_request.event_calling()
  # answer = start_test_request.look_list_files_of_disk()

  # pprint(answer.json())
  # pprint("THAT'S A COOL HERO BETWEEN THE ALL HEROES!")

  pprint('Task 2')
  path = 'v1/disk/resources/last-uploaded'
  url = 'https://cloud-api.yandex.net/'

  keys_h = Keys_host()
  keys_h.connect_type = 'application/json'
  keys_h.autorization = 'OAuth {}'.format(token)
  open_door = keys_h.open_door()
  pprint(open_door)

  print(' ')
  yandex_disk = Task2_look_files(url)
  yandex_disk.path = path

  yandex_disk.params = {'limit' : str(5)}
  yandex_disk.header = open_door

  answer = yandex_disk.look_list_files_of_disk()
  pprint(answer)

  print(' ')
  pprint('Task 2.1')
  host = url
  path = 'E:/ХЛАМ/загрузка/Screenshot_7.png'
  url = 'v1/disk/resources/upload'
  # '\Screenshot_7.png'

  Upload_file = Task2_Upload_file(host=host)
  Upload_file.file_of_local_disk = path
  Upload_file.path = url
  Upload_file.folder = '/Файлы'

  Upload_file.connect_type = 'application/json'
  Upload_file.autorization = 'OAuth {}'.format(token)

  Upload_file.headers = keys_h.open_door()

  pprint(Upload_file.Upload_file())






