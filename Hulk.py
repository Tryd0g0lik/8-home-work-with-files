import requests
from pprint import pprint
from urllib.parse import urlparse

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

    if response.status_code != 200:
      pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))

    elif response.status_code > 200:
      pprint(response.status_code)
    else:
      pprint('Чувак, ты крут! Всё Ок!')

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

if __name__ == '__main__':
  url = 'https://superheroapi.com/api/'
  start_test_request = get_request(url)
  start_test_request.id = 655
  answer = start_test_request.url_params()
  pprint(answer.json())
  pprint("THAT'S A COOL HERO BETWEEN THE ALL HEROES!")