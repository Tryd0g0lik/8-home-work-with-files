# {Content-Type : application/json}
# cloud-api.yandex.net/v1/
# {Authorization  : AQAAAAAEHsPoAADLW4SZ-XnrG0fgq7H0CmynvHw}
import requests

class YaUploader:
    # Базовая сслыка как константа

  def __init__(self, token: str, file_path: str, file_name: str):  # передаю параметры отдельно чтобы было понятно
    # path - путь у файлу на ЯДиске, overwrite - я разрешаю переписать файл
    self.file_path = file_path
    self.file_name = file_name
    self.token = token
    self.headers = {'Accept': 'application/json', 'OAuth': self.token}  # Заголовки обновляем токен
    self.params = {'path': f'{self.file_name}', 'overwrite': 'true'}


  def upload(self):
    PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    response = requests.get(url = 'https://disk.yandex.ru/client/disk/Файлы', headers = self.headers, params = self.params )
    put_url = response.json().get('href')

    files = {'file': open(self.file_path + self.file_name, 'rb+')}  # готовим файл для передачи его надо открыть в
    # байтовом режиме
    response = requests.put(PREPARE_UPLOAD_URL, data=(open(file_name, 'rw')))
    return response.text

if __name__ == "__main__":
  file_name = 'Screenshot_7.png'
  token = 'AQAAAAAEHsPoAADLW4SZ-XnrG0fgq7H0CmynvHw'
  file_path = 'E:/ХЛАМ/загрузка/'
  y = YaUploader(token, file_path, file_name)
  y.upload()

