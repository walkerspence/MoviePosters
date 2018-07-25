import unittest as test
import cv2
import draw as d
import processing


class TestDraw(test.TestCase):
    def test_draw(self):
        draw = d.Draw(["#A250B2", "#B2B250", "#5054B2"])
        draw.draw_image("test", 1000, 1000)

    def test_draw_from_video(self):
        file_name = "test.mp4"
        vp = processing.VideoProcessor(file_name)
        frames = vp.get_n_stills(12)
        ip = processing.ImgProcessor(frames)
        color_list = ip.average_list()

        draw = d.Draw(color_list)
        draw.draw_image("poster", 3900, 5700)