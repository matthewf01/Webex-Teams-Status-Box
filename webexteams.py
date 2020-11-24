#!/usr/bin/python
# 2020-04-01 Matthew Fugel
# https://github.com/matthewf01/Webex-Teams-Status-Box
# wiring diagram for LED
# https://www.instructables.com/id/Raspberry-Pi-3-RGB-LED-With-Using-PWM/

import os
import time
from webexteamssdk import WebexTeamsAPI
import RPi.GPIO as GPIO

# set up for RGB LEDs. Use GPIO pins referenced below when wiring:
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

#if not setting personId as an environment varaible,
#then replace the next line with api=WebexTeamsAPI(access_token=putyourtokenhere)
api=WebexTeamsAPI()

#helpful stuff you can run if using your personal access token temporarily to test:
# person= api.people.me()
# print (person.status,person.displayName)

#pull the personId from environment variable
mywebexid=os.environ.get('PERSON')
api.people.get(personId=mywebexid).status

try:
	while True:
		status = api.people.get(personId=mywebexid).status
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
		elif status == "OutOfOffice":
			print "Out of Office - PURPLE"
			GREEN.start(100)
			RED.start(90)
			BLUE.start(90)
			time.sleep (360)
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

# Status codes include: active,inactive,DoNotDisturb,meeting,presenting,call
