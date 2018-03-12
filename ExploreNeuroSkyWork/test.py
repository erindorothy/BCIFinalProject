# This file was written by Gael Van der Le


from NeuroPy import NeuroPy
import platform
import serial
import time

if platform.system() == 'Windows':
    sky = NeuroPy.Neuropy("COM6", 57600)
else:
    sky = NeuroPy.NeuroPy("/dev/rfcomm0", 57600)


def attention_callback(attention_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    print("Value of attention is", attention_value)
    # do other stuff (fire a rocket), based on the obtained value of attention_value
    # do some more stuff
    return None


# set call back:
sky.setCallBack("attention", attention_callback)

# call start method
sky.start()

while True:
    if (sky.meditation > 70):  # another way of accessing data provided by headset (1st being call backs)
        sky.stop()  # if meditation level reaches above 70, stop fetching data from the headset
