from pitftgpio import PiTFT_GPIO #for buttons on display
import RPi.GPIO as GPIO
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

GPIO.setmode(GPIO.BOARD)  #uses the pins on the board

############################# VARIABLES ##########################
#paw buttons
p1palm = 27
p1left = 29
p1center = 31
p1right = 33

p2palm = 35
p2left = 37
p2center = 36
p2right = 38


pitft = PiTFT_GPIO() #for buttons on display

############################# SET UP ##########################
#for paw controllers
GPIO.setup(p1palm, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p1left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p1center, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p1left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2palm, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2center, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2right, GPIO.IN, pull_up_down=GPIO.PUD_UP)

############################# LOOP ##########################
while True:

    if GPIO.input(p1palm): 
        print "p1palm is pressed"  
    if GPIO.input(p1left): 
        print "p1left is pressed"      
    if GPIO.input(p1center): 
        print "p1center is pressed"  
    if GPIO.input(p1right): 
        print "p1right is pressed" 
        
    if GPIO.input(p2palm): 
        print "p1palm is pressed"  
    if GPIO.input(p2left): 
        print "p1left is pressed"      
    if GPIO.input(p2center): 
        print "p1center is pressed"  
    if GPIO.input(p2right): 
        print "p1right is pressed"       
                     
    if pitft.Button1:
        print "Button 1 pressed - screen off"
        pitft.Backlight(False)
    if pitft.Button2:
        print "Button 2 pressed - screen on"
        pitft.Backlight(True) 
    if pitft.Button3:
        print "Button 3 pressed"
        #toggle up one channel
    if pitft.Button4:
        print "Button 4 pressed"
        *#toggle down a channel