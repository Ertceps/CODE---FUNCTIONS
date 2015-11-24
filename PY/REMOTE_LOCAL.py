# --------------------------------------
# REMOTE/LOCAL - INPUTS
# --------------------------------------

# -+- IMPORT -+-
import RPi.GPIO as GPIO # to control GPIO
import time

# Remote/Local
REMOTE_LOCAL_PIN = 26  # RPi.GPIO - Real RPi pin #37


def gpio_setup_mode():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(REMOTE_LOCAL_PIN, GPIO.IN)


def get_mode():
    while 1 < 2:  # To run forever
        global mode
        REMOTE_LOCAL = GPIO.input(REMOTE_LOCAL_PIN)
        if REMOTE_LOCAL == 1:
            mode = "REMOTE"
        elif REMOTE_LOCAL == 0:
            mode = "LOCAL"
        time.sleep(1)  # Get data every 1 sec frequency 1Hz
        print "%s"