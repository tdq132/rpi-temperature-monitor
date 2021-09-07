# rpi-temperature-monitor
## About

This repository contains Python scripts that enable you to disable, enable, or cycle the power to USB ports of a Raspberry Pi based on the Raspberry Pi's CPU temperature.

The scripts have been tested on a Raspberry Pi 4 model B running Ubuntu Server 21.04. 


## Prerequisites 

Python 3, libraspberrypi-bin and [uhubctl](https://github.com/mvp/uhubctl) - you can install these by running `sudo apt-get install python3 libraspberrypi-bin uhubctl`


## Installation 

Just suggestions. Feel free to deploy it however you like.

1. Clone this Github repository
2. Move it to /opt - `sudo mv rpi-temperature-monitor /opt/rpi-temperature-monitor`
3. Add the crontab entry - `sudo /opt/rpi-temperature-monitor/bash/install-crontab.sh`
4. Run a test - `sudo /opt/rpi-temperature-monitor/bash/run.sh`


## Important notes

- The bash scripts rely on you using the `/opt/rpi-temperature-monitor` path
- You can modify the execution time to whatever you like. The default is every 5 minutes.


## Future fixes and enhancements

- The power is disabled to all the Pi USB ports, not to a single port.
- The Python script does not check for the USB ports current power state, it only checks what the CPU temperature is and triggers the power enable or disable command.
- Add the ability to check muliple Pi's.

