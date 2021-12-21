from brcode import BRCode

url = 'https://www.gosuslugi.ru/covid-cert/status/51a4d2a1-862a-4e10-8041-0281b268246c?lang=ru' # адрес на сертификат о вакцинации 
embeded_image = 'logo_stroke.png' # изображение, которое будет помещено в центр qr-code
output_image = 'br-code.png'  # файл, куда будет записан qr-code

qr = BRCode()
img = qr.make_image(url, embeded_image)
print(img.mode)
qr.save_image(output_image)
qr.save_image(output_image, 'EPS')