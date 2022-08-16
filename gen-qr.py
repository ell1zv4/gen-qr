import qrcode

data = input("Escriba la data que quiera insertar <textos, urls, etc>: ")

image = qrcode.make(data=data)

image.save("Image.png")
