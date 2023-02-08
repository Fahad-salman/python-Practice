import qrcode
img = qrcode.make('')
type(img)  
img.save("find_out.png")
img.show() 