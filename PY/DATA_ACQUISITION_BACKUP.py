# --------------------------------------
# DATA ACQUISITION (PHYSICAL/COMMAND) - BACKUP 
#--------------------------------------

# -+- IMPORT -+-
import threading  # to do multi-tasking actions
import os  # to get file size
import time
import datetime
import shutil

tLock = threading.Lock()


# Write the Physical data in a log file
class PhysicalWrite(threading.Thread):
    def __init__(self, data, out, state):
        threading.Thread.__init__(self)
        self.state = state
        self.data = data
        self.out = out
        if self.state == "STATE 0":
            tLock.acquire()
        else:
            tLock.release()


def run(self):
    global SIZE_physical
    f = open(self.out, "a")
    f.write(self.data[1] + '\n')  # Timestamp
    f.write('Pirani P1' + self.data[2] + 'mbar \n')  # Pirani P1 (Pressure mbar)
    f.write('Cold Cathod P2' + self.data[3] + 'mbar \n')  # Cold Cathod P2 (Pressure mbar)
    f.write('Pirani P3' + self.data[4] + 'mbar \n')  # Pirani P3 (Pressure mbar)
    f.write('HVGV status' + self.data[5] + '\n')  # HVGV status (OPEN,CLOSED,OPENING,CLOSING)
    f.write('VV status' + self.data[6] + '\n')  # VV status (OPEN,CLOSED)
    f.write('PP status' + self.data[7] + '\n')  # PP status (ON,OFF)
    f.write('TMP status' + self.data[8] + '\n\n')  # TMP status (ON,OFF)
    f.write('TMP Flood Valve status' + self.data[9] + '\n\n')  # TMP status (ON,OFF)
    f.close()
    time.sleep(1)
    print("Finished Background file write to " + self.out)

    file_info = os.stat(self.out)
    SIZE_physical = file_info.st_size  # return the file size in bytes


# Write the commands in a log file
class CommandWrite(threading.Thread):
    def __init__(self, data, out):
        threading.Thread.__init__(self)
        self.state = data[3]
        self.data = data
        self.out = out
        if self.state == "STATE 0":
            tLock.acquire()
        else:
            tLock.release()

    def run(self):
        global SIZE_command
        f = open(self.out, "a")
        f.write(self.data[1] + '\n')  # Timestamp
        f.write('Command requested' + self.data[2] + 'mbar \n')  # Command
        f.write('Controllers current state' + self.data[3] + 'mbar \n\n')  # State
        f.close()
        time.sleep(1)
        print("Finished Background file write to " + self.out)

        file_info = os.stat(self.out)
        SIZE_command = file_info.st_size  # return the file size in bytes


def get_backup_directory(base_directory):
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    return base_directory.format(date)


def copy_files_to(srcdir, dstdir):
    for file in os.listdir(srcdir):
        file_path = os.path.join(srcdir, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dstdir)


def copy_files(dstdir):
    copy_files_to(GOOGLE_DRIVE_DIRECTORY, dstdir)


def backup(thread_name):
    while 1 < 2:  # To run forever
        copyfile(src, dst)  # copy and paste the file named src to dst
    time.sleep(1)  # Save backup of the data every 1 sec (frequency 1Hz)
    print "%s"