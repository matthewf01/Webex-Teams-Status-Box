cd /home/pi/Documents
wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/cronadds
wget https://raw.githubusercontent.com/matthewf01/Webex-Teams-Status-Box/master/webexteams.py >> webexteams.py

crontab -u pi /home/pi/Documents/cronadds

sudo pip install webexteamssdk
