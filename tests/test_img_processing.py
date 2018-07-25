import unittest as test
import numpy as np
import cv2
import processing


class TestImgProcessing(test.TestCase):
    def test_bgr_to_hex(self):
        rgb1 = np.asarray([50, 50, 50], dtype=np.float64)
        rgb2 = np.asarray([0, 0, 0], dtype=np.float64)
        rgb3 = np.asarray([127, 254, 35], dtype=np.float64)
        rgb4 = np.asarray([127, 254, 5], dtype=np.float64)

        ip = processing.ImgProcessor([])
        self.assertEqual("#323232", ip.bgr_to_hex(rgb1))
        self.assertEqual("#000000", ip.bgr_to_hex(rgb2))
        self.assertEqual("#23FE7F", ip.bgr_to_hex(rgb3))
        self.assertEqual("#05FE7F", ip.bgr_to_hex(rgb4))

    def test_average_color(self):
        img_list = [cv2.imread("input/test1.png"), cv2.imread("input/test2.png"), -1]
        ip = processing.ImgProcessor(img_list)
        self.assertEqual("#777777", ip.average_color(img_list[0]))
        self.assertEqual("#6464A0", ip.average_color(img_list[1]))

    def test_average_list(self):
        file_name = "test.mp4"
        vp = processing.VideoProcessor(file_name)
        frames = vp.get_n_stills(12)
        ip = processing.ImgProcessor(frames)
        color_list = ip.average_list()

        for color in color_list[0:4]:
            self.assertEqual("#C08E4C", color)

        for color in color_list[4:8]:
            self.assertEqual("#3BAE3F", color)

        for color in color_list[8:12]:
            self.assertEqual("#395391", color)


        #frames 1-4 #c08e4c
        #frames 5-8 #3cae3f
        #frames 9-12 #395390




    # test1 avg = 0x777777
    # test2 avg = 0x6464A0

