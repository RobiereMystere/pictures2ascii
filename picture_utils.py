from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


class PictureUtils:
    def __init__(self, character, width, height, font=None):
        self.character = character
        self.font = ImageFont.truetype(font, width)
        if self.font is None:
            self.font = ImageFont.truetype("res/Noto_Sans/NotoSans-Regular.ttf", width)

        img = Image.new("RGBA", (width , height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), character, (0, 0, 0), font=self.font)
        self.image = img
        # img.show()

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
