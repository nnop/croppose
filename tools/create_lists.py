#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create train/val lists
"""
import argparse
import logging
import os
from os import path
from glob import glob
import random

from lib.util import config_logger

name_to_label = {
    'listen' : 0,
      'read' : 1,
     'write' : 2,
    'handup' : 3,
     'twist' : 4,
      'play' : 5,
}

if __name__ == "__main__":
    config_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument('--list-dir', required=True,
            help='folder to save lists.')
    parser.add_argument('--data-dir', required=True,
            help='data folder containing pose images')
    args = parser.parse_args()
    data_dir = args.data_dir
    list_dir = args.list_dir
    assert path.isdir(data_dir), '{} not exists.'.format(data_dir)
    if not path.isdir(list_dir):
        logging.info('creating folder: {}'.format(list_dir))
        os.mkdir(list_dir)

    # get all pose images
    pose_files = glob(path.join(data_dir, '*.jpg'))
    # parse file name
    lines = []
    for p in pose_files:
        fn = path.split(p)[1]
        main_name = path.splitext(fn)[0]
        _, _, label_name = main_name.split('-')
        label = name_to_label[label_name]
        lines.append('{} {}\n'.format(fn, label))

    # split lists
    random.shuffle(lines)
    n_lines = len(lines)
    n_tr = int(0.8*n_lines)
    n_te = n_lines - n_tr
    tr_lines = lines[:n_tr]
    te_lines = lines[n_tr:]
    tr_list_path = path.join(list_dir, 'train_list.txt')
    te_list_path = path.join(list_dir, 'test_list.txt')
    with open(tr_list_path, 'w') as f:
        f.writelines(tr_lines)
    logging.info('save {}'.format(tr_list_path))
    with open(te_list_path, 'w') as f:
        f.writelines(te_lines)
    logging.info('save {}'.format(te_list_path))
