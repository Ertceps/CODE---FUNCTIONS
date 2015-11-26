# --------------------------------------
# ERROR - THE MONSTER
# --------------------------------------

# -+- IMPORT -+-
import time
import READ_ERROR_TXT
import SENSORS


def error_1():
    global mode, remote
    global free_memory
    if mode == "REMOTE":  # Remote or Local ?
        if PRESSURE_CONTROL_SOFT == 1:
            if remote == "AUTOMATIC":
                if CHAMBER_CTRL_PROG == "CONNECTED":
                    if free_memory > 4000000: #Free memory < 4GB
                        if EMERGENCY == "OFF":
                            if FUSE == "ON":
                                if SENSORS_SIGNAL =="ON": # Check if a signal from sensors is received
                                    if SIGNAL == 10 or SIGNAL == 0:  # 0 or 10 V

                                        if COMMAND_NEW == 1:
                                            if COMMAND_VALID == 1:
                                                if mode == "LOCAL":
                                                    error_2()
                                                else:
                                                    error = "Error 5514"
                                                    READ_ERROR_TXT.read_error_txt(error)
                                                if mode == "REMOTE":
                                                    if GUI == 1:
                                                        if remote == "AUTOMATIC":
                                                            error = "Error 5515"
                                                            READ_ERROR_TXT.read_error_txt(error)
                                                        else:
                                                            error_2()
                                                    else:
                                                        error_2()
                                                else:
                                                    error = "Error 5513"
                                                    READ_ERROR_TXT.read_error_txt(error)
                                            else:
                                                error = "Error 5518"
                                                READ_ERROR_TXT.read_error_txt(error)
                                        else:
                                            error = "OK"
                                            READ_ERROR_TXT.read_error_txt(error)
                                    else:
                                        error = "Error 5509"
                                        READ_ERROR_TXT.read_error_txt(error)
                                else:
                                    error = "Error 5508"
                                    READ_ERROR_TXT.read_error_txt(error)
                            else:
                                error = "Error 5512"
                                READ_ERROR_TXT.read_error_txt(error)
                        else:
                            error = "Error 5501"
                            READ_ERROR_TXT.read_error_txt(error)
                    elif free_memory < 1000: #Free memory < 1MB:
                            error = "Error 5520"
                            READ_ERROR_TXT.read_error_txt(error)
                    else:
                        error = "Error 5519"
                        READ_ERROR_TXT.read_error_txt(error)
                else:
                    error = "Error 5517"
                    READ_ERROR_TXT.read_error_txt(error)
        else:
            error = "Error 5516"
            READ_ERROR_TXT.read_error_txt(error)


def error_2():
    # global command, error
    # global p1, p2, p3
    # global vv
    if command == "STATE 1":  # Establish vacuum ?
        p1_0 = p1
        p2_0 = p2
        time.sleep(1)
        p1_1 = p1
        p2_1 = p2
        if (p1_1 < p1_0) and (p2_1 < p2_0):  # Pressure decreasing ?
            error = "OK"
            READ_ERROR_TXT.read_error_txt(error)
        else:
            p1_3 = p1
            p2_3 = p2
            if p1_3 <= ....................
                if p1_3 < 10^(-5) and p2_3 < 10^(-5):
                    error = "OK"
                    READ_ERROR_TXT.read_error_txt(error)
                elif SIGNAL_to_TMP == 1:
                    if p1_3 < 10^(-2) and p2_3 < 10^(-2):
                        error = "Error 5510"
                        READ_ERROR_TXT.read_error_txt(error)
                    else:
                        error = "Error 5504"
                        READ_ERROR_TXT.read_error_txt(error)
                elif p1_3 > 950 and p2_3 > 950: # Check if the pressure is over 950hPa = 950mbar - (atm pressure = 1013hPa) - Max range TPG 300 (1000 hPa)
                    error = "Error 5505"
                    READ_ERROR_TXT.read_error_txt(error)
                else:
                    error = "OK"
                    READ_ERROR_TXT.read_error_txt(error)
            elif PP_FUSE == "..........":
                error = "Error 5503"
                READ_ERROR_TXT.read_error_txt(error)
            else:
                error = "Error 5510"
                READ_ERROR_TXT.read_error_txt(error)
    elif command == "STATE 3":  # Vent the chamber ?
        p1_0 = p1
        p2_0 = p2
        time.sleep(1)
        p1_1 = p1
        p2_1 = p2
        if (p1_1 > p1_0) and (p2_1 > p2_0):  # Check if Pressure rising ?
            error = "OK"
        elif vv == 1:  # Check if vv open ?
            error = "Error 5507"
            READ_ERROR_TXT.read_error_txt(error)
        else:
            error = "Error 5506"
            READ_ERROR_TXT.read_error_txt(error)
    else:
        error = "Error 5502"
        READ_ERROR_TXT.read_error_txt(error)
	   
with open ("data.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')