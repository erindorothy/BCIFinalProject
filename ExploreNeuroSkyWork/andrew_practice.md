Andrew Washington

From my terminal  
* after copying mindwave.py from [mindwave-python](https://github.com/BarkleyUS/mindwave-python). 
* using python 3 (in condo env)  
* on macOS   

```
Andrews-MacBook-Pro:bci andrew$ ls
mindwave.py
Andrews-MacBook-Pro:bci andrew$ python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mindwave
>>> headset = mindwave.Headset('/dev/tty.MindWave', 'MMSQH02478')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mindwave.py", line 231, in __init__
    self.serial_open()
  File "mindwave.py", line 256, in serial_open
    self.dongle = serial.Serial(self.device, 115200)
AttributeError: 'module' object has no attribute 'Serial'
>>> quit()
Andrews-MacBook-Pro:bci andrew$ conda env list
# conda environments:
#
ipykernel_py2            /Users/andrew/miniconda3/envs/ipykernel_py2
lab                      /Users/andrew/miniconda3/envs/lab
py3                      /Users/andrew/miniconda3/envs/py3
root                  *  /Users/andrew/miniconda3

Andrews-MacBook-Pro:bci andrew$ . activate py3
(py3) Andrews-MacBook-Pro:bci andrew$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mindwave
>>> headset = mindwave.Headset('/dev/tty.MindWave', '')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/andrew/Documents/Projects/bci/mindwave.py", line 231, in __init__
    self.serial_open()
  File "/Users/andrew/Documents/Projects/bci/mindwave.py", line 256, in serial_open
    self.dongle = serial.Serial(self.device, 115200)
AttributeError: module 'serial' has no attribute 'Serial'
>>> headset = mindwave.Headset('/dev/tty.MindWave', 'MMSQH02478')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/andrew/Documents/Projects/bci/mindwave.py", line 231, in __init__
    self.serial_open()
  File "/Users/andrew/Documents/Projects/bci/mindwave.py", line 256, in serial_open
    self.dongle = serial.Serial(self.device, 115200)
AttributeError: module 'serial' has no attribute 'Serial'
>>> quit*(
... ()
...
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> quit()
(py3) Andrews-MacBook-Pro:bci andrew$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mindwave import mindwave
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'mindwave'
>>> import mindwave
>>> mindwave.
mindwave.ATTENTION             mindwave.POOR_SIGNAL
mindwave.AUTOCONNECT           mindwave.RAW_VALUE
mindwave.BLINK                 mindwave.REQUEST_DENIED
mindwave.CONNECT               mindwave.STANDBY_SCAN
mindwave.DISCONNECT            mindwave.STATUS_CONNECTED
mindwave.EXCODE                mindwave.STATUS_SCANNING
mindwave.HEADSET_CONNECTED     mindwave.STATUS_STANDBY
mindwave.HEADSET_DISCONNECTED  mindwave.SYNC
mindwave.HEADSET_NOT_FOUND     mindwave.select
mindwave.Headset(              mindwave.serial
mindwave.MEDITATION            mindwave.threading
>>> mindwave.
mindwave.ATTENTION             mindwave.POOR_SIGNAL
mindwave.AUTOCONNECT           mindwave.RAW_VALUE
mindwave.BLINK                 mindwave.REQUEST_DENIED
mindwave.CONNECT               mindwave.STANDBY_SCAN
mindwave.DISCONNECT            mindwave.STATUS_CONNECTED
mindwave.EXCODE                mindwave.STATUS_SCANNING
mindwave.HEADSET_CONNECTED     mindwave.STATUS_STANDBY
mindwave.HEADSET_DISCONNECTED  mindwave.SYNC
mindwave.HEADSET_NOT_FOUND     mindwave.select
mindwave.Headset(              mindwave.serial
mindwave.MEDITATION            mindwave.threading
>>> mindwave.Headset?
  File "<stdin>", line 1
    mindwave.Headset?
                    ^
SyntaxError: invalid syntax
>>> help mindwave.Headset
  File "<stdin>", line 1
    help mindwave.Headset
                ^
SyntaxError: invalid syntax
>>> help(mindwave.Headset)

>>> help(mindwave.Headset)

>>> headset = mindwave.Headset('/dev/tty.MindWave', 'MMSQH02478', open_serial=False)
>>> headset.connect()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/andrew/Documents/Projects/bci/mindwave.py", line 242, in connect
    self.dongle.write(''.join([CONNECT, headset_id.decode('hex')]))
AttributeError: 'NoneType' object has no attribute 'write'
>>> headset.connect()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/andrew/Documents/Projects/bci/mindwave.py", line 242, in connect
    self.dongle.write(''.join([CONNECT, headset_id.decode('hex')]))
AttributeError: 'NoneType' object has no attribute 'write'
>>> headset = mindwave.Headset('/dev/tty.MindWave', 'MMSQH02478', open_serial=False)
>>> while True:
...     print "Attention 1: %s, Meditation 1: %s" % (h1.attention, h1.meditation)
  File "<stdin>", line 2
    print "Attention 1: %s, Meditation 1: %s" % (h1.attention, h1.meditation)
                                            ^
SyntaxError: invalid syntax
>>> while True:    print "Attention 2: %s, Meditation 2: %s" % (h2.attention, h2.meditation)
  File "<stdin>", line 1
    while True:    print "Attention 2: %s, Meditation 2: %s" % (h2.attention, h2.meditation)
                                                           ^
SyntaxError: invalid syntax
>>> while True:print "Attention 2: %s, Meditation 2: %s" % (h2.attention, h2.meditation)
  File "<stdin>", line 1
    while True:print "Attention 2: %s, Meditation 2: %s" % (h2.attention, h2.meditation)
                                                       ^
SyntaxError: invalid syntax
>>> while True:print headset.attention
  File "<stdin>", line 1
    while True:print headset.attention
                           ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(True:print headset.attention)?
>>> while True:print(headset.attention)
...
KeyboardInterrupt
>>> print headset.status
  File "<stdin>", line 1
    print headset.status
                ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(headset.status)?
>>> print(headset.status)
None
>>> headset
<mindwave.Headset object at 0x10d32a9e8>
>>> headset = mindwave.Headset('/dev/tty.MindWave', 'MMSQH02478', open_serial=False)
>>> print(headset.status)
None
>>> while True:print(headset.attention)
...
KeyboardInterrupt
>>> quit()
```
