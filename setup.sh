#!/bin/bash
echo "Running setup..."
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    echo "usage: ./setup.sh <imagename>
fi
docker build -t secplus.app --build-arg MY_IMAGE=$1