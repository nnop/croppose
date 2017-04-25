#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sample a small part of a dataset for downloading
input:
    input folder name
output:
    new output folder under output_root folder
"""
from os import path
import argparse
from glob import glob
import random
import shutil
import logging

from .lib import config_logger

def get_data_dirs(d):
    return path.join(d, 'Frame'), path.join(d, 'xml')

def sample_part(in_root_dir, out_root_dir, sub_d, num):
    src_image_dir, src_xml_dir = get_data_dirs(path.join(in_root_dir, sub_d))
    dst_image_dir, dst_xml_dir = get_data_dirs(path.join(out_root_dir, sub_d))

    # get images
    image_list = glob(src_image_dir, '*.jpg')
    image_list = random.sample(image_list, num)
    for src_image_path in image_list:
        image_fn = path.split(src_image_path)[1]
        xml_fn = path.splitext(image_fn)[0]+'.xml'
        src_xml_path = path.join(src_xml_dir, xml_fn)
        dst_image_path = path.join(dst_image_dir, image_fn)
        dst_xml_path = path.join(dst_xml_dir, xml_fn)
        shutil.copyfile(src_image_path, dst_image_path)
        shutil.copyfile(src_xml_path, dst_xml_path)
        logging.info('{} -> {}'.format(src_image_path, dst_image_path))
        logging.info('{} -> {}'.format(src_xml_path, dst_xml_path))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('in_root_dir', help='input folder containing training data')
    parser.add_argument('out_root_dir', help='output folder created under this folder')
    args = parser.parse_args()
    config_logger()

    # select N samples and output to dest folder
    sub_dirs = ['training/classroom1',
                'validation/classroom1',
                'validation/classroom2']
    for sub_d in sub_dirs:
        sample_part(in_root_dir, out_root_dir, sub_d, 10)
