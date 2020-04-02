# Webex-Teams-Status-Box
Use a Raspberry Pi, Python, and the webexteamssdk and API to build an IoT "status light" reflecting your real-time presence status in Webex Teams.


# Setup Instructions

You will need 2 pieces of information: 

Your bot's access token from Webex:

-You can get a TEMPORARY access token here, but it will expire in 12 hours. Reccomend for TESTING ONLY.
--https://developer.webex.com/docs/api/getting-started
-For permanent use, create a bot at the site below. Give it a unique name and you'll get an access token
--https://developer.webex.com/my-apps/new/bot

Your user's personId from Webex:


https://developer.webex.com/docs/api/v1/people/get-my-own-details


Run these command from your Raspberry Pi's terminal:

wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/setup.sh

(possibly chmod +x setup.sh)

sh setup.sh
