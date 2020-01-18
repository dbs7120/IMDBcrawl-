from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'count.txt'), encoding='UTF8').read()

# read the mask image
# taken from
img_mask = np.array(Image.open(path.join(d, "superman_mask.png")))

wc = WordCloud(background_color="black", max_words=200, mask=img_mask, contour_width=2, contour_color='white')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "superman.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
wc.generate(text)
plt.figure()
plt.imshow(img_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()