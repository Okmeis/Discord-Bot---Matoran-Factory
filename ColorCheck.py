import re

def convHexToRGB(hexCode):
    if re.match(r'^#?([A-Fa-f0-9]{6})$', hexCode):
        if hexCode.startswith("#"):
            hexCode = hexCode[1:]
        r = int(hexCode[0:2], 16)
        g = int(hexCode[2:4], 16)
        b = int(hexCode[4:6], 16)
        return (r, g, b)
    else:
        raise ValueError("String is not a HEX-Color")
