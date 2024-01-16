import processing
import draw
import sys
import os

if __name__ == "__main__":
    file_name = input("Place the file you wish to convert in the 'input' folder and type its name: ")
    poster_name = input("Name your poster png: ")
    num_stills = int(input("Enter the number of layers you want your image to have: "))
    vp = processing.VideoProcessor(file_name)
    frames = vp.get_n_stills(num_stills)
    ip = processing.ImgProcessor(frames)
    color_list = ip.average_list()

    draw = draw.Draw(color_list)
    draw.draw_image("output/" + poster_name, 3900, 5700)

    exit(0)
