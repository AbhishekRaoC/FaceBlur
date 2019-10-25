
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

def findFace(self):
    # Use opencv to find the coordinates of the face in the scence if any
    import opencv
    
    return True

def blurCoordinates(self, image):
    # Using the coordinates of the face, the edge coordinates of face is blurred out
    from PIL import Image, ImageFilter

    coordinates = findFace()
    croppedImage = image.crop(coordinates)
    blurredImage = croppedImage.filter(ImageFilter.GaussianBlur(radius=20))
    image.paste(blurredImage, coordinates)


def stitchImages(self, frameRate, resolution):
    # Stitches all the images together and adds in the audio
    stitchCommand = ("ffmpeg -r ", frameRate, "-s ", resolution, "-i images%04d.png -i videoSound.mp3 -vcodec libx264 -b 4M -vpre normal -acodec copy FinalVideo.mp4 ")
    os.system(stitchCommand)