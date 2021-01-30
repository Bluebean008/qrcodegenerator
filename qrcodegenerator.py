import qrcode
import os

item = str(input("Convert this item to QR Code:"))
imagename = str(input("Name of the QR Code:"))
cwd = os.getcwd()

qr = qrcode.make(item)
filename = str(imagename + '.png')
qr.save(filename)
imagecwd = cwd + "\\" + filename
os.startfile(imagecwd)
print('Image saved in ', cwd)
