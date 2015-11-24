# --------------------------------------
# CONTROL RELAY - OUTPUTS
# --------------------------------------

# -+- IMPORT -+-
import RPi.GPIO as GPIO

# Relays
PP_PIN = 4  # RPi.GPIO - Real RPi pin #7
TMP_PIN = 17  # RPi.GPIO - Real RPi pin #11
# TMP_FLOOD_PIN = ?
HVGV_PIN = 27  # RPi.GPIO - Real RPi pin #13
VV_PIN = 22  # RPi.GPIO - Real RPi pin #15


# Setup the channels (HIGH/1 = OPENED/ON -+- LOW/0 = CLOSED/OFF)

def gpio_setup_relays():
    global PP, TMP, HVGV, VV
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PP_PIN, GPIO.OUT, initial=GPIO.LOW)
    PP = 0
    GPIO.setup(TMP_PIN, GPIO.OUT, initial=GPIO.LOW)
    TMP = 0
    # GPIO.setup(TMP_FLOOD_PIN, GPIO.OUT, initial=GPIO.LOW)
    # TMP_FV = 0
    GPIO.setup(HVGV_PIN, GPIO.OUT, initial=GPIO.HIGH)
    HVGV = 1
    GPIO.setup(VV_PIN, GPIO.OUT, initial=GPIO.HIGH)
    VV = 1
    GPIO.setwarnings(False)


# GPIO.input(channel) # Read the value on the input channel
# GPIO.output(channel, state) #Set the output state of a GPIO pin

# --- PRIMARY PUMP ---
def pp_on():  # Switch ON Primary Pump
    GPIO.output(PP_PIN, 1)
    global PP
    PP = 1
    print "PP on"
    return ()


def pp_off():  # Switch OFF Primary Pump
    GPIO.output(PP_PIN, 0)
    global PP
    PP = 0
    print "PP off"
    return ()


# --- TURBO MOLECULAR PUMP ---
def tmp_on():  # Switch ON Turbo Molecular Pump
    GPIO.output(TMP_PIN, 1)
    global TMP
    TMP = 1
    print "TMP on"
    return ()


def tmp_off():  # Switch OFF Turbo Molecular Pump
    GPIO.output(TMP_PIN, 0)
    global TMP
    TMP = 0
    print "TMP off"
    return ()


# --- HIGH-VACUUM VENTING VALVE ---
def hvgv_on():  # Open High Vacuum Gate Valve
    GPIO.output(HVGV_PIN, 1)
    global HVGV
    HVGV = 1
    print "HVGV open"
    return ()


def hvgv_off():  # Close High Vacuum Gate Valve
    GPIO.output(HVGV_PIN, 0)
    global HVGV
    HVGV = 0
    print "HVGV closed"
    return ()


# --- VENTING VALVE ---
def vv_on():  # Open Venting Valve
    GPIO.output(VV_PIN, 1)
    global VV
    VV = 1
    print "VV open"
    return ()


def vv_off():  # Close Venting Valve
    GPIO.output(VV_PIN, 0)
    global VV
    VV = 0
    print "VV closed"
    return ()

# --- TMP FLOOD VALVE ---
# def tmp_flood_on():  # Open TMP Flood Valve
#     GPIO.output(TMP_FLOOD_PIN, 1)
#     global TMP_FV
#     TMP_FV = 1
#     print "TMP Flood Valve on"
#     return ()


# def tmp_flood_off():  # Close TMP Flood Valve
#     GPIO.output(TMP_FLOOD_PIN, 0)
#     global TMP_FV
#     TMP_FV = 0
#     print "TMP Flood Valve off"
#     return ()