#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:41:28 2017

@author: allen
"""
import cv2
from darkflow.net.build import TFNet

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

options = {"model": "cfg/yolo.cfg",
           "load": "bin/yolo.weights",
           "threshold": 0.3}
tfnet = TFNet(options)

video=cv2.VideoCapture('/Volumes/Transcend/opencv/IMG_0390.m4v')

while(video.isOpened()):
    ret,img=video.read()
    predictions = tfnet.return_predict(img)
    for i in range(len(predictions)):
        cv2.rectangle(img,(predictions[i]['topleft']['x'],predictions[i]['topleft']['y']),\
                      (predictions[i]['bottomright']['x'],predictions[i]['bottomright']['y']),\
                      (0,255,0),int(13*abs(predictions[i]['topleft']['y']-predictions[i]['bottomright']['y'])/1805))
        cv2.putText(img,predictions[i]['label'],(predictions[i]['topleft']['x'],predictions[i]['bottomright']['y']),\
                    cv2.FONT_HERSHEY_SIMPLEX,int(6*abs(predictions[i]['topleft']['y']-predictions[i]['bottomright']['y'])/1859),(255,255,255),int(15*abs(predictions[i]['topleft']['y']-predictions[i]['bottomright']['y'])/1859),cv2.LINE_AA)
    height,width=img.shape[:2]
    img_re=cv2.resize(img,(int(width/2),int(height/2)),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('test',img_re)
    if cv2.waitKey(1) and 0xFF==ord('q'):
        break
    cv2.destroyAllWindows()