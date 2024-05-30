import pyqrcode
url =input("enter web sites url:    ")
qr_code=pyqrcode.create(url)
qr_code.svg("qr_code.svg",scale=5)
