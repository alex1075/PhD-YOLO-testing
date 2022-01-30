#!/bin/bash

echo "Starting buildinh docker images"
PS3='Select building os architechture: '
option=("arm64" "amd64" "tensorboard" "Quit")
select fav in "${option[@]}"; do
    case $fav in
        "amd64")
            echo "Building dockerfile for amd64"
            docker build . -t alex1075/phd:latest -f Dockerfiles/Tensorflow/Dockerfile && docker build . -t alex1075/phd:latest-gpu -f Dockerfiles/Tensorflow-GPU/Dockerfile 
            docker push alex1075/phd:latest && docker push alex1075/phd:latest-gpu
            ;;
        "arm64")
            echo "Building dockerfile for arm64"
            docker build . -t alex1075/phd:latest-arm -f Dockerfiles/Tensorflow-arm/Dockerfile
            docker push alex1075/phd:tensorboard
            ;;
        "tensorboard")
            echo "Building dockerfile for tensorboard agnostic"
            docker build . -t alex1075/phd:tensorboard -f Dockerfiles/Tensorboard/Dockerfile
            docker push alex1075/phd:latest-arm
            ;;
        "Quit")
            echo "User requested exit"
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
