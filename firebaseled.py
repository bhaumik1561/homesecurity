
import RPi.GPIO as GPIO
import time
import Pyrebase
#Firebase Configuration
config = {
"apiKey": "AIzaSyCZowZajsv49aNYRKbZJaHT7P4r_bHnSfU",
"authDomain": "homesecurity-65358.firebaseapp.com",
"databaseURL": "homesecurity-65358.firebaseio.com",
"storageBucket": "homesecurity-65358.appspot.com"
}
firebase = pyrebase.initialize_app(config)
#GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
#Firebase Database Intialization
db = firebase.database()
#While loop to run until user kills program
while(True):
    #Get value of LED 
    led = db.child("led").get()
    #Sort through children of LED(we only have one)
    
    
    if(led.val() == "Off"):
    #If value is off, turn LED off
        GPIO.output(18, False)
    else:
        #If value is not off(implies it's on), turn LED on
        GPIO.output(18, True)
        #0.1 Second Delay
        time.sleep(0.1)   
