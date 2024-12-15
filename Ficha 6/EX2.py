from PIL import Image
def imageArt():
    pathImages = ".\\images\\"
    newsize = (600, 600)
    imagem = Image.new(size= newsize, mode="RGB", color="white")
    imagem.show()
    pixelMap = imagem.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            while j < 200:
                red = 255
                blue = 0
                green = 0
                pixelMap[i,j]=(red, blue, green)
            while j>200 and j<400:
                red = 255
                blue = 255
                green = 255
                pixelMap[i,j]=(red, blue, green)
            else:
                red = 0
                blue = 255
                green = 0
                pixelMap[i,j]=(red, blue, green)
    imagem.load()
    imagem.save(pathImages+"imagem1.jpg")
imageArt()