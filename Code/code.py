# Wooden LED Fiber Optic Lamp, by Peter Seddon
# https://github.com/pseddonxvi/Wooden-Fiber-Optic-Lamp?tab=readme-ov-file
# S/N
# Mfg. date:

import board
import neopixel
from ledPixelsPico import *
import touchio

nPix = 35

pix = ledPixels(nPix, board.GP28)

touch = touchio.TouchIn(board.GP29)
print("Start touch", touch.value)

switch = True
mode="rainbow"

while True:
    
    if mode=="rainbow":
        
        for j in range(255):
            for i in range(pix.nPix):
                pixel_index = (i * 256 // pix.nPix) + j
                pix.pixels[i] = pix.wheel(pixel_index & 255, 0.5)
            if touch.value:
                mode="purple"
                time.sleep(0.5)
                break
            pix.pixels.show()
            time.sleep(0.01)
            
    if mode=="purple":
        pix.setColor((255, 0, 255))
        if touch.value:
            mode="seafoam"
            print(mode)
            time.sleep(0.5)

    if mode=="seafoam":
        pix.setColor((0, 255, 110))
        if touch.value:
            mode="vanilla"
            print(mode)
            time.sleep(0.5)
 
    if mode=="vanilla":
        pix.setColor((255, 255, 50))
        if touch.value:
            mode="red"
            print(mode)
            time.sleep(0.5)

    if mode=="red":
        pix.setColor((255, 0, 0))
        if touch.value:
            mode="green"
            print(mode)
            time.sleep(0.5)

    if mode=="green":
        pix.setColor((10, 255, 0))
        if touch.value:
            mode="blue"
            print(mode)
            time.sleep(0.5)

    if mode=="blue":
        pix.setColor((0, 10, 255))
        if touch.value:
            mode="pink"
            print(mode)
            time.sleep(0.5)

    if mode=="pink":
        pix.setColor((255, 10, 100))
        if touch.value:
            mode="cyan"
            print(mode)
            time.sleep(0.5)

    if mode=="cyan":
        pix.setColor((0, 150, 150))
        if touch.value:
            mode="orange"
            print(mode)
            time.sleep(0.5)
            
    if mode=="orange":
        pix.setColor((255, 70, 0))
        if touch.value:
            mode="purple2"
            print(mode)
            time.sleep(0.5)

    if mode=="purple2":
        pix.setColor((228, 26, 255))
        if touch.value:
            mode="yellow"
            print(mode)
            time.sleep(0.5)
            
    if mode=="yellow":
        pix.setColor((255, 165, 0))
        if touch.value:
            mode="crimsion"
            print(mode)
            time.sleep(0.5)
            
    if mode=="crimsion":
        pix.setColor((255, 26, 26))
        if touch.value:
            mode="nuclear"
            print(mode)
            time.sleep(0.5)
 
    if mode=="nuclear":
        pix.setColor((60, 133, 0))
        if touch.value:
            mode="perrywinkle"
            print(mode)
            time.sleep(0.5)
            
    if mode=="perrywinkle":
        pix.setColor((117, 66, 255))
        if touch.value:
            mode="off"
            print(mode)
            time.sleep(0.5)

    if mode=="off":
        pix.setColor((0, 0, 0))
        if touch.value:
            print(mode)
            mode="rainbow"
            time.sleep(0.5)

    
    
    
        
    

# pix.rainbowForever(speed=0.001)
