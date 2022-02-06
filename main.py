from character_manager import CharacterManager
from picture_comparer import PictureComparer
from picture_manager import PictureManager

FONT = "res/fonts/JetBrainsMono-Regular.ttf"

if __name__ == '__main__':
    RATIO = 10
    SIZE = 5
    SAVE = False
    SAVE2 = True
    GEN = False

    pm = PictureManager("res/7.png", SIZE, SIZE // 2)
    characters = {}

    stripes = []
    final_chars = ""
    max_width = (pm.image.width // (SIZE // 2))

    if not GEN:
        with open("100.txt", "r", encoding="utf-8") as f:
            final_chars = f.read()
    else:
        for index in range(len(pm.subdivisions)):
            subdivision = pm.subdivisions[index]
            pm_img = pm.list_to_picture(subdivision)
            for i in range(31, 1000):
                character = chr(i)
                cm = CharacterManager(chr(i), SIZE, SIZE, FONT)
                pc = PictureComparer(pm_img, cm.image)
                characters[character] = abs(pc.mean_diff)
            min_char = min(characters, key=characters.get)
            print(min_char, end="")
            final_chars += min_char
            if index % max_width == (max_width - 1):
                final_chars += "\n"
                print()
    if SAVE2:
        final_image = None
        temp_image = None
        index = 0
        SIZE = SIZE * RATIO
        lines = final_chars.split("\n")
        for line in lines:
            line = lines[index]
            line_image = None
            for char in line:
                temp_image = CharacterManager(char, 2*SIZE //5, SIZE, FONT).image
                if line_image is None:
                    line_image = temp_image
                else:
                    line_image = PictureManager.juxtapose_h(line_image, temp_image)
            if final_image is None:
                final_image = line_image
            else:
                if line_image is not None:
                    final_image = PictureManager.juxtapose_v(final_image, line_image)
            index += 1

        final_image.show()
        final_image.save("final.png")

    if SAVE:
        SIZE = SIZE * RATIO
        WIDTH = pm.image.width * RATIO
        for char in final_chars:
            cm = CharacterManager(char, SIZE // 2, SIZE, FONT)
            if temp_image is None:
                temp_image = cm.image
            else:
                temp = PictureManager.juxtapose_h(temp_image, cm.image)
                if temp.width < WIDTH - (SIZE // 2) + 1:
                    temp_image = temp
                else:
                    if final_image is None:
                        final_image = temp_image
                    else:
                        final_image = PictureManager.juxtapose_v(final_image, temp_image)
                        # final_image.show()
                    temp_image = None
        final_image.show()
        final_image.save("final.png")
