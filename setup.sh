cd /home/pi/Documents
wget https://github.com/matthewf01/Webex-Teams-Status-Box/blob/master/webexteams.py
wget https://github.com/matthewf01/Webex-Teams-Status-Box/blob/master/cronadds

crontab -u pi /home/pi/Documents/Webex-Teams-Status-Box/cronadds

sudo pip install webexteamssdk
