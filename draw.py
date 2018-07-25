from PIL import Image, ImageDraw


class Draw():
    def __init__(self, color_list):
        self.color_list = color_list

    def draw_image(self, name, x, y):
        """
        :param x: width of file
        :param y: height of file
        :param name: name of file
        :return: saves image with bars of color according to list
        """
        im = Image.new('RGB', (x, y))
        vert_increase = y/len(self.color_list)
        hori_increase = x
        x = 0
        y = 0

        draw = ImageDraw.Draw(im)

        for color in self.color_list:
            draw.rectangle([x, y, x + hori_increase, y + vert_increase], fill=color)
            y = y + vert_increase

        im.save("./" + name.upper() + ".png", "PNG")
