import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data('https://www.gosuslugi.ru/covid-cert/status/51a4d2a1-862a-4e10-8041-0281b268246c?lang=ru')

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(237, 35, 13)),
    embeded_image_path='logo_stroke.png'
)
#logo_display = Image.open('logo.png')
#logo_display.thumbnail((60, 60))
#logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
#img.paste(logo_display, logo_pos)

#img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/image.png")

img.save('qraindo-code.png')