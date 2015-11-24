# --------------------------------------
# STATE 1
# --------------------------------------

# -+- IMPORT -+-
import time
import STATE_2
import STATE_4
import LCD_DISPLAY
import ACTIONS
import WAIT_ROUTINE
import DATA_ACQUISITION_BACKUP


def state_1():
    global command, state
    global P1, P2, P3, timestamp_sensors
    global PP, TMP, TMP_FV, HVGV, VV
    global data
    data = [timestamp_sensors, P1, P2, P3, HVGV, VV, PP, TMP, TMP_FV]
    print "STATE 1 : ESTABLISH VACUUM\n"

    LCD_DISPLAY.main("STATE 1")  # Display  LCD : STATE 1

    # Safety Check

    # Update command log
    state = "STATE 1"
    thread_command_write = DATA_ACQUISITION_BACKUP.CommandWrite(data, out)
    thread_command_write.start()
    # Start Data acquisition
    thread_physical_write = DATA_ACQUISITION_BACKUP.PhysicalWrite(data, out, state)
    thread_physical_write.start()

    ACTIONS.pp_on()
    start_time = time.time()

    while P3 < P1:
        # Error log
        WAIT_ROUTINE.wait_routine(state)
        elapsed_time = time.time() - start_time
        if elapsed_time > (3600*5):  # Check if PP switch ON for more than 5 hours
            # Error log
            STATE_4.state_4()  # Go to STATE 4 : SAFE STATE

    ACTIONS.hvgv_on()
    start_time = time.time()

    while P1 > 10^(-1):
        # Error log
        WAIT_ROUTINE.wait_routine(state)
        elapsed_time = time.time() - start_time
        if elapsed_time > (3600*5):  # Check if PP switch ON for more than 5 hours
            # Error log
            STATE_4.state_4()  # Go to STATE 4 : SAFE STATE

    ACTIONS.tmp_on()
    start_time = time.time()

    while P2 > 10^(-4):
        # Error log
        WAIT_ROUTINE.wait_routine(state)
        elapsed_time = time.time() - start_time
        if elapsed_time > (3600*60):  # Check if PP switch ON for more than 60 hours
            # Error log
            STATE_4.state_4()  # Go to STATE 4 : SAFE STATE

    while P2 > 10^(-5):
        WAIT_ROUTINE.wait_routine(state)

    STATE_2.state_2()  # Go to STATE 2 : Maintain Vacuum