import typing
import colorsys
from PIL import Image 
from PIL import ImageColor




with Image.open("./images/1.png").convert("P", palette=Image.Palette.ADAPTIVE, colors=256) as img:
    # hlsList = []
    palette = img.getpalette()
    # convert flat palette [r,g,b, r,g,b, ...] to list of (r,g,b) tuples
    rgbPalette = []
    if palette is None:
        pass
    else:
        rgbPalette = [(palette[i], palette[i+1], palette[i+2]) for i in range(0, len(palette), 3)]

        # convert to HLS using colorsys (inputs 0..1, outputs h,l,s in 0..1)
        hlsPalette = set([colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0) for r, g, b in rgbPalette])

        filterPalette = sorted([color for color in hlsPalette if color[2] > 0.5 and color[1] > 0.7], key=lambda c:c[0])
        print(filterPalette)
        print(len(filterPalette))

        # optional: convert to human-friendly units (H in degrees, L and S in percent)
        # hls_degrees = [(h * 360.0, l * 100.0, s * 100.0) for h, l, s in hls_palette]

        # store or inspect
        # hlsList = hls_palette
        # print("first 10 HLS (deg, L%, S%):", [tuple(map(lambda x: round(x, 2), v)) for v in hls_degrees[:10]])



