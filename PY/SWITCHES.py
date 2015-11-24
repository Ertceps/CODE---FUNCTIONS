# --------------------------------------
# SWITCHES - INPUTS
# --------------------------------------

# -+- IMPORT -+-
import RPi.GPIO as GPIO

# Rocker switches pins
SW_PP_PIN = 5  # RPi.GPIO - Real RPi pin #29
SW_TMP_PIN = 6  # RPi.GPIO - Real RPi pin #31
SW_HVGV_PIN = 13  # RPi.GPIO - Real RPi pin #33
SW_VV_PIN = 19  # RPi.GPIO - Real RPi pin #35


def gpio_setup_switches():
    global SW_PP, SW_TMP, SW_HVGV, SW_VV

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SW_PP_PIN, GPIO.IN)
    GPIO.setup(SW_TMP_PIN, GPIO.IN)
    GPIO.setup(SW_HVGV_PIN, GPIO.IN)
    GPIO.setup(SW_VV_PIN, GPIO.IN)
    GPIO.setwarnings(False)

    SW_PP = GPIO.input(SW_PP_PIN)
    SW_TMP = GPIO.input(SW_TMP_PIN)
    SW_HVGV = GPIO.input(SW_HVGV_PIN)
    SW_VV = GPIO.input(SW_VV_PIN)
