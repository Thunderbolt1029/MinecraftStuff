import time, os, mouse, countdown, threading
from PIL import ImageGrab

countdown = countdown.countdown()

mithrilMined=titaniumMined=diamondMined=0

mithril = (235, 193, 189)
titanium = (183, 194, 211)
diamond = (136, 63, 79)

(mithrilR, mithrilG, mithrilB) = mithril
(titaniumR, titaniumG, titaniumB) = titanium
(diamondR, diamondG, diamondB) = diamond

mineableOreList = """Mineable ore list:
[1]  Mithril and Titanium
[2]  Diamond"""

validOre = False
while validOre!=True:
    try:
        print(mineableOreList, end="\n\n")
        ore = input("Which ore would you like to mine? ")
        if ore=="1" or ore.lower()=="mithril and titanium":
            print("Mining for Mithril and Titanium")
            ore=1
        elif ore=="2" or ore.lower()=="diamond":
            print("Mining for Diamond")
            ore=2
        else:
            raise Exception("Not an ore in the list")
    except:
        print("The chosen ore has to be in the list")
        time.sleep(1)
        print("")
    else:
        validOre=True
        print("")

errorRangeInt = False
while errorRangeInt!=True:
    try:
        errorRange = input("Set your error margin: ")
        errorRange = int(errorRange)
    except:
        print("The error margin has to be a positive integer", end="\n\n")
    else:
        errorRangeInt=True
        print("")

countdown.start(5)

def pickobulous():
    while True:
        mouse.right_click()
        time.sleep(3.5)
        mouse.right_click()
        time.sleep(3.5)
        mouse.right_click()
        print("              PICKOBULOUS")
        time.sleep(120)

threading.Thread(target=pickobulous).start()

if ore==1:
    while True:
        blockMined = False
        image = ImageGrab.grab()
        color = image.getpixel((840, 516))
        (r, g, b) = color
        if (mithrilR-errorRange<=r<=mithrilR+errorRange and mithrilG-errorRange<=g<=mithrilG+errorRange and mithrilB-errorRange<=b<=mithrilB+errorRange) or (titaniumR-errorRange<=r<=titaniumR+errorRange and titaniumG-errorRange<=g<=titaniumG+errorRange and titaniumB-errorRange<=b<=titaniumB+errorRange):
            if mithrilR-errorRange<=r<=mithrilR+errorRange and mithrilG-errorRange<=g<=mithrilG+errorRange and mithrilB-errorRange<=b<=mithrilB+errorRange:
                mouse.drag(0, 0, 0, 0, absolute=False, duration=4.5)
                mithrilMined+=1
            elif titaniumR-errorRange<=r<=titaniumR+errorRange and titaniumG-errorRange<=g<=titaniumG+errorRange and titaniumB-errorRange<=b<=titaniumB+errorRange:
                mouse.drag(0, 0, 0, 0, absolute=False, duration=6)
                titaniumMined+=1
            print("Total: "+str(mithrilMined+titaniumMined)+"    Mithril: "+str(mithrilMined)+"    Titanium: "+str(titaniumMined))
            time.sleep(1)
elif ore==2:
    while True:
        blockMined = False
        image = ImageGrab.grab()
        color = image.getpixel((840, 516))
        (r, g, b) = color
        if diamondR-errorRange<=r<=diamondR+errorRange and diamondG-errorRange<=g<=diamondG+errorRange and diamondB-errorRange<=b<=diamondB+errorRange:
            mouse.drag(0, 0, 0, 0, absolute=False, duration=0.3)
            diamondMined+=1
            print("Diamonds mined: "+str(diamondMined))
            time.sleep(1)
