#!/usr/bin/python3
# Code to control the wind speed sensor. Write observations to disk
# Paul A. Kucera, Ph.D. and Joseph Rener
# UCAR
# Boulder, CO USA
# Email: pkucera@ucar.edu and jrener@ucar.edu
# Developed at COMET at University Corporation for Atmospheric Research and the Research Applications Laboratory at the National Center for Atmospheric Research (NCAR)

import sys
sys.path.insert(0, '/home/pi/3d_paws/scripts/')
import RPi.GPIO as GPIO, time, helper_functions, os 

# Set rest interval based on if we're testing or not
test, rest, iterations = helper_functions.getTest()

# Number of sensors in anemometer
SENSOR_NUM = 2

# Wind speed calibration factor
CAL_Factor = 2.64 # (3.14/1.19)
SCALE = CAL_Factor*(2*3.14156*0.079)/(SENSOR_NUM*rest) # wind speed in m/s

# Identify the GPIO pin for the wind sensor
PIN = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variable to keep track of how much rotations
wind = 0

# Call back function for each wind sensor reading
def cb(channel):
	global wind
	wind += 1
					
# Register the call back for pin interrupts
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=cb, bouncetime=1)

print("Wind Speed Sensor")

# Run once... or if in test mode, run every 10 seconds during the interval
for x in range (0, iterations):
	time.sleep(rest)
	try:
		wind_spd = wind*SCALE

		# Handle script output
		line = "%.4f" % (wind_spd)	
		if test:
			helper_functions.output(True, line, "test_wind_speed")
		else:
			helper_functions.output(True, line, "wind_speed")

		wind = 0

	except Exception as e:
		helper_functions.handleError(e, "wind_speed")
		GPIO.cleanup()
		pass