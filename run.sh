#!/bin/bash

sudo apt-get update
sudo apt-get -y install python3-pip

export GROUP_NUMBER=48

sudo rm -r practica_creativa2

python3 parte1.py