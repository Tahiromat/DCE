import cv2
import numpy
from PIL import Image


class ImageProcessingModel:
    def __init__(self):
        pass

    def load_bgr_image(self, file):
        return Image.open(file)

    def load_rgb_image(self, file, image_path):
        image = cv2.imread(image_path + "/" + file.name)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def get_r_g_b_pixel_values(self, image):

        r = image[:, :, 0]
        g = image[:, :, 1]
        b = image[:, :, 2]

        cond = r[:, :] > 255
        r[cond] = r[cond] - 255

        cond = g[:, :] > 255
        g[cond] = g[cond] - 255

        cond = b[:, :] > 255
        b[cond] = b[cond] - 255

        return r, g, b

    def increase_pixel_values(self, image, red_value, green_value, blue_value):
        r, g, b = self.get_r_g_b_pixel_values(image)

        r = r + red_value
        g = g + green_value
        b = b + blue_value

        image[:, :, 0] = r
        image[:, :, 1] = g
        image[:, :, 2] = b

        return image

    def resize_image(self, image, height, width):
        return cv2.resize(image, (height, width), interpolation=cv2.INTER_AREA)

    def reshape_image(self, image):
        return numpy.reshape(image, (-1, 3))
