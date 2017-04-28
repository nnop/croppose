#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
show objects and names of an image
"""
import argparse
import sys
from os import path
import random
import cv2
import matplotlib.pyplot as plt

from lib.config import cfg
from lib.voc_parser import VOCParser
from lib.draw import draw_bbox
from lib.dataset import xml_to_image_path, image_to_xml_path

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--xml', help='xml path')
    group.add_argument('--image', help='image path')
    args = parser.parse_args()
    if args.xml:
        xml_path = args.xml
        img_path = xml_to_image_path(args.xml)
    else:
        img_path = args.image
        xml_path = image_to_xml_path(args.image)

    assert path.isfile(xml_path), '{} not exists.'.format(xml_path)
    assert path.isfile(img_path), '{} not exists.'.format(img_path)

    # get image size from xml
    voc_xml = VOCParser(xml_path)
    hei_xml, wid_xml, ch_xml = voc_xml.size

    # verify image size
    im = cv2.imread(img_path)[:, :, [2, 1, 0]]
    hei, wid, ch = im.shape
    if not (hei_xml == hei and wid_xml == wid and ch_xml == ch):
        print 'WARNING: size wrong in {}.'.format(xml_path)

    # show each object
    colors = plt.cm.hsv
    plt.imshow(im)
    ax = plt.gca()
    for obj in voc_xml.objects:
        name = obj['name']
        bbox = obj['bbox']
        draw_bbox(ax, bbox, text=name, color=colors(random.random()))

    out_fn = path.split(xml_path)[1][:-4]+'.pdf'
    plt.savefig(out_fn)
    print 'save {} bbox to {}'.format(len(voc_xml.objects), out_fn)

