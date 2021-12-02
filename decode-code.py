# brew install zbar
# pip install pyzbar
from pyzbar.pyzbar import decode as qrdecode
from PIL import Image

print(qrdecode(Image.open('covid-cert.png')))