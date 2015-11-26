# --------------------------------------
# CONTROL RELAY - OUTPUTS
# --------------------------------------

# -+- IMPORT -+-
import RPi.GPIO as GPIO

# Relays
pp_pin = 4  # RPi.GPIO - Real RPi pin #7
tmp_pin = 17  # RPi.GPIO - Real RPi pin #11
hvgv_pin = 2  # RPi.GPIO - Real RPi pin #13
vv_pin = 3  # RPi.GPIO - Real RPi pin #15

pp = 0
tmp = 0
hvgv = 0
vv = 0

# SETUP the channels (HIGH/1 = OPENED/ON -+- LOW/0 = CLOSED/OFF)
def gpio_setup_relays():
    global pp, tmp, hvgv, vv
    GPIO.setmode(GPIO.BCM)  # BCM = referring to the pins by the "Broadcom SOC channel"

    GPIO.setup(pp_pin, GPIO.OUT, initial=GPIO.LOW)
    pp = 0
    GPIO.setup(tmp_pin, GPIO.OUT, initial=GPIO.LOW)
    tmp = 0
    GPIO.setup(hvgv_pin, GPIO.OUT, initial=GPIO.HIGH)
    hvgv = 1
    GPIO.setup(vv_pin, GPIO.OUT, initial=GPIO.HIGH)
    vv = 1
    GPIO.setwarnings(False)
    print("Relays pins setup")


# --- PRIMARY PUMP ---
def pp_on():  # Switch ON Primary Pump
    global pp
    GPIO.output(pp_pin, 1)
    pp = 1
    print "pp on"
    return ()


def pp_off():  # Switch OFF Primary Pump
    global pp
    GPIO.output(pp_pin, 0)
    pp = 0
    print "pp off"
    return ()


# --- TURBO MOLECULAR PUMP ---
def tmp_on():  # Switch ON Turbo Molecular Pump
    global tmp
    GPIO.output(tmp_pin, 1)
    tmp = 1
    print "tmp on"
    return ()


def tmp_off():  # Switch OFF Turbo Molecular Pump
    global tmp
    GPIO.output(tmp_pin, 0)
    tmp = 0
    print "tmp off"
    return ()


# --- HIGH-VACUUM VENTING VALVE ---
def hvgv_on():  # Open High Vacuum Gate Valve
    global hvgv
    GPIO.output(hvgv_pin, 1)
    hvgv = 1
    print "hvgv open"
    return ()


def hvgv_off():  # Close High Vacuum Gate Valve
    global hvgv
    GPIO.output(hvgv_pin, 0)
    hvgv = 0
    print "hvgv closed"
    return ()


# --- VENTING VALVE ---
def vv_on():  # Open Venting Valve
    global vv
    GPIO.output(vv_pin, 1)
    vv = 1
    print "vv open"
    return ()


def vv_off():  # Close Venting Valve
    global vv
    GPIO.output(vv_pin, 0)
    vv = 0
    print "vv closed"
    return ()
