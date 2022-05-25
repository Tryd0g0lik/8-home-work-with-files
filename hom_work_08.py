import requests
from pprint import pprint
from urllib.parse import urlparse


class get_request():

  def __init__(self, url_):
    self.url_adress = url_
    self.response = ''
    self.id = 0
    self.name = ''
    self.group_affiliation = ''''''
    self.relatives = ''' '''

  def url_(self):
    response = requests.get(self.url_adress, g=False)

    if response.status_code != 200:
      pprint('Уууууу... Лоо-шаа-ра Код: {}'.format(response.status_code))

    elif response.status_code > 200:
      pprint(response.status_code)
    else:
      pprint('Чувак, ты крут! Всё Ок!')

    return response

  def url_params(self):

    name = self.name

    path = '2619421814940190' + '/' + str(self.id)
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
  # data_ = {"response": "success", "id": "70", "name": "Batman"

  # url = 'https://54seo.ru/ '
  # url = 'http://httpbin.org/'
  # url = 'https://www.superheroapi.com/api.php/2619421814940190/'
  url_ = 'https://superheroapi.com/api/'
  start_test_request = get_request(url_)
  start_test_request.id = 70
  start_test_request.name = 'Batman'
  # start_test_request.event_calling()
  answer = start_test_request.url_params()
  # pprint(answer.content)
  pprint(answer.json())