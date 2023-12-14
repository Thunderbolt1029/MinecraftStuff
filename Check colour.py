from PIL import ImageGrab
import countdown
import time, sys

countdown = countdown.countdown()
countdown.start(5)

image = ImageGrab.grab()
color = image.getpixel((840, 516))

print(color)
