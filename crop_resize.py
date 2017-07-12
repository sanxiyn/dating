import fractions
import os

from tqdm import tqdm
from wand.image import Image
import attr

@attr.s
class Size(object):
    width = attr.ib()
    height = attr.ib()

    def aspect_ratio(self):
        return fractions.Fraction(self.width, self.height)

def parse_size(size):
    width, height = size.split('x')
    width, height = int(width), int(height)
    return Size(width, height)

def read(dirname):
    result = []
    for filename in os.listdir(dirname):
        path = os.path.join(dirname, filename)
        if os.path.isfile(path):
            result.append(path)
    return result

def process(paths, args):
    original = parse_size(args.original)
    crop = parse_size(args.crop)
    resize = parse_size(args.resize)
    if crop.aspect_ratio() != resize.aspect_ratio():
        raise Exception('different aspect ratio')
    for path in paths:
        with Image(filename=path) as image:
            if image.size != attr.astuple(original):
                error = '{} is {}x{}'.format(path, image.width, image.height)
                raise Exception(error)
    for path in tqdm(paths):
        filename = os.path.basename(path)
        save_path = os.path.join(args.output, filename)
        with Image(filename=path) as image:
            image.crop(width=crop.width, height=crop.height, gravity='center')
            image.resize(resize.width, resize.height)
            image.save(filename=save_path)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('original', help='original size, e.g. 330x470')
parser.add_argument('crop', help='cropped size, e.g. 330x440 (center crop is used)')
parser.add_argument('resize', help='resized size, e.g. 240x320 (should preserve aspect ratio)')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

paths = read(args.input)
process(paths, args)
