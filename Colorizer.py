def dye(img, color):
    image = img.convert("RGBA")
    data = image.getdata()
    newData = []
    for item in data:
        #check transparency
        if item[3] == 0:
            newData.append(item)  #add transparency
        else:
            newColor = (
                int((item[0]/255*color[0])),
                int((item[1]/255*color[1])),
                int((item[2]/255*color[2])),
                item[3],
            )
            newData.append(newColor)
    image.putdata(newData)
    return image