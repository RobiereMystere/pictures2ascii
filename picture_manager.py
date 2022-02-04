from PIL import Image, ImageDraw
import numpy as np


class PictureManager:
    def __init__(self, path, width, height):
        self.image = Image.open(path, 'r')
        self.pixels = list(self.image.getdata())
        self.pixels = self.h_split(self.pixels, self.image.width)
        print(len(self.pixels))
        self.subdivisions = self.cross_split(self.pixels, width, height)
        print(len(self.subdivisions))

    @staticmethod
    def h_split(list2d, chunk_size):
        result = []
        for index in range(0, len(list2d), chunk_size):
            result.append(list2d[index:index + chunk_size])
        return result

    @staticmethod
    def cross_split(_list, w, h):

        x = []
        for n in range(0, len(_list) // w):
            for m in range(0, len(_list[n * w]) // h):
                t = []
                for i in _list[n * w:(n + 1) * w]:
                    l = []
                    for j in i[m * h:(m + 1) * h]:
                        l.append(j)
                    t.append(l)
                x.append(t)
        return x

    @staticmethod
    def list_to_picture(_list):
        _list = np.array(_list, dtype=np.uint8)
        img = Image.fromarray(_list)
        # img.show()
        return img

    @staticmethod
    def juxtapose_h(picture1, picture2):
        image = Image.new("RGBA", (picture1.width + picture2.width, max(picture1.height, picture2.height)),
                          (255, 255, 255))
        image.paste(picture1, (0, 0))
        image.paste(picture2, (picture1.width, 0))
        return image

    @staticmethod
    def juxtapose_v(picture1, picture2):
        image = Image.new('RGB', (picture1.width, picture1.height + picture2.height))
        image.paste(picture1, (0, 0))
        image.paste(picture2, (0, picture1.height))
        return image
