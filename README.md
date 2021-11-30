# br-code

Python-скрипт для формирования т.н. br-code - стилизованного qr-code для брейндошников. Подробнее можно прочитать здесь https://www.facebook.com/Braindoclub

## Установка
Для создания кодов необходима библиотека qrcode
```bash
pip install qrcode[pil]
```

## Создание br-code
Для формирования своего кода необходимо открыть файл encode-code и изменить следующие переменные. Например:
```python
url = 'https://www.gosuslugi.ru/covid-cert/status/XXXX?lang=ru' # адрес на сертификат о вакцинации 
embeded_image = 'logo_stroke.png' # изображение, которое будет помещено в центр qr-code
output_image = 'br-code.png' # файл, куда будет записан qr-code 
```