from PIL import Image
from Colorizer import dye
from ColorCheck import convHexToRGB
import os
import re

#overlap images
def combineBody(bodyParts):
    body = Image.new('RGBA', bodyParts[0].size, (255, 255, 255, 0))
    for bodyPart in bodyParts:
        body.paste(bodyPart, (0, 0), bodyPart)
    return body

#load an image or at least try to
def loadImage(filePath):
    try:
        img = Image.open(filePath)
        return img
    except IOError:
        print(f"Unable to load {filePath}")
        return None

#generate a picture of a matoran
def generateMatoran(torsoC, footC, eyesC, maskC, maskName):
    maskName = maskName.lower()
    partsDirectory = "parts/"
    fileNames = ["armsTorso", "handsFoot", "masks/"+maskName]
    fileEnding = ".png"
    bodyParts = []
    colors = [torsoC, footC, maskC]
    bodyParts.append(dye(loadImage(partsDirectory+"eyes"+fileEnding), eyesC))
    bodyParts.append(loadImage(partsDirectory+"head"+fileEnding))
    for i in range(len(fileNames)):
        bodyPart = dye(loadImage(partsDirectory+fileNames[i]+fileEnding), colors[i])
        bodyParts.append(bodyPart)
    matoran = combineBody(bodyParts)
    return matoran

#make sure that the parameters describe a MNOG2 style matoran
def isMatoran(torsoC, footC, eyesC, maskC, maskName):
    #important to avoid the usage of ".." and "/" to access private files
    if not re.match(r'^[a-z]{3,6}$', maskName):
        return False, None, None, None, None
    #check if all parameters are valid
    if not os.path.exists("parts/masks/"+maskName+".png"):
        return False, None, None, None, None
    #try convert to (r,g,b), if not possible: return false
    try:
        torsoC = convHexToRGB(torsoC)
        eyesC  = convHexToRGB(eyesC)
        footC  = convHexToRGB(footC)
        maskC  = convHexToRGB(maskC)
    except ValueError as e:
        return False, None, None, None, None
    return True, torsoC, footC, eyesC, maskC