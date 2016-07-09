# RemoteToPC
Control your laptop or pc using TV remote with power of Python and Arduino.
This is made for Windows originally. It might require a bit of tweaking for other OS'.

#Usage
* Upload the code to Arduino. Sensor should be on pin 11.
* Configure your remote by running config_ir.py. It will ask you to press buttons for the functions shown. 
* Run recieve.py.

###Requirements
* Python2
* Pyserial and win32api
* Arduino with IRremote library.
* TV IR sensor

###To Do
- [ ] Add mouse control.
