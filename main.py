from character_manager import CharacterManager
from picture_comparer import PictureComparer
from picture_manager import PictureManager

FONT = "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf"

if __name__ == '__main__':
    SIZE = 10
    SAVE = True
    pm = PictureManager("res/4.png", SIZE, SIZE // 2)
    characters = {}
    final_image = None
    temp_image = None
    stripes = []
    final_chars = []
    for subdivision in pm.subdivisions:

        pm_img = pm.list_to_picture(subdivision)
        for i in range(31, 200):
            character = chr(i)
            cm = CharacterManager(chr(i), SIZE, SIZE, FONT)

            pc = PictureComparer(pm_img, cm.image)
            characters[character] = abs(pc.mean_diff)
        min_char = min(characters, key=characters.get)
        print(min_char, end="")
        final_chars.append(min_char)
        max_width = (pm.image.width // (SIZE // 2))
        if len(final_chars) % max_width == (max_width - 1):
            print()

    if SAVE:
        for char in final_chars:
            cm = CharacterManager(char, SIZE // 2, SIZE, FONT)
            if temp_image is None:
                temp_image = cm.image
            else:
                temp = PictureManager.juxtapose_h(temp_image, cm.image)
                if temp.width < pm.image.width - (SIZE // 2):
                    temp_image = temp
                else:

                    if final_image is None:
                        final_image = temp_image
                    else:
                        final_image = PictureManager.juxtapose_v(final_image, temp_image)
                        # final_image.show()

                    temp_image = None
    if SAVE:
        final_image.save("final.png")
