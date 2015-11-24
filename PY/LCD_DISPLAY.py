# --------------------------------------
# LCD DISPLAY
# --------------------------------------

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED - CAN BE USED FOR 8 BITS
# 8 : Data Bit 1             - NOT USED - CAN BE USED FOR 8 BITS
# 9 : Data Bit 2             - NOT USED - CAN BE USED FOR 8 BITS
# 10: Data Bit 3             - NOT USED - CAN BE USED FOR 8 BITS
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

# -+- IMPORT -+-
import RPi.GPIO as GPIO  # to control GPIO
import time  # to get the time


# LCD mapping
LCD_RS = 18
LCD_E = 23
LCD_D4 = 12
LCD_D5 = 16
LCD_D6 = 20
LCD_D7 = 21

# Define some device constants
LCD_WIDTH = 16  # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

# Main program block
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)   # E
GPIO.setup(LCD_RS, GPIO.OUT)  # RS
GPIO.setup(LCD_D4, GPIO.OUT)  # DB4
GPIO.setup(LCD_D5, GPIO.OUT)  # DB5
GPIO.setup(LCD_D6, GPIO.OUT)  # DB6
GPIO.setup(LCD_D7, GPIO.OUT)  # DB7

def start():
        str_pad = " " * 16
        # START UP
        lcd_string_fix("RUAG SPACE", LCD_LINE_1)
        time.sleep(2)
        my_long_string = "VACUUM CONTROLLER"
        my_long_string = str_pad + my_long_string
        for i in range(0, len(my_long_string)):
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_text = my_long_string[i:(i+15)]
            lcd_string_scroll(lcd_text, 1)
            time.sleep(0.4)
        lcd_byte(LCD_LINE_2, LCD_CMD)
        lcd_string_scroll(str_pad, 1)


def main(state):
    global P1, P2, P3
    # Initialise display
    lcd_init()

    while True:
        str_pad = " " * 16

        # STATE 0
        if state == "STATE 0":
            lcd_string_fix("STATE 0", LCD_LINE_1)
            time.sleep(2)
            lcd_string_fix("VENTED CHAMBER", LCD_LINE_1)
            my_long_string = "P1 : " + P1 + "P2 : " + P2 + "P3 : " + P3
            my_long_string = str_pad + my_long_string
            for i in range(0, len(my_long_string)):
                lcd_byte(LCD_LINE_2, LCD_CMD)
                lcd_text = my_long_string[i:(i+15)]
                lcd_string_scroll(lcd_text, 1)
                time.sleep(0.4)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string_scroll(str_pad, 1)

        # STATE 1
        if state == "STATE 1":
            lcd_string_fix("STATE 1", LCD_LINE_1)
            time.sleep(2)
            lcd_string_fix("ESTABLISH VACUUM", LCD_LINE_1)
            my_long_string = "P1 : " + P1 + "P2 : " + P2 + "P3 : " + P3
            my_long_string = str_pad + my_long_string
            for i in range(0, len(my_long_string)):
                lcd_byte(LCD_LINE_2, LCD_CMD)
                lcd_text = my_long_string[i:(i+15)]
                lcd_string_scroll(lcd_text, 1)
                time.sleep(0.4)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string_scroll(str_pad, 1)

        # STATE 2
        if state == "STATE 2":
            lcd_string_fix("STATE 2", LCD_LINE_1)
            time.sleep(2)
            lcd_string_fix("MAINTAIN VACUUM", LCD_LINE_1)
            my_long_string = "P1 : " + P1 + "P2 : " + P2 + "P3 : " + P3
            my_long_string = str_pad + my_long_string
            for i in range(0, len(my_long_string)):
                lcd_byte(LCD_LINE_2, LCD_CMD)
                lcd_text = my_long_string[i:(i+15)]
                lcd_string_scroll(lcd_text, 1)
                time.sleep(0.4)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string_scroll(str_pad, 1)

        # STATE 3
        if state == "STATE 3":
            lcd_string_fix("STATE 3", LCD_LINE_1)
            time.sleep(2)
            lcd_string_fix("VENTING CHAMBER", LCD_LINE_1)
            my_long_string = "P1 : " + P1 + "P2 : " + P2 + "P3 : " + P3
            my_long_string = str_pad + my_long_string
            for i in range(0, len(my_long_string)):
                lcd_byte(LCD_LINE_2, LCD_CMD)
                lcd_text = my_long_string[i:(i+15)]
                lcd_string_scroll(lcd_text, 1)
                time.sleep(0.4)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string_scroll(str_pad, 1)

        # STATE 4
        if state == "STATE 4":
            lcd_string_fix("STATE 4", LCD_LINE_1)
            time.sleep(2)
            lcd_string_fix("SAFE STATE", LCD_LINE_1)
            my_long_string = "P1 : " + P1 + "P2 : " + P2 + "P3 : " + P3
            my_long_string = str_pad + my_long_string
            for i in range(0, len(my_long_string)):
                lcd_byte(LCD_LINE_2, LCD_CMD)
                lcd_text = my_long_string[i:(i+15)]
                lcd_string_scroll(lcd_text, 1)
                time.sleep(0.4)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string_scroll(str_pad, 1)


def lcd_init():
    # Initialise display
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(E_DELAY)

def lcd_string_fix(message,line):
    # Send string to display

    message = message.ljust(LCD_WIDTH, " ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def lcd_string_scroll(message,style):
    # Send string to display
    # style=1 Left justified
    # style=2 Centred
    # style=3 Right justified

    if style == 1:
        message = message.ljust(LCD_WIDTH, " ")
    elif style == 2:
        message = message.center(LCD_WIDTH, " ")
    elif style == 3:
        message = message.rjust(LCD_WIDTH, " ")

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    GPIO.output(LCD_RS, mode) # RS

    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()

    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()

def lcd_toggle_enable():
    # Toggle enable
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

if __name__ == '__main__':
  main()

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string_fix("Goodbye!",LCD_LINE_1)
    GPIO.cleanup()

