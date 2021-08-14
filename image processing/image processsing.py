
from PIL import Image,ImageFilter
img = Image.open("pikachu.jpg")

#image properties
print(img.format)
print(img.size)
print(img.mode)

#showing image and cropping image
#img.show()
box = (100, 100, 400, 400)
region = img.crop(box)
#region.show()


#conversion and filter(BLUR,SHARPEN,SMOOTH) of image
img1=img.filter(ImageFilter.GaussianBlur)
#img1.show()

# convert image to black and white
img2=img.convert('L')
#img2.show()

#rotate a picture
img3=img.rotate(180)
#img3.show()

#thumbnail
img.show()
img.thumbnail((200,200))
img.show()
