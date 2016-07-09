# For Calibration
from time import sleep
import serial  #Communication library

print "Starting connection"

ser = serial.Serial("COM10", 9600)

#The buttons you like to map in the software. 
#Add or remove the key's you want, but THEY MAY NOT CONTAIN SPACES!
#Because they are going to be used as identifiers in another program
#this program will write.
button = ["Mute", "Vol_up", "Vol_down", "OK", "Up", "Down", "Left", "Right", "Back", "Play", "My_media"]

inp1 = [0] * len(button)
inp2 = [0] * len(button)

#Calibarate every button
for i in range(0, len(button)):
	print "Press the "+button[i]+"'s button two times -> ",
	inp1[i] = ser.readline().replace('\n', '').replace('\r', '')
	inp2[i] = ser.readline().replace('\n', '').replace('\r', '')
	print inp1[i]+" and "+ inp2[i]

print ""	

ser.close()
config = open("config_ir_values.py", 'w')

#write the buttons to the config file
for i in range(0,len(button)):
	line = button[i] + "= [" + inp1[i] + " ," + inp2[i] + "]"
	print line
	config.write(line)
	config.write("\n")

config.close()
