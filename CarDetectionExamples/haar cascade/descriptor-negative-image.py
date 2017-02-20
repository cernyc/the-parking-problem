#!/usr/bin/python

import urllib
import cv2
import numpy as np
import os
import httplib

for file_type in ['neg']:

    for img in os.listdir(file_type):

        if file_type == 'pos':
            line = file_type + '/' + img + ' 1 0 0 50 50\n'
            with open('info.dat', 'a') as f:
                f.write(line)
        elif file_type == 'neg':
            line = file_type + '/' + img + '\n'
            with open('bg.txt', 'a') as f:
                f.write(line)