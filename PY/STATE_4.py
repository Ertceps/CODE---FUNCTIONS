# --------------------------------------
# STATE 4
# --------------------------------------

# -+- IMPORT -+-
import STATE_1
import STATE_3
import LCD_DISPLAY
import ACTIONS
import READ_ERROR_TXT


def state_4():
    global command, state, mode
    global HVGV

    print "STATE 4 : SAFE STATE\n"

    LCD_DISPLAY.main("STATE 4")  # Display  LCD : STATE 4

    # Update command log
    state = "STATE 4"

    # Error log

    while HVGV == 1:
        ACTIONS.hvgv_off()

    if HVGV == 0:
        ACTIONS.vv_off()  # Close VV
        ACTIONS.tmp_off()  # Switch OFF TMP

        # Return USB : SAFE STATE
        # Error Log
        # Receive command
        while command != "":  # Check if command received
            if state == "STATE 3":
                STATE_3.state_3()  # Go to State 3 : Venting Chamber
            elif state == "STATE 1":
                STATE_1.state_1()  # Go to State 1 : Establish Vacuum
            elif mode == "LOCAL":
                error = "Error 5521"  # Send error 5521 to chamber control
                READ_ERROR_TXT.read_error_txt(error)

            else:
            # Return USB message :  Invalid command
