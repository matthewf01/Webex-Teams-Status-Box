# wiring diagram for LED
# https://www.instructables.com/id/Raspberry-Pi-3-RGB-LED-With-Using-PWM/

import time

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


from webexteamssdk import WebexTeamsAPI

#make sure to replace with a permanent bot token later
api=WebexTeamsAPI(access_token='your_bot_token')

person= api.people.me()
print (person.status,person.displayName)


matthew_id = "your_personId_on_webex"
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
			time.sleep (60)
		elif status == "call":
			print "he's on a call! ORANGE"
			GREEN.start(85)
			RED.start(1)
			BLUE.start(100)
			time.sleep (60)
		elif status == "inactive":
			print "inactive - BLUE"
			GREEN.start(100)
			RED.start(100)
			BLUE.start(20)
			time.sleep (180)
		else:
			print "don't bug him! RED"
			GREEN.start(100)
			RED.start(1)
			BLUE.start(100)	
			time.sleep (60)


except KeyboardInterrupt:
	RED.stop()
	GREEN.stop()
	BLUE.stop()	
	GPIO.cleanup()

# active,inactive,DoNotDisturb,meeting,presenting,call
