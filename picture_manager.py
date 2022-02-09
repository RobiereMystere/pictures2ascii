from PIL import Image
import numpy as np

from unicode_picture import UnicodePicture


class PictureManager:
    def __init__(self, path, width, height):
        self.image = Image.open(path, 'r')
        self.image.convert("RGB")
        self.pixels = list(self.image.getdata())
        self.pixels = self.h_split(self.pixels, self.image.width)
        print(len(self.pixels))
        self.subdivisions = self.cross_split(self.pixels, width, height)
        print(len(self.subdivisions))

    def picture_to_string(self, size, unicode_picture: UnicodePicture):
        r = ""
        final_chars = [[""]]
        max_width = (self.image.width // size)
        characters = {}
        str_index = 0
        for index in range(len(self.subdivisions)):
            subdivision = self.subdivisions[index]
            pm_img = self.list_to_picture(subdivision)
            min_char = ''
            for char, picture in unicode_picture.unicode_pictures.items():
                picture['mean'] = self.compare(pm_img, picture['image'])
                characters[char] = abs(picture['mean'])
                if characters[char] == 0:
                    min_char = char
                    break
            if min_char == '':
                min_char = min(characters, key=characters.get)

            r += min_char
            final_chars[str_index] += min_char
            if index % max_width == (max_width - 1):
                final_chars.append([""])
                str_index += 1
                r += "\n"
        print(r)
        return final_chars

    def picture_to_string_old(self, size, font):
        final_chars = ""
        characters = {}
        max_width = (self.image.width // (size // 2))

        for index in range(len(self.subdivisions)):

            subdivision = self.subdivisions[index]
            pm_img = self.list_to_picture(subdivision)
            for character, image in UnicodePicture.unicode_pictures.items():
                mean_diff = self.compare(pm_img, image)
                characters[character] = abs(mean_diff)
            min_char = min(characters, key=characters.get)
            print(min_char, end="")
            final_chars += min_char
            if index % max_width == (max_width - 1):
                final_chars += "\n"
                print()
        return final_chars

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
    def compare(picture1, picture2):
        pixels1 = np.array(picture1)
        pixels2 = np.array(picture2).reshape(pixels1.shape)
        diff = 255 * np.absolute(np.subtract(pixels1[:, :, :-1], pixels2[:, :, :-1]))
        mean_diff = np.mean(diff)
        return mean_diff

    @staticmethod
    def compare_old(picture1, picture2):
        pixels1 = list(picture1.getdata())
        pixels2 = list(picture2.getdata())
        pixels1 = PictureManager.h_split(pixels1, picture1.width)
        pixels2 = PictureManager.h_split(pixels2, picture2.width)
        diff = pixels1.copy()
        mean_diff = []
        for i in range(len(pixels1)):
            for j in range(len(pixels1[i])):
                diff[i][j] = PictureManager.pixel_substraction(pixels1[i][j], pixels2[i][j])
                mean_diff.append(PictureManager.list_mean(diff[i][j][:-1]))
        # self.image = PictureManager.list_to_picture(diff)
        mean_diff = PictureManager.list_mean(mean_diff)
        print(mean_diff)
        return mean_diff

    @staticmethod
    def pixel_substraction(pixel1, pixel2):
        result = []
        for i in range(len(pixel1) - 1):
            result.append(pixel1[i] - pixel2[2])
        return tuple(result)

    @staticmethod
    def list_mean(_list):
        if len(_list) == 0:
            return 0
        return sum(_list) / len(_list)
