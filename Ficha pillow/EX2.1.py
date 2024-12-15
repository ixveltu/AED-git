from PIL import Image
def imageArt():
    pathImages = ".\\images\\"
    newsize = (600, 600)
    imagem = Image.new(size= newsize, mode="RGB", color="white")
    
    pixelMap = imagem.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            while j < 200:
                pixelMap[i,j]=(255, 0, 0)
            while j>200 and j<400:
                pixelMap[i,j]=(255, 255, 255)
            else:
                pixelMap[i,j]=(0, 255, 0)
    imagem.load()
imageArt()