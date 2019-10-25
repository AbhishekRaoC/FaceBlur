
"""
-Takes in a video clip
-In each scene it looks for faces
-Using the coordinates it blurs the face region
-Then searches the next scene
-Finally stitches all images into one video
"""
import os

def breakVideo(video):
    audioCommand = ("ffmpeg -i ", video, "videoSound.mp3")
    imageCommand = ("ffmpeg -i ", video, "images%06d.jpg -hide_banner")
    os.system(audioCommand)
    os.system(imageCommand)
    return(True)

def findFace():
    faceCoordinates = 1
    return(faceCoordinates)

def blurCoordinates():
    liveImage = 1
    return(liveImage)

def stitchImages(frameRate, resolution):
    stitchCommand = ("ffmpeg -r ", frameRate, "-s ", resolution, "-i images%04d.png -i videoSound.mp3 -vcodec libx264 -b 4M -vpre normal -acodec copy FinalVideo.mp4 ")
    os.system(imageCommand)
