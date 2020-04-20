import sys
from PIL import Image

SIZE   = 690

image1 = Image.open(sys.argv[1])
image2 = Image.open(sys.argv[2])

w1, h1 = image1.size
w2, h2 = image2.size

print str(SIZE - w1) + "." + str(SIZE - h1) + "." + str(SIZE - w2) + "." + str(SIZE - h2)
