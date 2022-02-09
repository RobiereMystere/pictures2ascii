from picture_manager import PictureManager
from unicode_picture import UnicodePicture
from time import perf_counter

FONT = "res/fonts/JetBrainsMono-Regular.ttf"
# FONT = "res/fonts/unifont-14.0.01.ttf"
RATIO = 2
_SIZE = 20
SAVE = True
GEN = True
FIXED_STRING = "ABCD\nEFGH\nIJKL\n‱‱௵௵"
MAX_UNICODE = 144697


def main():
    picture_manager = PictureManager("res/5.png", _SIZE, _SIZE)

    up = UnicodePicture(_SIZE, FONT, MAX_UNICODE)
    final_chars = picture_manager.picture_to_string(_SIZE, up)
    size = _SIZE * RATIO
    image = up.str_to_image(final_chars, size, FONT)
    image.show()
    image.save("final.png")


def add(a, b, c):
    print(a + b + c)


def chronomeister(function, *args):
    start = perf_counter()
    function(*args)
    stop = perf_counter()
    return stop - start


if __name__ == '__main__':
    # print(chronomeister(main))

    print(chronomeister(main))
