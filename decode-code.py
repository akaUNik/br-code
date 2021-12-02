from brcode import BRCode

input_image = 'covid-cert.png'

qr = BRCode()
print(qr.decode_image(input_image))