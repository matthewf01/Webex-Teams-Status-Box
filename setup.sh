#!/bin/sh
# 2020-04-03 Matthew Fugel 
# https://github.com/matthewf01/Webex-Teams-Status-Box/

cd /home/pi/Documents

#retrieve user-specific values that will be written to mycredentials.sh file for storing as env variables
read -p "Enter your WebexTeams admin token: " accessToken
read -p "Enter the personId of the WebexTeams user you're checking status of: " person

#write the values out to file
echo "---Webex Teams Credentials---" >> mycredentials.txt
echo" ---saving here for your reference. This file is not used by the script. Creds are in /lib/systemd/system/webexteams.service.--" >> mycredentials.txt
echo "Environment=WEBEX_TEAMS_ACCESS_TOKEN="$accessToken >> mycredentials.txt
echo "Environment=PERSON="$person >> mycredentials.txt

#import as environment variables now
source /home/pi/Documents/mycredentials.sh

#download script files
wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/cronadds
wget -O webexteams.py https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/webexteams.py
wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/webexteams.service

#update service file with creds
sed -i "s/foo/$accessToken/" webexteams.service
sed -i "s/bar/$person/" webexteams.service

#register app as a service
sudo mv webexteams.service /lib/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable webexteams.service

#set up the cronjob schedule using downloaded file
crontab -u pi /home/pi/Documents/cronadds

#install dependencies
sudo pip install webexteamssdk

#finally, reboot
echo "Install complete. Rebooting...."
sleep 5
sudo reboot

