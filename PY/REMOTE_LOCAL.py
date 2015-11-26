# --------------------------------------
# REMOTE/LOCAL - INPUTS
# --------------------------------------

# -+- IMPORT -+-
import RPi.GPIO as GPIO # to control GPIO
import time
import threading

# Remote/Local
remote_local_pin = 26  # RPi.GPIO - Real RPi pin #37


def gpio_setup_mode():
    GPIO.setmode(GPIO.BCM)  # BCM = referring to the pins by the "Broadcom SOC channel"
    GPIO.setup(remote_local_pin, GPIO.IN)  # Setup the pin as INPUT
    GPIO.add_event_detect(remote_local_pin, GPIO.RISING, bouncetime=200)  # Detect switch with a bouncetime of 200ms
    print("Local/Remote pin setup")

       
class ThreadMode (threading.Thread):
    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):

        print "Starting " + self.name
        
        while 1 < 2:  # To run forever
            global mode
            print "%s: %s" % (self.name, time.ctime(time.time()))
            REMOTE_LOCAL = GPIO.input(remote_local_pin)
        
            if REMOTE_LOCAL == 1:
                mode = "REMOTE"
            else:
                mode = "LOCAL"


            time.sleep(1)  # Get data every 1 sec frequency 1Hz
            print('REMOTE_LOCAL = ' + mode)

        print "Exiting " + self.name
