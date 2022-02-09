import datetime

from picture_manager import PictureManager
from unicode_picture import UnicodePicture
from time import perf_counter

FONT = "res/fonts/JetBrainsMono-Regular.ttf"
# FONT = "res/fonts/unifont-14.0.01.ttf"
RATIO = 10
_SIZE = 3
SAVE = True
GEN = True
FIXED_STRING = "ABCD\nEFGH\nIJKL\n‱‱௵௵"
MAX_UNICODE = 100
CHARSET = " azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN,;:!?./§ù*&é'(-è_ç%à)=1234567890°+´~~ê³²¡÷×¿âå€çþýûîô¶¹ÔÎÛðæ±ÊøÂ¬ß®©»«|œ“Œ{[`|\\^@]}"

CHARSET="Bonjour !"
def main():
    picture_manager = PictureManager("res/4.png", _SIZE, _SIZE)

    up = UnicodePicture(_SIZE, FONT, MAX_UNICODE, charset=CHARSET)
    final_chars = picture_manager.picture_to_string(_SIZE, up)
    size = _SIZE * RATIO
    up = UnicodePicture(size, FONT, MAX_UNICODE, charset=CHARSET)

    image = up.str_to_image(final_chars, size, FONT)
    image.show()
    now = datetime.datetime.now()
    image.save(
        str(now.day) + str(now.month) + str(now.year) + str(now.hour) + str(now.minute) + str(now.second) + ".png")


def chronomeister(function, *args):
    start = perf_counter()
    function(*args)
    stop = perf_counter()
    return stop - start


if __name__ == '__main__':
    # print(chronomeister(main))

    print(chronomeister(main))
