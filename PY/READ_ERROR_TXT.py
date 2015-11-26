# --------------------------------------
# READ_ERROR_TXT
# --------------------------------------

# -+- IMPORT -+-
import logging

def read_error_txt(error_num):
    global contents
    global send_error
    f = open(error_num + ".txt", "r")
    contents = f.readlines()
    if 'Critical' in contents:
        send_error = True
    f.close()
    error_log(contents)

def error_log(contents):

    # create logger
    logger = logging.getLogger('error.log')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    message = contents]

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %s', datefmt='%m/%d/%Y %I:%M:%S %p', message) # Timestamp/Error Code/Error information/Importance

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')