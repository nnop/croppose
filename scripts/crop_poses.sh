#!/bin/sh
cat all_jpgs.txt | xargs -I{} -P 8 \
tools/crop_poses.py --data-dir dataset/ --save-dir data/ \
  --image {}
