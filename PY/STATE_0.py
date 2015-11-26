# --------------------------------------
# STATE 0
# --------------------------------------

# -+- IMPORT -+-
import STATE_1
import STATE_MACHINE
import LCD_DISPLAY
import READ_ERROR_TXT
import LOCAL

class State0(STATE_MACHINE.State):
    def state_0(self):
        global state, command, mode
        print "STATE 0 : VENTED CHAMBER\n"

        LCD_DISPLAY.main("STATE 0")  # Display  LCD : STATE 0

        # Update command log
        state = "STATE 0"
        command = "VC_vent"

        # Stop Data acquisition
        # Data acquisition automatically stopped when COMMAND = "STATE 0"

        while state == "STATE 0":
            while command == "VC_vacuum":  # Receive command
                if state == "STATE 1":
                    STATE_1.State1.state_1()
                elif mode == "LOCAL":
                    error = "Error 5521"  # Send error 5521 to chamber control
                    READ_ERROR_TXT.read_error_txt(error)
                    LOCAL.local()  # Exit Remote sequence
                    print "REMOTE MODE EXIT"