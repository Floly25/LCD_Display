# https://tutorials-raspberrypi.de/hd44780-lcd-display-per-i2c-mit-dem-raspberry-pi-ansteuern/

# Libraries laden:
import datetime
from time import *
from tkinter import *
import lcddriver
import datetime

# Global vars
LCD_ADRESS = 0x27
SCHUELERNAME = "Florian Manhartseder"

# Install libraries:
    # sudo apt-get install -y i2c-tools && sudo apt-get install -y python-smbus

# NTP Time configuration:
    # sudo apt-get install ntp

# stop current time configuration:
    # sudo systemctl stop systemd-timesyncd
    # sudo systemctl disable systemd-timesyncd
    # ​sudo /etc/init.d/ntp stop
    # ​sudo /etc/init.d/ntp start

# Open config file:
    # sudo nano /etc/ntp.conf

# Write new config:
"""
    #/etc/ntp.conf, configuration for ntpd

    driftfile /var/lib/ntp/ntp.drift
    statsdir /var/log/ntpstats/

    statistics loopstats peerstats clockstats
    filegen loopstats file loopstats type day enable
    filegen peerstats file peerstats type day enable
    filegen clockstats file clockstats type day enable
    
    # You do need to talk to an NTP server or two (or three).
    #server ntp.your-provider.example
    
    # IP adress of my FritzBox to get local time. Some Users said that they have to add iburst behind the IP address like in the following line. Give it a try if it does not work with my solution.
    # server 192.168.178.1 iburst
    server 192.168.178.1
    
    # pool.ntp.org maps to more than 300 low-stratum NTP servers.
    # Your server will pick a different set every time it starts up.
    # *** Please consider joining the pool! ***
    # *** ***
    # 0.cz.pool.ntp.org iburst
    # 1.cz.pool.ntp.org iburst
    # 2.cz.pool.ntp.org iburst
    # 3.cz.pool.ntp.org iburst
"""

# NTP restarten:
    # ​​sudo /etc/init.d/ntp restart


# I2C Display Adress:
    # sudo i2cdetect -y 1


LCD = lcddriver.lcd()
DATE = ''
TIME = ''


def updateDateTime():
    global DATE
    global TIME

    DATE = datetime.time.strftime("%Y%m%d")
    TIME = datetime.time.strftime("%H:%M:%S")


while True:
    sleep(0.5)
    LCD.lcd_clear()

    updateDateTime()

    LCD.lcd_display_string("Hallo " + SCHUELERNAME + "!", 1)
    LCD.lcd_display_string("Heute ist: " + DATE, 2)
    LCD.lcd_display_string("Es ist: " + TIME, 3)
    LCD.lcd_display_string("", 4)







