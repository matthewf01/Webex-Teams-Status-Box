cd /home/pi/Documents
wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/webexteams.py
wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/cronadds

crontab -u pi /home/pi/Documents/cronadds

sudo pip install webexteamssdk
