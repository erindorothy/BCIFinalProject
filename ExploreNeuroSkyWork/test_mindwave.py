# This file was written by Gael Van der Le

import mindwave

headset = mindwave.Headset('/dev/tty.MindWave', 'MMSQH02478', open_serial=False)

while True:
    print(headset.attention)
