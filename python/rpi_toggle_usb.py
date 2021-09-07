

import os
import argparse
import logging
import logging.handlers


# User defined variables
command      = '/usr/sbin/uhubctl'
location     = '2'
action_on    = '1'
action_off   = '0'
action_cycle = '2'
log_level    = 'info'

# inherit logging
logger = logging.getLogger('rpi_temperature_monitor')


def check_root():
    euid = os.geteuid()
    logger.debug(f'Current euid is {euid}')

    if euid != 0:
        logger.error(f'euid is {euid}')
        logger.error(f'Script requires euid 0 (root) to execute successfully')
        logger.error(f'Script exiting with status 1')
        exit(1)

    return euid


def toggle_usb(action):
    # code the action
    if action == 'enable':
        toggle_cmd = f'{command} --location {location} --action {action_on}'
    elif action == 'disable':
        toggle_cmd = f'{command} --location {location} --action {action_off}'
    elif action == 'cycle':
        toggle_cmd = f'{command} --location {location} --action {action_cycle}'

    # execute the command
    logger.debug(f'Executing command: {toggle_cmd}')
    cmd = os.system(toggle_cmd)

    logger.info(f'Sent {action} command')



if __name__ == "__main__":
    # Logging initiation
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)5s - %(filename)s-%(funcName)s-%(lineno)04d - %(message)s')
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(log_level.upper())
    logger.addHandler(stream_handler)
    logger.setLevel(log_level.upper())
    logger.debug(f'Logging initiated - log level {log_level.upper()}')
    logger.debug(f'Current PID is {os.getpid()}')
    
    # Parse arguments
    logger.debug('Parsing arguments')
    arg_parser = argparse.ArgumentParser(description='Toggle the power to the board USB devices') 
    arg_parser.add_argument('-a', '--action', action='store', default=None, required=True,\
        help='Action for this script to instruct the OS.', choices=['enable','disable','cycle'], type=str.lower) 
    args = arg_parser.parse_args()

    # Call function
    check_root()
    toggle_usb(args.action)

