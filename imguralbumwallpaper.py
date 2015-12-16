#!/usr/bin/env python2
# encoding: utf-8
# some code taken from
# https://github.com/alexgisby/imgur-album-downloader/blob/master/imguralbum.py

import time
import sys
import re
import urllib
import os
from random import randint

class ImgurPicGetter:
    def __init__(self, album_url):
        self.album_url = album_url
        self.image_urls = []
        match = re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", album_url)
        self.album_key = match.group(4)

        #get noscript page
        fullListURL = "http://imgur.com/a/" + self.album_key + "/layout/blog"

        self.response = urllib.urlopen(url=fullListURL)
        html = self.response.read().decode('utf-8')
        self.imageIDs = re.findall('<div id="([a-zA-Z0-9]+)" class="post-image-container', html)

        for (counter, image) in enumerate(self.imageIDs, start=1):
            image_url = "http://i.imgur.com/"+image+".jpg"
            self.image_urls.append(image_url)
            #print(self.image_urls)


    def setbackground(self):
        key = randint(0, len(self.image_urls)-1)
        thisimage = self.image_urls[key]
        os.system("feh --bg-max " + thisimage)

args = sys.argv
if len(args) > 1:
	inputtedurl = args[1]
else:
	inputtedurl = prompt(text='Enter an imgur album URL', title='Imgur Album Wallpapers')

picgetter = ImgurPicGetter(inputtedurl)
picgetter.setbackground()
