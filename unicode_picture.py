from picture_utils import PictureUtils


class UnicodePicture:

    def __init__(self, size, font, max_value_char):
        self.unicode_pictures = {}

        for i in range(31, max_value_char):
            self.unicode_pictures[chr(i)] = {'image': PictureUtils(chr(i), size, size, font).image, 'mean': 0.0}

    def str_to_image(self, strings, size, font):
        final_image = None
        for line in strings:
            line_image = None
            for char in line:
                try:
                    temp_image = self.unicode_pictures[char]['image']
                    if line_image is None:
                        line_image = temp_image
                    else:
                        line_image = PictureUtils.juxtapose_h(line_image, temp_image)
                except KeyError:
                    pass
            if final_image is None:
                final_image = line_image
            else:
                if line_image is not None:
                    final_image = PictureUtils.juxtapose_v(final_image, line_image)
        return final_image
