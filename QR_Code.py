import pyqrcode
from pyqrcode import QRCode

s ="https://www.javatpoint.com/net-framework"

# generate QR Code
url = pyqrcode.create(s)

url.svg("1st.svg",scale=8)