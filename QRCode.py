#pip install pyqrcode
import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.google.com"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) 
