import unittest as test
import cv2
import numpy
import processing


class TestVideoProcessing(test.TestCase):
    def test_file(self):
        file_name = "test.mp4"
        vp = processing.VideoProcessor(file_name)
        self.assertEqual("input/test.mp4", vp.file_path)
        self.assertAlmostEqual(30, round(vp.fps))
        self.assertEqual(360, vp.frame_count)
        self.assertTrue(type(vp.capture) is cv2.VideoCapture)

    def test_get_frame_at(self):
        file_name = "test.mp4"
        vp = processing.VideoProcessor(file_name)
        frame = vp.frame_at_index(0)
        self.assertIsNotNone(frame)
        self.assertTrue(type(frame) is numpy.ndarray)

    def test_get_n_stills(self):
        file_name = "test.mp4"
        vp = processing.VideoProcessor(file_name)
        frames = vp.get_n_stills(12)
        ip = processing.ImgProcessor(frames)

