#!/bin/bash

# This script will dump your current crontab to file
#  then append a new crontab entry to run the rpi-temperature-monitor
#  script. It will run every 5 minutes with the default schedule below.

# write out the currrent crontab
crontab -l > cronlist

# echo new crontab entry to 
echo "*/5 * * * * /opt/rpi-temperature-monitor/bash/run.sh" >> cronlist

# install new cron file
crontab cronlist
rm cronlist

