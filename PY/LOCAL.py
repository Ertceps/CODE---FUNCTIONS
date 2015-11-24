# --------------------------------------
# LOCAL
# --------------------------------------

# -+- IMPORT -+-
import time
import os
import ACTIONS
import SWITCHES



def local():
    if SWITCHES.SW_PP_PIN == 1:
        ACTIONS.pp_on()
    if SWITCHES.SW_TMP_PIN == 1:
        ACTIONS.tmp_on()
    if SWITCHES.SW_VV_PIN == 1:
        ACTIONS.vv_on()
    if SWITCHES.SW_HVGV_PIN == 1:
        ACTIONS.hvgv_on()

    if SWITCHES.SW_PP_PIN == 0:
        ACTIONS.pp_off()
    if SWITCHES.SW_TMP_PIN == 0:
        ACTIONS.tmp_off()
    if SWITCHES.SW_VV_PIN == 0:
        ACTIONS.vv_off()
    if SWITCHES.SW_HVGV_PIN == 0:
        ACTIONS.hvgv_off()