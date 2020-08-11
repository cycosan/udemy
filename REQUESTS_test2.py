import requests
from PIL import Image
from io import BytesIO
r=requests.get("https://wallpaperaccess.com/full/1631809.jpg")
image=Image.open(BytesIO(r.content))
path='./imags.'+image.format
image.save(path,image.format)