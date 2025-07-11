
import board
import neopixel
from ledPixelsPico import *
import touchio

nPix = 35

pix = ledPixels(nPix, board.GP28)

touch = touchio.TouchIn(board.GP27)
print("Start touch", touch.value)

switch = True

while True:
    
    if switch:
        
        for j in range(255):
            for i in range(pix.nPix):
                pixel_index = (i * 256 // pix.nPix) + j
                pix.pixels[i] = pix.wheel(pixel_index & 255, 0.5)
            if touch.value:
                pix.light(0, (200,0,0))
                while touch.value:
                    time.sleep(0.1)
                switch = not switch
                print("Touch", switch)
                pix.setColor((0,0,0))
        
                #time.sleep(0.5)
                break
            pix.pixels.show()
            time.sleep(0.01)
            
    #time.sleep(0.5)
    if touch.value:
        pix.light(0, (200,0,0))
        while touch.value:
            time.sleep(0.1)
        switch = not switch
        #print("Touch On", switch)
        #time.sleep(0.5)
    
        
    

# pix.rainbowForever(speed=0.001)


