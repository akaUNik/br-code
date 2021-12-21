from brcode import BRCode

 # адрес на сертификат о вакцинации 
urls = {
    'Ilya': 'https://www.gosuslugi.ru/covid-cert/status/0e4c3720-df7e-4d09-99cb-4de73fe5d96f?lang=ru',
    'Zoya': 'https://www.gosuslugi.ru/covid-cert/status/846db371-ebb4-4576-b9f9-6b135b6624c8?lang=ru',
    'Stas': 'https://www.gosuslugi.ru/covid-cert/verify/9270000011535004?lang=ru&ck=2e9b57b1608707a755e1fb4209b10ce7',
    'Lera': 'https://www.gosuslugi.ru/covid-cert/status/5d9d32a6-0aec-47b1-91fc-d56825f10472?lang=ru',
    'Max': 'https://www.gosuslugi.ru/covid-cert/status/2e5818ae-c896-4ba6-934d-5daaf93b7177?lang=ru',
    'Mikhail': 'https://www.gosuslugi.ru/covid-cert/status/c0889d55-c7ef-4051-beb3-12d065583533?lang=ru',
    'Olya': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
}

embeded_image = 'logo_stroke.png' # изображение, которое будет помещено в центр qr-code

for key, value in urls.items():
    output_image = f'br-codes/br-code_{key}.png'  # файл, куда будет записан qr-code
    with BRCode() as qr:
        img = qr.make_image(value, embeded_image)
        qr.save_image(output_image)
        qr.save_image(output_image, 'EPS')