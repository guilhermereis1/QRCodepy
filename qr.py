import pyqrcode
import png
from pyqrcode import QRCode

s = "guilhermereis"
url = pyqrcode.create(s)
url.png('teste.png', scale = 5)
