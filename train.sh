#!/bin/bash

echo "Starting training"
echo "Testing if folders are present"
mkdir -p data/train/
mkdir -p data/valid/
mkdir -p data/test/
echo "Testing tensorflow"
python -c "from helper import *; tf_test()"
echo "Training starting:"
python train.py | tensorboard --logdir data/logs --bind_all
