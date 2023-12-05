#!/usr/bin/python

import emoji
import hashlib
import logging
import time

## Initialize some variables
str_master = "master.json"
str_sha256_current = None

## Set up logging
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    handlers=[logging.FileHandler("main.log", "a", encoding = "UTF-8")],
    level=logging.DEBUG
)

## Get the SHA256 property of a file
def get_sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

## Function to add emojis to log messages
def log_with_emoji(level, message):
    emoji_dict = {
        'DEBUG': emoji.emojize(':page_with_curl:'),
        'INFO': emoji.emojize(':information:'),
        'WARNING': emoji.emojize(':warning:'),
        'ERROR': emoji.emojize(':fire:'),
        'CRITICAL': emoji.emojize(':skull:')
    }
    emoji_symbol = emoji_dict.get(level, '')
    if emoji_symbol:
        return f"{emoji_symbol} - {message}"
    else:
        return f"" + emoji.emojize(':diamond_with_a_dot:') + " - {message}"

## Using the custom log_with_emoji function for logging
def main():
    # logging.debug(log_with_emoji('DEBUG', 'This is a debug message'))
    # logging.info(log_with_emoji('INFO', 'This is an info message'))
    # logging.warning(log_with_emoji('WARNING', 'This is a warning message'))
    # logging.error(log_with_emoji('ERROR', 'This is an error message'))
    # logging.critical(log_with_emoji('CRITICAL', 'This is a critical message'))
    global str_sha256_current
    if str_sha256_current != get_sha256sum(str_master):
        logging.info(log_with_emoji('INFO', 'Changes found in the command file ' + emoji.emojize(':dog:')))
        str_sha256_current = get_sha256sum(str_master)
    pass

if __name__ == "__main__":
    str_sha256_current = get_sha256sum(str_master)
    while True:
        try:
            main()
            time.sleep(1)
        except KeyboardInterrupt:
            # print("Caught KeyboardInterrupt exception... Goodbye!")
            exit()
        
'''

References
https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

'''