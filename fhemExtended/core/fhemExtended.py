import sys,os
import time
import spidev
import fhem
import numpy as np

sys.path.append('/opt/fhemExtended/RPiSensors')
import max6675

header = """\
   __ _                    ______      _                 _          _ 
  / _| |                  |  ____|    | |               | |        | |
 | |_| |__   ___ _ __ ___ | |__  __  _| |_ ___ _ __   __| | ___  __| |
 |  _| '_ \ / _ \ '_ ` _ \|  __| \ \/ / __/ _ \ '_ \ / _` |/ _ \/ _` |
 | | | | | |  __/ | | | | | |____ >  <| ||  __/ | | | (_| |  __/ (_| |
 |_| |_| |_|\___|_| |_| |_|______/_/\_\\__\___|_| |_|\__,_|\___|\__,_|
"""                                                                      
                                                                     
print header

fh = fhem.Fhem("fhem")
sensor = max6675.Max6675(0, 0)

old_temp = -999

def getTempMax6675(measurments, rate, std):
	i = np.array([])
	for j in range(0,measurments):
		i = np.append(i,[sensor.temperature])
		time.sleep(rate)
	print i
	print "Std: ",np.std(i)
	print "Med: ",np.median(i).round(1)
	if(np.std(i) <= std):
		temp = np.median(i).round(1)
		global old_temp
		old_temp = temp
		return temp
	else:
		return old_temp

while 1:
	fh.send_cmd("setreading temp t  "+str(getTempMax6675(10, 0.5, 5)))
	time.sleep(5)



