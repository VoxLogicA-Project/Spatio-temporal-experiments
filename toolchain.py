#!/usr/bin/env python3

import argparse
import subprocess
import skvideo.io
import skimage.io
import numpy
import os
numpy.float = numpy.float64
numpy.int = numpy.int_
from pathlib import Path

def main():
    """
    The main entry point of the toolchain.

    The toolchain takes two arguments, a specification file and a video file.
    It will extract the specified number of frames from the video, save them
    as rgba images in the frames directory, and then run the temporal
    analysis on the frames.

    Args:
        filename (str): The name of the specification file
        videoFile (str): The name of the video file
    """
    parser = argparse.ArgumentParser(description='Process a file.')
    parser.add_argument('filename', type=str, help='The name of the specification file')
    parser.add_argument('videoFile', type=str, help='The video file to process')

    args = parser.parse_args()
    
    Path("/home/ubuntu/VoxLogicA2/src/frames").mkdir(parents=True, exist_ok=True)
    frames = skvideo.io.vread(args.videoFile + ".mkv", outputdict={"-pix_fmt": "rgba"})
    print(len(frames))
    numFrames = 400
    
    for i in range(0,numFrames):
        name = "/home/ubuntu/VoxLogicA2/src/frames/video_" + str(i) + ".png"
        skimage.io.imsave(name, frames[i])

    args = parser.parse_args()
    spec = args.filename.split(".")[0]
    #spec = spec2.split("/")[-1]

    os.chdir("/home/ubuntu/VoxLogicA2/src")
    subprocess.run("python3 temporal.py " + args.filename + " " + str(numFrames), shell=True)
    subprocess.run("cp stdlib2.imgql /home/ubuntu/VoxLogicA/src", shell=True)

    os.chdir("/home/ubuntu/VoxLogicA/src")

    subprocess.run("rm -rf frames", shell=True)
    subprocess.run("mv /home/ubuntu/VoxLogicA2/src/frames /home/ubuntu/VoxLogicA/src", shell=True)
    subprocess.run("mv /home/ubuntu/VoxLogicA2/src/" + spec + "-temporal-new-VL1.imgql /home/ubuntu/VoxLogicA/src", shell=True)
    subprocess.run("/home/ubuntu/VoxLogicA/releases/VoxLogicA_1.3.3-experimental_linux-x64/VoxLogicA " + spec + "-temporal-new-VL1.imgql", shell=True)

if __name__ == "__main__":
    main()