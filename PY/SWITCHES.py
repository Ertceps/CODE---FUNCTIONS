# --------------------------------------
# SWITCHES - INPUTS
# --------------------------------------

# -+- IMPORT -+-
import RPi.GPIO as GPIO
import threading

# Rocker switches pins
sw_pp_pin = 5  # RPi.GPIO - Real RPi pin #29
sw_tmp_pin = 6  # RPi.GPIO - Real RPi pin #31
sw_hvgv_pin = 13  # RPi.GPIO - Real RPi pin #33
sw_vv_pin = 19  # RPi.GPIO - Real RPi pin #35

# Create the variables
sw_pp = 0
sw_tmp = 0
sw_hvgv = 0
sw_vv = 0

def gpio_setup_switches():
    global sw_pp, sw_tmp, sw_hvgv, sw_vv

    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(sw_pp_pin, GPIO.IN)
    GPIO.setup(sw_tmp_pin, GPIO.IN)
    GPIO.setup(sw_hvgv_pin, GPIO.IN)
    GPIO.setup(sw_vv_pin, GPIO.IN)
    GPIO.setwarnings(False)

    GPIO.add_event_detect(sw_pp_pin, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(sw_tmp_pin, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(sw_hvgv_pin, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(sw_vv_pin, GPIO.RISING, bouncetime=200)
    
    sw_pp = GPIO.input(sw_pp_pin)  # Get the status of PP switch
    sw_tmp = GPIO.input(sw_tmp_pin)  # Get the status of TMP switch
    sw_hvgv = GPIO.input(sw_hvgv_pin)  # Get the status of HVGV switch
    sw_vv = GPIO.input(sw_vv_pin)  # Get the status of VV switch

class ThreadSwitches(threading.Thread):
    
    def __init__(self, threadID, name, counter, mode):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.mode = mode
        
    def run(self):
        global sw_pp, sw_tmp, sw_hvgv, sw_vv, mode

        while mode == "LOCAL":
            print "Starting " + self.name
            sw_pp = GPIO.input(sw_pp_pin)  # Get the status of PP switch
            sw_tmp = GPIO.input(sw_tmp_pin)  # Get the status of TMP switch
            sw_hvgv = GPIO.input(sw_hvgv_pin)  # Get the status of HVGV switch
            sw_vv = GPIO.input(sw_vv_pin)  # Get the status of VV switch


        
