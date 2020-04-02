#!/bin/sh
# 2020-04-01 Matthew Fugel 
# https://github.com/matthewf01/Webex-Teams-Status-Box/

cd /home/pi/Documents

#retrieve user-specific values that will be written to mycredentials.sh file for storing as env variables
read -p "Enter your WebexTeams admin token: " accessToken
read -p "Enter the personId of the WebexTeams user you're checking status of: " person

#write the values out to file
echo "export WEBEX_TEAMS_ACCESS_TOKEN="$accessToken >> mycredentials.sh
echo "export PERSON="$person >> mycredentials.sh

#import as environment variables now
source /home/pi/Documents/mycredentials.sh

#download script files
wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/cronadds
wget -O webexteams.py https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/webexteams.py

#set up the cronjob schedule using downloaded file
crontab -u pi /home/pi/Documents/cronadds

#install dependencies
sudo pip install webexteamssdk

