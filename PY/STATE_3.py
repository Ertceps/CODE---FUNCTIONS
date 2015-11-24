# --------------------------------------
# STATE 3
# --------------------------------------

# -+- IMPORT -+-
import time
import STATE_0
import STATE_4
import LCD_DISPLAY
import ACTIONS
import WAIT_ROUTINE
import READ_ERROR_TXT
import LOCAL


def state_3():
    global command, mode, state, error
    global P1, P2, P3
    print "STATE 3 : VENTING CHAMBER\n"

    LCD_DISPLAY.main("STATE 3")  # Display LCD : STATE 3

    # Safety Check


    # Update command log
    state = "STATE 3"

    ACTIONS.hvgv_off()  # Close HVGV
    ACTIONS.tmp_off()  # Switch OFF TMP

    # Receive command
    if state != "STATE 3":
        error = "Error 5502"  # Send error 5521 to chamber control
        READ_ERROR_TXT.read_error_txt(error)
        STATE_4.state_4()  #Go to State 4 : Safe State
    elif mode == "LOCAL":
        error = "Error 5521"  # Send error 5521 to chamber control
        READ_ERROR_TXT.read_error_txt(error)
        LOCAL.local()  #Exit automatic sequence
    else:
        # ACTIONS.tmp_flood_on()  # Open TMP flood valve
        ACTIONS.pp_off()  # Switch OFF PP
        ACTIONS.vv_on()  # Open Venting Valve
        start_time = time.time()
        time.sleep(10)  # Wait 10 sec

        # Error log
        counter = 0
        p1_0 = P1
        p2_0 = P2
        time.sleep(0.5)
        p1_1 = P1
        p2_1 = P2
        elapsed_time = time.time() - start_time
        skip = 0
        while skip == 0:
            counter += 1
            if counter < 3:
                if (p1_0 < p1_1) and (p2_0 < p2_1):
                    skip = 1
                    while elapsed_time < 100:  # !!!!! Value TBD:
                        time.sleep(30)  # Wait 30 sec
                        # Error log
                        WAIT_ROUTINE.wait_routine(state)
                        elapsed_time = time.time() - start_time  # Time since VV open
                        if elapsed_time > 100:  # !!!!! Value TBD
                            ACTIONS.vv_off()
                            # ACTIONS.tmp_flood_off()
                            STATE_0.state_0()  # Go to STATE 0 : Vented Chamber
                else:
                    skip = 0
            else:
                # Error log
                STATE_4.state_4()  # Go to STATE 4 : Safe State