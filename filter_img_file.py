import os
from PIL import Image
import filetype

imgs = list(os.walk("./pics"))[0][2]

for f in imgs:
    fn = "pics/" + f
    kind = filetype.guess(fn)
    if kind is None:
        print('Cannot guess file type!')
        os.remove(fn)
    elif kind.extension == "gif":
        os.remove(fn)
    else:
        img = Image.open(fn)
        if img.width != img.height:
            img.close()
            os.remove(fn)
        elif img.width < 200:
            img.close()
            os.remove(fn)
