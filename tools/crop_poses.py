#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
crop poses and encode the label in saved file name.
"""
import argparse
import os
from os import path
import shutil
import logging
import cv2

from lib.util import config_logger
from lib.voc_parser import VOCParser
from lib.dataset import image_to_xml_path, xml_to_image_path

if __name__ == "__main__":
    config_logger('crop_poses.log')
    # parse arguments
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--xml', help='xml path')
    group.add_argument('--image', help='image path')
    parser.add_argument('--data-dir', default='',
            help='root folder of frame images')
    parser.add_argument('--save-dir', required=True,
            help='folder to store the cropped pose images')
    args = parser.parse_args()
    save_dir = args.save_dir
    data_dir = args.data_dir
    if args.xml:
        xml_path = path.join(data_dir, args.xml)
        img_path = xml_to_image_path(xml_path)
    else:
        img_path = path.join(data_dir, args.image)
        xml_path = image_to_xml_path(img_path)
    
    if not path.isdir(save_dir):
        logging.info('creating folder: {}'.format(save_dir))
        os.mkdir(save_dir)

    # crop 
    fn_main_name = str(abs(hash(path.splitext(xml_path)[0])))
    im_frame = cv2.imread(img_path)
    voc = VOCParser(xml_path)
    for i, obj in enumerate(voc.objects):
        name = obj['name']
        bbox = obj['bbox']
        im_pose = im_frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
        out_fn = '{}-{}-{}.jpg'.format(fn_main_name, i, name)
        out_path = path.join(save_dir, out_fn)
        cv2.imwrite(out_path, im_pose)
        logging.info('save to {}'.format(out_path))
