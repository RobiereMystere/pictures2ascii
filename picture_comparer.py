from picture_manager import PictureManager
from PIL import Image
from PIL import ImageChops


class PictureComparer:
    def __init__(self, picture1, picture2):
        pixels1 = list(picture1.getdata())
        pixels2 = list(picture2.getdata())
        pixels1 = PictureManager.h_split(pixels1, picture1.width)
        pixels2 = PictureManager.h_split(pixels2, picture2.width)
        diff = pixels1.copy()
        mean_diff = []
        for i in range(len(pixels1)):
            for j in range(len(pixels1[i])):
                diff[i][j] = self.pixel_substraction(pixels1[i][j], pixels2[i][j])
                mean_diff.append(self.list_mean(diff[i][j][:-1]))
        self.image = PictureManager.list_to_picture(diff)
        self.mean_diff = self.list_mean(mean_diff)

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
