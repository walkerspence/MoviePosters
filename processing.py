import numpy as np
import cv2

class VideoProcessor:
    def __init__(self, file_name):
        self.file_path = "input/" + file_name
        self.capture = cv2.VideoCapture(self.file_path)
        self.frame_count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.capture.get(cv2.CAP_PROP_FPS)

    def get_n_stills(self, n):
        """
        gets n stills evenly spread through current video object
        :param n: number of stills
        :return: array of image objects with length n
        """
        interval = int(self.frame_count / n)
        frames = []

        for i in range(0, self.frame_count, interval):
            frames += [self.frame_at_index(i)]

        return frames

    def frame_at_index(self, index):
        """
        get the frame at index
        :param index: index of frame
        :return: image of frame
        """
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, index)
        ret, frame = self.capture.read()

        return frame

class ImgProcessor:
    def __init__(self, image_list):
        self.image_list = image_list

    def average_list(self):
        color_list = []

        for image in self.image_list:
            color = [self.average_color(image)]
            color_list += color

        return color_list

    def average_color(self, image):
        """
        :param image: image to get average color of
        :return: average color in html format
        """
        avg_color_per_row = np.average(image, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        return self.bgr_to_hex(avg_color)

    @staticmethod
    def bgr_to_hex(bgr):
        """
        :param bgr: np ndarray with r, g, b values
        :return: hex code for the same color
        """
        bgr = bgr.astype(int)
        bgr_hex = []
        pad_strip_hex = lambda hex_val: hex_val[2:] if len(hex_val[2:]) == 2 else "0" + hex_val[2:]

        brightness_coefficient = 0;
        for i in range(bgr.size):
            hex_str = str(hex(bgr.item(i) + brightness_coefficient))
            bgr_hex += [pad_strip_hex(hex_str)]

        rgb_hex = "#" + bgr_hex[2] + bgr_hex[1] + bgr_hex[0]

        return rgb_hex.upper()
