from PIL import Image, ImageDraw
import face_recognition
import numpy

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

image = Image.open(args.input)
array = numpy.array(image)
locations = face_recognition.face_locations(array)
draw = ImageDraw.Draw(image)
for location in locations:
    y0, x1, y1, x0 = location
    draw.rectangle((x0, y0, x1, y1), outline='red')
image.save(args.output)
