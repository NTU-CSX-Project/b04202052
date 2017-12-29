#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:06:02 2017

@author: allen
"""

from snownlp import SnowNLP
import jieba.analyse
import jieba.posseg as pseg

jieba.set_dictionary('dict.txt')

lyric=u"我們在原野上找一面牆 我們在標籤裡找方向 我們在廢墟般的垃圾裡找一塊紅磚 \
我們在工整的巷子裡找家 找家 找 我們義無反顧的試著後悔 我們聲嘶力竭的假裝吶喊 我們萬分惋惜的浪費著 \
用盡一切換來的紙張 用盡一切換來的紙張 用盡一切"


def lyric_sentiment(lyric):
    lyric=lyric.replace("\n\n","\n",100)
    lyric=lyric.replace(" ","，",100)
    lyric=lyric.replace("　","，",100)
    lyric=lyric.replace("\n","，",100)
    lyric=lyric.replace("－","",100)
    lyric_s=SnowNLP(lyric)
    score=1
    for i in range(len(lyric_s.sentences)):
        #print(lyric_s.sentences[i],end="\t")
        #print(SnowNLP(lyric_s.sentences[i]).sentiments)
        if abs(SnowNLP(lyric_s.sentences[i]).sentiments-0.5)<0.25:pass
        else:
            score+=((SnowNLP(lyric_s.sentences[i]).sentiments-0.5)/abs((SnowNLP(lyric_s.sentences[i]).sentiments-0.5)))
    if score>0:
        print("這是一首開心的歌")
    else:
        print("這不是一首開心的歌")

for x, w in jieba.analyse.extract_tags(lyric, withWeight=True):
    if w>1:
        print('本首歌關鍵字：%s'%x)
    

lyric_sentiment(lyric)
