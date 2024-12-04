#!/usr/bin/env python3

import argparse
import subprocess
import skvideo.io
import skimage.io
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Process a file.')
    parser.add_argument('filename', type=str, help='The name of the specification file')
    parser.add_argument('videoFile', type=str, help='The video file to process')
    Path("../../VoxlogicA2/src/frames").mkdir(parents=True, exist_ok=True)
    frames = skvideo.io.vread(args.videoFile + ".mkv", outputdict={"-pix_fmt": "rgba"})
    numFrames = len(frames)
    for i in range(0,len(frames)):
        name = "../../VoxlogicA2/src/frames/video$_" + str(i) + ".png"
        skimage.io.imsave(name, frames[i])

    args = parser.parse_args()

    subprocess.run(['../../VoxLogicA2/src/temporal.py', args.filename, str(numFrames)])

if __name__ == "__main__":
    main()