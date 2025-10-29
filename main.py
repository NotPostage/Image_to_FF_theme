import typing
import colorsys
from PIL import Image 
from PIL import ImageColor



with Image.open("./images/1.png").convert("P", palette=Image.Palette.ADAPTIVE, colors=256) as img:
        
    palette = img.getpalette()



