import requests
from pprint import pprint
from urllib.parse import urlparse
from look_files import Keys_host as keys
from look_files import Url

# import look_files
token = '....'

key_ = keys()


class Upload(keys):
  def __init__(self, host_key, link_file):
    self.header = host_key
    self.link_file  = link_file
    # self.link_disk  = None
    self.domen  = None
    self.path = None
    self.floder = None

  def _get_link_ya_disk(self):
    link_YAdisk = 'https://'  + self.domen  + self.path
    # pprint('11', self.floder)

    return link_YAdisk
  
  def _link_on_file(self):
    get_link_file = (self.link_file)
    params  = {'path' : get_link_file, "overwrite" : 'true'}
    # requests.get(self.link_file, headers=self.header, params=params)
    print('1',Upload._get_link_ya_disk(self))
    print(self.header)
    pprint(params)

    get_link  = requests.get(Upload._get_link_ya_disk(self), headers = self.header, params=params)
    # get_link  = requests.get(link_disk, headers = self.header, params=params)
    print(get_link.status_code)
    return (get_link.json())

  def upload_file(self, file_name):
    href_file = Upload._link_on_file(self)
    response  = requests.put(href_file, data=(open(file_name, 'rb')))
    (response.raise_for_status())
    return response.json()
    # return  (link_disk, link_file, get_link, params)


if __name__ ==  '__main__':


  #  Keys
  keys_h = key_
  keys_h.connect_type = 'application/json'
  keys_h.autorization = 'OAuth {}'.format(token)
  # open_host = keys_h.open_host()
  # pprint(open_host)

  domen = 'cloud-api.yandex.net/'
  part_disk = 'v1/disk/resources/upload'
  # link_file = 'E:/ХЛАМ/загрузка/Screenshot_7.png'
  # link_file = 'E:/ХЛАМ/загрузка/Screenshot_7.png'
  link_file = '/%5C%D0%A5%D0%9B%D0%90%D0%9C%5C%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0%5C'
  # ''
  pprint(link_file)
  upload = Upload(keys_h.open_host(), link_file)
  upload.path = part_disk
  upload.domen  = domen
  # upload.floder = 'Файлы'

  upload.upload_file('Screenshot_7.png')

  # print(Upload.upload_file(self=upload))

  # href.
  # pprint(href)
