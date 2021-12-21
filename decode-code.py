from brcode import BRCode
qr = BRCode()

input_image = 'max2.jpg'
print(qr.decode_image(input_image))