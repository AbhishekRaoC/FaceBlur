"""
-Takes in a video clip
-In each scene it looks for faces
-Using the coordinates it blurs the face region
-Then searches the next scene
-Finally stitches all images into one video
"""

import os

def breakVideo(self, video):
    # Takes video and separates it frame by frame
    audioCommand = ("ffmpeg -i ", video, "videoSound.mp3")
    imageCommand = ("ffmpeg -i ", video, "images%06d.jpg -hide_banner")
    os.system(audioCommand)
    os.system(imageCommand)
    return(True)

def stitchImages(self, frameRate, resolution):
    stitchCommand = ("ffmpeg -r ", frameRate, "-s ", resolution, "-i images%04d.png -i videoSound.mp3 -vcodec libx264 -b 4M -vpre normal -acodec copy FinalVideo.mp4 ")
    os.system(stitchCommand)