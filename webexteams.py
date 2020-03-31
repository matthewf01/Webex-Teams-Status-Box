your-access-token='PUT A BOT TOKEN HERE' 
matthew_id = "FIND YOUR WEBEX TEAMS PERSONID AND PUT IT HERE"

# wiring diagram for LED
# https://www.instructables.com/id/Raspberry-Pi-3-RGB-LED-With-Using-PWM/

#modules to load
import time
from picamera import PiCamera
from webexteamssdk import WebexTeamsAPI

#set up camera
camera = PiCamera()
camera.rotation = 180 #options are 0,90,180,270

# set up for RGB LEDs
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
green=20
red=21
blue=22
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
Freq=100 #for PWM control
RED=GPIO.PWM(red,Freq)
GREEN=GPIO.PWM(green,Freq)
BLUE=GPIO.PWM(blue,Freq)




#make sure to replace with a permanent bot token later
api=WebexTeamsAPI(access_token=your-access-token)

person= api.people.me()
print (person.status,person.displayName)



api.people.get(personId=matthew_id).status

try:
	while True:
		status = api.people.get(personId=matthew_id).status
		print (status)
		if status == "active":
			print "he's active! GREEN"
			GREEN.start(1)
			RED.start(100)
			BLUE.start(100)
		elif status == "call":
			print "he's on a call! ORANGE"
			GREEN.start(85)
			RED.start(1)
			BLUE.start(100)
		elif status == "inactive":
			print "inactive - turn off light"
			GREEN.start(100)
			RED.start(100)
			BLUE.start(100)
		else:
			print "don't bug him! RED"
			GREEN.start(100)
			RED.start(1)
			BLUE.start(100)		
		time.sleep (55)

except KeyboardInterrupt:
	RED.stop()
	GREEN.stop()
	BLUE.stop()	
	GPIO.cleanup()

# active,inactive,DoNotDisturb,meeting,presenting,call

# camera code here ---- 
# camera.start_preview()
# sleep(5)
# camera.capture('/home/pi/Desktop/image.jpg')
# camera.stop_preview()
