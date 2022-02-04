from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


class CharacterManager:
    def __init__(self, character, width, height, font=None):
        self.character = character
        self.font = ImageFont.truetype(font, width)
        if self.font is None:
            self.font = ImageFont.truetype("res/Noto_Sans/NotoSans-Regular.ttf", width)

        img = Image.new("RGBA", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), character, (0, 0, 0), font=self.font)
        self.image = img
        #img.show()
