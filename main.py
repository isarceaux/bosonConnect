# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from BosonSDK import *
import serial

myCam = CamAPI.pyClient(manualport="/dev/ttyACM0")
myCam.bosonRunFFC()

result, serialnumber = myCam.bosonGetCameraSN()

myCam.Close
# Useful to put a stop point for using debugging on that last line !