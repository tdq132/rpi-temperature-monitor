

import re
import os
import subprocess
import logging
import logging.handlers
import rpi_toggle_usb


# User defined variables
temperature_upper_limit = 50
log_level = 'info'


def initiate_logging():
    ''' Set up our logger to be used throughout the script.
    '''
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)5s - %(filename)s-%(funcName)s-%(lineno)04d - %(message)s')
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(log_level.upper())
    logger.addHandler(stream_handler)
    logger.setLevel(log_level.upper())
    logger.debug(f'Logging initiated - log level {log_level.upper()}')


def check_root():
    euid = os.geteuid()
    logger.debug(f'Current euid is {euid}')

    if euid != 0:
        logger.error(f'euid is {euid}')
        logger.error(f'Script requires euid 0 (root) to execute successfully')
        logger.error(f'Script exiting with status 1')
        exit(1)

    return euid


def get_rpi_temperature():
    # execute OS command to output the CPU temperature
    logger.debug(f'Running subprocess to extract current temperature')
    temp = subprocess.Popen(['vcgencmd','measure_temp'],stdout=subprocess.PIPE)
    temp_return = temp.stdout.read().decode("utf-8") 
    logger.debug(f'Command returned value: {temp_return}')
    
    # regex to extract only integers
    # we are only returning the whole number
    temperature = re.findall(r'\d+', temp_return)[0]
    temperature = int(temperature)

    return temperature


def monitor_temperature():
    temperature = get_rpi_temperature()
    
    logger.debug(f'Current temperature: {temperature}, temperature upper limit: {temperature_upper_limit}')
    if temperature > temperature_upper_limit:
        logger.debug('Temperature is above the upper limit. Enabling the USB port power')
        rpi_toggle_usb('enable')
    elif temperature < temperature_upper_limit:
        logger.debug('Temperature is below the upper limit. Disabling the USB port power')
        rpi_toggle_usb('disable')



if __name__ == "__main__":
    initiate_logging()
    logger = logging.getLogger('')
    
    check_root()
    monitor_temperature()

