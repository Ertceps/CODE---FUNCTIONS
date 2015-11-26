# --------------------------------------
# LOCAL
# --------------------------------------

# -+- IMPORT -+-
import time
import os
import ACTIONS
import SWITCHES
import RPi.GPIO as GPIO

def local():
    print("MODE = LOCAL")

    while mode == "LOCAL":

    # Button detection / Debouncing
        GPIO.add_event_detect(SWITCHES.sw_pp_pin, GPIO.RISING, callback=ACTIONS.pp_on(), bouncetime=200)
        GPIO.add_event_detect(SWITCHES.sw_tmp_pin, GPIO.RISING, callback=ACTIONS.tmp_on(), bouncetime=200)
        GPIO.add_event_detect(SWITCHES.sw_vv_pin, GPIO.RISING, callback=ACTIONS.vv_on(), bouncetime=200)    
        GPIO.add_event_detect(SWITCHES.sw_hvgv_pin, GPIO.RISING, callback=ACTIONS.hvgv_on(), bouncetime=200)

        GPIO.add_event_detect(SWITCHES.sw_pp_pin, GPIO.FALLING, callback=ACTIONS.pp_off(), bouncetime=200)
        GPIO.add_event_detect(SWITCHES.sw_tmp_pin, GPIO.FALLING, callback=ACTIONS.tmp_off(), bouncetime=200)
        GPIO.add_event_detect(SWITCHES.sw_vv_pin, GPIO.FALLING, callback=ACTIONS.vv_off(), bouncetime=200)    
        GPIO.add_event_detect(SWITCHES.sw_hvgv_pin, GPIO.FALLING, callback=ACTIONS.hvgv_off(), bouncetime=200)


