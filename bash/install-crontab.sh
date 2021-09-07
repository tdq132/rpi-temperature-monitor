#!/bin/bash
set -e


# write out the currrent crontab
crontab -l > cronlist

# echo new crontab entry to 
echo "*/5 * * * * /opt/rpi-temperature-monitor/bash/run.sh" >> cronlist

# install new cron file
crontab cronlist
rm cronlist
