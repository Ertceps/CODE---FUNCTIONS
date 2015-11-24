# --------------------------------------
# TCP/IP Communication
# --------------------------------------

# Client Program
import socket
import threading
import os
import sys
import select
import SENSORS
from time import sleep


class Transmit(threading.Thread):
    def run(self):
        # Sending data to the server
        # print('Transmit started')
        global s  # connection
        global P1, P2, P3, timestamp_sensors
        global PP, TMP, TMP_FV, HVGV, VV
        global data
        data = [timestamp_sensors, P1, P2, P3, HVGV, VV, PP, TMP, TMP_FV]
        global threadRunning
        while threadRunning:
            # Read text with 0.5 sec timeout
            i, o, e = select.select([sys.stdin], [], [], 0.5)
            if i:
                string = str(data)
                byte_array = bytearray(string, "utf-8")  # Convert string into a b$
                s.sendall(byte_array)

        # print('Transmit stopped - threadRunning')
        return


class Receive(threading.Thread):
    def run(self):
        # Receiving data from the server
		# print('Receive started')
        global s  # connection
        global threadRunning
        global command
        while threadRunning:
            # Use 1 second timeout on receive
            ready = select.select([s], [], [], 1)
            if ready[0]:
                data = s.recv(1024).strip()
                if len(data) == 0:  # Connection closed by server
                    threadRunning = False
                else:
                    command = data.decode("utf-8")
                    print('Received:', command)  # Converts the receive$
                    return command

            sleep(0.1)

        # print('Receive stopped - threadRunning')
        return


def main():
    # Running main program
    host = '192.168.137.1'  # The remote host - windows machine running the LabVIEW Server
    port = 6852  # The same port as used by the server - defined in LabVIEW
    global threadRunning  # Used to stop threads
    global receive
    global transmit
    threadRunning = False
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    os.system('clear')
    print('Connection with server established')

    try:
        print(34 * '-')
        print("        M A I N - M E N U")
        print(' Press CTRL+C to close connection')
        print(34 * '-')
        # Create instance of class
        threadRunning = True
        transmit = Transmit()
        receive = Receive()
        # Start class
        transmit.start()
        receive.start()
        while threadRunning:
            sleep(0.1)

    except KeyboardInterrupt:  # Stop program when CTRL+C is pressed
        # print('Main stopped')
        threadRunning = False
        sleep(2)
        s.close()

    finally:
        s.close()
