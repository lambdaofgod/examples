import PIL
import numpy as np


img_path = 'data/123033/0e27621e3f8b484c993619abd064948be27f60a2.jpg'
img = PIL.Image.open(img_path)
img_array = np.asarray(img)
print(img_array.shape)
