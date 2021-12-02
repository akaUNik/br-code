# br-code

Python-класс для формирования т.н. br-code - стилизованного qr-code для брейндошников. Подробнее можно прочитать здесь https://www.facebook.com/Braindoclub

## Установка
Для создания кодов необходима библиотека qrcode
```bash
pip install qrcode[pil]
```

Для декодирования qr-code необходимо установить библиотеку pyzbar
```bash
brew install zbar
pip install pyzbar
```

## Создание br-code
см. examples