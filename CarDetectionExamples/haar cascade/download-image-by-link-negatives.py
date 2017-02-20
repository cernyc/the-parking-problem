#!/usr/bin/python

import urllib
import cv2
import numpy as np
import os
import sys
import glob


path1 = "the-parking-problem/CarDetectionExamples/pictures/garagepic/bg/*.jpg"
path2 = "the-parking-problem/CarDetectionExamples/haar cascade/neg/"

script_dir = sys.path[0]
for file in glob.glob("D:/TravelMonster/PycharmProject/the-parking-problem/CarDetectionExamples/haar cascade/pos/*"):
    print(file)
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

         # should be larger than samples / pos pic (so we can place our image on it)

    if img != None:
        resized_image = cv2.resize(img, (100, 100))
        cv2.imwrite(file, resized_image)



#### Below is what we will use if taking images from a site for negatives
#'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
#'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
# neg_images_link = ''
#
# neg_image_urls = urllib.urlopen(neg_images_link).read().decode()
# pic_num = 816
#
# if not os.path.exists('neg'):
#     os.makedirs('neg')
#
# for i in neg_image_urls.split('\n'):
#
#     try:
#         print(i)
#         try:
#             r = urllib.urlopen(i).getcode()
#         except IOError:
#             print "error opening " + str(r)
#             continue
#
#         print r
#         if r == 200:
#             urllib.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
#             img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
#
#         # should be larger than samples / pos pic (so we can place our image on it)
#
#             if img != None:
#                 resized_image = cv2.resize(img, (100, 100))
#                 cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)
#                 pic_num += 1
#
#      except Exception as e:
#          print(str(e))








