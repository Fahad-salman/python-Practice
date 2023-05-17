import qrcode
img = qrcode.make('https://youtube.com/shorts/z3KmtSA0I-w?feature=share')
type(img)  
img.save("saleh.png")
# img.show() 