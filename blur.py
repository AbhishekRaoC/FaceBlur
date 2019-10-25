
class findAndBlur:
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