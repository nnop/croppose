#!/bin/sh
set -e

echo "Creating train lmdb..."

TOOLS=$CAFFEROOT/build/tools
RESIZE_HEIGHT=256
RESIZE_WIDTH=256

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    data/ \
    lists/train_list.txt \
    lmdb/train_lmdb

echo "Creating test lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    data/ \
    lists/test_list.txt \
    lmdb/test_lmdb

echo "Done."
