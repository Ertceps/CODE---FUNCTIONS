# --------------------------------------
# WAIT ROUTINE
# --------------------------------------

#-+- IMPORT -+-
import STATE_4
import READ_ERROR_TXT
import LOCAL


def wait_routine(state):
    global mode
    if state != "STATE 3":
        error = "Error 5502"  # Send error 5521 to chamber control
        READ_ERROR_TXT.read_error_txt(error)
        STATE_4.state_4() #Go to State 4 : Safe State
    elif mode == "LOCAL":
        error = "Error 5521"  # Send error 5521 to chamber control
        READ_ERROR_TXT.read_error_txt(error)
        LOCAL.local()#Exit automatic sequence