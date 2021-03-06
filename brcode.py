# pip install qrcode[pil]
# brew install zbar
# pip install pyzbar

from typing import List
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from pyzbar.pyzbar import decode as qrdecode
from PIL import Image

class BRCode:
    def __init__(self) -> None:
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.qr.clear()

    def make_image(self, url, embeded_image):
        self.qr.add_data(url)
        self.img = self.qr.make_image(
            image_factory = StyledPilImage,
            module_drawer = RoundedModuleDrawer(),
            color_mask = SolidFillColorMask(back_color=(255, 255, 255), front_color=(208, 2, 0)),
            embeded_image_path = embeded_image
        )
        return self.img

    def save_image(self, image_path, format='PNG') -> None:
        if format == 'PNG':
            self.img.save(image_path)
        elif format == 'EPS':
            if self.img.mode == 'RGBA':
                fig = self.img.convert('RGB')
                fig.save(f'{image_path}-RGB.eps', lossless = True)

    def decode_image(self, input_image) -> list:
        return qrdecode(Image.open(input_image))
        