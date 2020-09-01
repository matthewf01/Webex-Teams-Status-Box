# Webex-Teams-Status-Box
**Uses a Raspberry Pi, Python, and the webexteamssdk and API to create an IoT "status light" reflecting your real-time presence status in Cisco Webex Teams.**


In early 2020, nearly the entire world had to shift to working 100% from home due to coronavirus risks. I have a young child, My home has a very "open" design, and my office _HAS NO DOOR_. My family tip-toed over to my office asking "are you in a meeting?" throughout the day, not knowing if they were interrupting my workday. 

As I've deployed Webex Teams for my company as our standard collaboration platform, and have already been making extensive use of the Teams API (via Powershell infact), I found a way to leverage my "status" to let my family know whether I'm _interruptable_ or not using a real-world visual indicator that could be placed somewhere in plain view.

Finished project:
![Finished project](https://github.com/matthewf01/Webex-Teams-Status-Box/raw/master/photos/final_enclosure.jpg)

Test unit on a breadboard:
![Unit being tested on breadboard](https://github.com/matthewf01/Webex-Teams-Status-Box/raw/master/photos/unit_on_breadboard.jpg)

### This project uses the Webex Teams SDK Python library: ###

* [Documentation](https://webexteamssdk.readthedocs.io/en/latest/index.html)

* [Github - webexteamssdk](https://github.com/CiscoDevNet/webexteamssdk)


## Hardware Setup Instructions ##

### Parts you will need: ###
* A Raspberry Pi with network connectivity 
  * (I've tested and run this on a Pi 3B and a Pi Zero W; both have built-in wifi)
* an SD card formatted with at least Raspbian Jessie 
  * I recommend just using [PiBakery](https://www.pibakery.org/) to pre-configure your SD card image:
  * Set your wifi network configuration, set your password, set your hostname, enable VNC on first boot 
* 1x RGB LED
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
Actually really easy for you! I've scripted out most of the setup process to bootstrap itself into place.

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

The _setup.sh_ shell script I created is awesome and performs the following for you:
* Prompts you for the access token and your personId
* Stores these credentials in a local file called _mycredentials.txt_ just in case you need them later.
* Downloads the Python script (_webexteams.py_) and a service installation file
* Injects your credentials into the service's unit file
* Installs the script as a service which starts at boot
* Installs the webexteamssdk module via pip
* Reboots on completion

### Testing ###

To test, from Terminal run: `python /Home/pi/Documents/webexteams.py`
After a moment, you should see the status codes being returned from the Webex Teams API. `CTRL+C` to break and stop the test run.

Verify your LED is lighting up properly at this time. Double-check that the GPIO pins you've connected match the `webexteams.py` script.

## Running the thing! ##
The Python script has been set via systemd service to run at startup. 

Restart the Raspberry Pi and confirm the script has started automatically. 

**Enjoy your new Webex Teams Status light, and teach your family what the color-codes mean! Red = do not disturb me, and green = I'm working but you can come into the room. Blue means inactive (so I'm not working).**



[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/matthewf01/Webex-Teams-Status-Box)
