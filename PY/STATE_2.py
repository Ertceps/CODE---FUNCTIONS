# --------------------------------------
# STATE 2
# --------------------------------------

# -+- IMPORT -+-
import STATE_3
import STATE_4
import LCD_DISPLAY
import SENSORS
import WAIT_ROUTINE
import ACTIONS
import TCPCommunicatorClient
import DATA_ACQUISITION_BACKUP

class State2(object):
    def state_2(self):
        global command, state
        global p1, p2, p3
        global hvgv
        print "STATE 2 : MAINTAIN VACUUM\n"

        LCD_DISPLAY.main("STATE 2")  # Display LCD : STATE 2

        while :
            # Update command log
            state = "STATE 2"

            while command == "":  # Command received ?

                # Error log
                if hvgv == 1:
                    if p3 < 5*10^(-2):
                        if p2 < 10^(-5):
                        # Received USB command
                        else:
                            # Display Warning
                            if p2 < 10^(-2):
                            else:
                                # Error Log


                                STATE_4.state_4()
                    else :
                     # Error log

                     STATE_4.state_4()
                else :
                # Error log

                    STATE_4.state_4()
            if state == "STATE 3":
                STATE_3.state_3()
            else :
                WAIT_ROUTINE.wait_routine(state)
                # Return USB message : Invalid command