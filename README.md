# smart-fridge

For more information:

https://orianzinger.wordpress.com/2021/02/02/smart-fridge-part-1/

https://orianzinger.wordpress.com/2021/02/18/smart-fridge-part-2/

Create credentials at: https://developers.google.com/drive/api/v3/quickstart/python

Clone this repository
If you want to develop it:
 1. Run the `desktopinstaller.sh`
 2. Move your credentials to /etc/smartfridge/
 3. Run with `python3 main.py`

If you want to run it on your RPI:
1. Run the `rpiinstaller.sh`
2. Move your credentials to /etc/smartfridge/
3. Reboot the machine `sudo reboot`
 
Follow the logs at `tail -F /var/log/syslog`
