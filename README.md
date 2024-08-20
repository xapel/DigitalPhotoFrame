# DigitalPhotoFrame
A digital photoframe using a raspberry Pi and an e-Paper display.

# Hardware
- Pi Zero W (with headers)
- Waveshare UPS HAT (c)
- Waveshare 7.5inch E-Paper Display 640x384

# How to build
You need a valid token to access the Google API. You can create the token on your desktop (create_photos_token.py) and then just copy the token to the Pi. You can edit the /etc/rc.local file on the Pi to run your script at startup. 
```
#load new photo on e-ink display
cd /home/pi/project/v1/
su pi -c '/home/pi/project/v1/photo.sh'

#shutdown (unless NOT_SHUTDOWN file is there)
FILE=/boot/NOT_SHUTDOWN;
if ! [ -e $FILE ] ; then 
    shutdown -h now ; 
fi

exit 0
```
This will run your script (photo.sh) to fetch a photo from your favourites in your google photos library. It will filter out photos in landscape and select a portrait one at random and then resize it and upload it to the display. Then it will shutdown and the image will remain on the display.

If you put a file called "NOT_SHUTDOWN" in the /boot folder it will not shutdown your Pi after updating the display. This allows you to remove the SD card from the PI and insert it into your desktop, put this file in place, and then when you put it back into your PI, your Pi will remain powered on.

