import requests
import Hulk as h
from pprint import pprint
from urllib.parse import urlparse

token = 'AQAAAAAEHsPoAADLW4SZ-XnrG0fgq7H0CmynvHw'


# Task # 2

class Keys_host():
  # This is a key factor for the open the door in to the server

  def __init__(self):
    self.connect_type = ''
    self.autorization = ''

  def open_host(self):

    self.jsn = {
      'Conntent-Type' : self.connect_type,
      'Authorization' : self.autorization
    }
    return self.jsn

class Url(Keys_host):
  # goes into the read the file/ First get the link on disk
  def __init__(self, domen, path):
    Keys_host.__init__(self)
    self.domen = domen
    self.path = path

    self.folder = None
    self.limit = None
    self.media_type = None
    self.params = {}

  def _href(self):
    href = 'https://'  + self.domen + self.path
    if self.folder:
      href = href + '/' + self.folder
    return href

  def look_file(self):
    header = super().open_host()
    href = Url._href(self)

    # media_type = {}
    if self.media_type:
      # media_type = self.media_type
      self.params['media_type'] = self.media_type

    if self.limit:
      # limit = str(self.limit)
      self.params['limit'] = str(self.limit)

    response =  requests.get(url  = href, headers = header, params = self.params)

    return response

  def __str__(self):
    return Url.look_file(self).json()
  # def Look_files(self):
  #   Url.look_file()
  #   params = {}

class Upload(Keys_host):
  def __init__(self):
    pass


#
#   def __init__(self, url):
#     self.url_adress = url
#     self.header = {}
#     self.params = {}
#     self.path = ''
#
#   def look_list_files_of_disk(self):
#     # pprint(f'self.url_adress {self.url_adress}, self.path {self.path}, self.header {self.header}')
#     disk_url_ = self.url_adress + self.path
#     response = requests.get(url = disk_url_, headers = self.header, params = self.params)
#     if response.status_code != 200 and response.status_code < 300:
#       pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))
#
#     elif response.status_code >= 300:
#       pprint(response.status_code)
#     else:
#       pprint('Чувак, ты крут! Всё Ок!')
#       pprint("""This's a file's list when sorted by days. 5 files in total open by default """)
#
#     return response.json()
#   # def files_list(self):
#   #
#
# class Task2_Upload_file():
#   def __init__(self,host):
#     # self.name_file = name_file
#     self.host = host
#     self.path = ''
#     self.connect_type = ''
#     self.autorization = ''
#
#     self.file_of_local_disk = ''
#     self.folder = ''

  # def Upload_file(self):
  #
  #   params_upload = {'path': self.host + self.path, "overwrite" : "true"}
  #   # params = {'path': self.path, 'url': self.file_of_local_disk}
  #   # pprint('Keys_host.open_host(): ', Keys_host.open_host(self=self))
  #
  #   get_upload_link = requests.get(self.host + self.path, Keys_host.open_host(self), )
  #
  #   response = requests.put(get_upload_link, headers= Keys_host.open_host(self), params=params_upload)
  #   if response.status_code != 200 and response.status_code < 300:
  #     pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))
  #
  #   elif response.status_code >= 300:
  #     pprint(response.status_code)
  #   else:
  #     pprint('Чувак, ты крут! Всё Ок!')

if __name__ == '__main__':

  pprint('Task 2')
  path = 'v1/disk/resources/files'
  domen = 'cloud-api.yandex.net/'
  file_type = {'musik': 'audio', 'doc': 'document', 'img': 'image'}

  #  Keys
  keys_h = Keys_host()
  keys_h.connect_type = 'application/json'
  keys_h.autorization = 'OAuth {}'.format(token)
  open_host = keys_h.open_host()

  # Open the dor into server
  properties_url = Url(domen, path)
  properties_url.autorization = keys_h.autorization
  properties_url.connect_type = keys_h.connect_type
  # (properties_url.Look_files())
  properties_url.media_type = (str(file_type['img'])).strip("'")
  properties_url.limit = 150
  pprint(properties_url.__str__())
  # properties_url.folder = "Файлы"


  # Looking the files
  print(' ')
  pprint("Task a part 2.1")

  answered = properties_url.look_file()
  pprint(answered)

  # url = 'v1/disk/resources/upload'
  # path = 'E:/ХЛАМ/загрузка/'
  # '\Screenshot_7.png'






