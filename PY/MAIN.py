########################################################################################################################

 #  VACUUM CHAMBER CONTROL  #

########################################################################################################################

# -+- IMPORT -+-
import time
import threading
import SENSORS
import ACTIONS
import SWITCHES
import REMOTE_LOCAL
import BACKUP
import TCPCommunicatorClient
import LCD_DISPLAY
from STATE_MACHINE import Machine, State, MachineError

start = time.time()


class System(object):

    # Define states
    states = ['STATE 0', 'STATE 1', 'STATE 2', 'STATE 3', 'STATE 4']

    def __init__(self, name):

        self.name = name

        # Initialize the state machine
        self.machine = Machine(model=self, states=System.states, initial='STATE 0')

        # Add transition
        # Transition between state 0 to state 1
        self.machine.add_transition(trigger='establish_vacuum', source='STATE 0', dest='STATE 1')
        # Transition between state 1 to state 2
        self.machine.add_transition(trigger='', source='STATE 1', dest='STATE 2')
        # Transition between state 2 to state 3
        self.machine.add_transition(trigger='venting chamber', source='STATE 2', dest='STATE 3')
        # Transition between state 3 to state 0
        self.machine.add_transition(trigger='', source='STATE 3', dest='STATE 0')
        # Transition between state 1 to state 4
        self.machine.add_transition(trigger='stop', source='STATE 1', dest='STATE 4')
        # Transition between state 4 to state 1
        self.machine.add_transition(trigger='establish vacuum', source='STATE 4', dest='STATE 1')
        # Transition between state 3 to state 4
        self.machine.add_transition(trigger='stop', source='STATE 3', dest='STATE 4')
        # Transition between state 4 to state 3
        self.machine.add_transition(trigger='venting_chamber', source='STATE 4', dest='STATE 3')
        # Transition between state 2 to state 4
        self.machine.add_transition(trigger='', source='STATE 2', dest='STATE 4')


# --------------------------------------
# MAIN
# --------------------------------------s
def main():
    global mode
    # SETUP
    REMOTE_LOCAL.gpio_setup_mode()  # Setup the GPIOs for the modes LOCAL/REMOTE controlled with the Switch key
    SENSORS.gpio_setup_sensors()  # Setup the GPIOs of the sensors P1 / P2 / P3
    SWITCHES.gpio_setup_switches()  # Setup the GPIOs of the switches
    ACTIONS.gpio_setup_relays()  # Setup the GPIOs of the 4 relays to control (PP/TMP/VV/HVGV)
    LCD_DISPLAY.start()  # Display message on start

    # THREADS
    thread_mode = threading.Thread(target=REMOTE_LOCAL.get_mode, args="Mode")
    thread_tcp_ip_main = threading.Thread(target=TCPCommunicatorClient.main(), args="TCP IP")
    thread_sensors = threading.Thread(target=SENSORS.get_sensors, args="Sensors")
    thread_backup = threading.Thread(target=BACKUP.backup_files, args="Backup")

    thread_mode.start()
    if mode == "REMOTE":
        thread_tcp_ip_main.start()
    thread_sensors.start()
    thread_backup.start()

    print("Main complete")

if __name__ == "__main__":
    main()
print "Elapsed Time: %s" % (time.time() - start)