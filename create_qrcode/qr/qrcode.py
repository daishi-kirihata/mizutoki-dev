# -*- coding: utf-8 -*-
import qrcode
from PIL import Image

class appsBase():
    def __init__(self):
        self.qr_image = None
    
    def make(self):
        qr = qrcode.QRCode(box_size = 5)
        #qr.add_data('https://mizutoki.co.jp')
        qr.add_data('https://qiita.com/iorionda/items/c7e0aca399371068a9b8')
        qr.make()
        self.qr_image = qr.make_image()
        self.qr_image.save('./test.png')
