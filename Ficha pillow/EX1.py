from PIL import Image
from random import randint
def imageArt():
    pathImages = ".\\images\\"
    newsize = (400, 400)
    imagem = Image.new(size=newsize, mode="RGB", color="white")
    pixelMap = imagem.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            red = randint(0,255)
            green = randint(0,255)
            blue = randint(0,255)
            pixelMap[i,j]=(red, blue, green)
    imagem.show()
imageArt()

