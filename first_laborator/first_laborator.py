import glob
import numpy
import matplotlib
from skimage import io

matplotlib.use('TkAgg')
io.use_plugin('matplotlib')

# ex.1
cars = []
images = glob.glob('images/*.npy')

for img in images:
    cars.append(numpy.load(img))

united_images = numpy.concatenate(cars)
io.imshow(united_images.astype(numpy.uint8))

if __name__ == '__main__':
    print(io.show())
