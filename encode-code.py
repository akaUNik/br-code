# pip install qrcode[pil]

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image

url = 'https://www.gosuslugi.ru/covid-cert/status/51a4d2a1-862a-4e10-8041-0281b268246c?lang=ru' # адрес на сертификат о вакцинации 
embeded_image = 'logo_stroke.png' # изображение, которое будет помещено в центр qr-code
output_image = 'br-code.png'  # файл, куда будет записан qr-code

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data(url)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(208, 2, 0)),
    embeded_image_path=embeded_image
)

img.save(output_image)