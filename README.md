# Webex-Teams-Status-Box
**Use a Raspberry Pi, Python, and the webexteamssdk and API to build an IoT "status light" reflecting your real-time presence status in Webex Teams.**

### This project uses the Webex Teams SDK Python library: ###

* [Documentation](https://webexteamssdk.readthedocs.io/en/latest/index.html)

* [Github - webexteamssdk](https://github.com/CiscoDevNet/webexteamssdk)


![Unit being tested on breadboard](https://github.com/matthewf01/Webex-Teams-Status-Box/raw/master/photos/unit_on_breadboard.jpg)

## Hardware Setup Instructions

### Parts you will need: ###
* A Raspberry Pi with network connectivity 
  * (I've tested and run this on a Pi 3B and a Pi Zero W; both have built-in wifi)
* an SD card formatted with at least Raspbian Jessie 
  * I recommend just using [PiBakery](https://www.pibakery.org/) to pre-configure your SD card image:
  * Set your wifi network configuration, set your password, set your hostname, enable VNC on first boot 
* * 1x RGB LED
  * I'm using [this big one from Adafruit](https://www.adafruit.com/product/848) because it's big, bright, and fun. Common anode, which I understand makes a difference in how its wired. Just wire as shown.
* Resistors, 100 ohm and 150 ohm
* A solderless breadboard, or a soldering iron, and some wire or jumpers

### Wiring Guide ###

Reference [this article](https://www.instructables.com/id/Raspberry-Pi-3-RGB-LED-With-Using-PWM/) on how to wire up your breadboard or solder together your components. The following GPIO pins are used:

* GPIO 20: Green LED leg (leg #3 if using common anode LED)
* GPIO 21: Red LED leg (leg #1 if using common anode LED)
* GPIO 22: Blue LED leg (leg #4 if using common anode LED)
* 5V for power (long leg of LED, leg #2 if using common anode LED)

A resistor should be run between each LED leg (except 5V) and the GPIO to protect the LED. Red gets a different value resistor, so check that guide.

## Software Setup Instructions ##

### You will need 2 pieces of information to complete software setup: ###

1. **Your bot's access token from Webex:**
  * TEMPORARY: you can get a temp access token here, but it will expire in 12 hours. FOR TESTING ONLY.
    * https://developer.webex.com/docs/api/getting-started
  * PERMANENT: create a bot at the site below. Give it a unique name and you'll get an access token good for life
    * https://developer.webex.com/my-apps/new/bot

2. **Your user's personId from Webex:**
  * https://developer.webex.com/docs/api/v1/people/get-my-own-details
    1. Sign into your Webex account, then under the "Try It" section, click "Run"
    2. Copy the value `id` from the response shown


### Run these command from your Raspberry Pi's terminal: ###

* `wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/setup.sh`
* `sh setup.sh`

The setup.sh shell script performs the following:
* Prompts you for the access token and your personId
* Stores these credentials in a local file called mycredentials.sh
* Downloads the script file and a scheduled task (cron) file
* Installs the webexteamssdk module via pip
* Sets the script to run on start-up using a cron job
* Imports your access token and personId as an environment variable (the access token is called by the webexteamsapi behind the scenes, so you won't see it referenced in webexteams.py)

### Testing ###

To test, from Terminal run: `python /Home/pi/Documents/webexteams.py`
After a moment, you should see the status codes being returned from the Webex Teams API. `CTRL+C` to break and stop the test run.

Verify your LED is lighting up properly at this time. Double-check that the GPIO pins you've connected match the `webexteams.py` script.

## Running the thing! ##
The Python script has been set via cron to run at startup. You can verify the cron schedule is present by running `crontab -e`.

Restart the Raspberry Pi and confirm the script has started automatically. 

**Enjoy your new Webex Teams Status light, and teach your family what the color-codes mean! Red = do not disturb me, and green = I'm working but you can come into the room.**


