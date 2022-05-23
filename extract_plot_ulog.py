#first install 
#	pip install pyulog

#Navigate to folder (contains your ulog file and python script)

from pyulog import *
import sys
from matplotlib import pyplot as plt

filename = "test.ulg"

# load the log and extract the necessary data for the analyses
try:
	ulog = ULog(filename)
except FileNotFoundError:
	print("Error: file {} is found:".format(filename))
	sys.exit()


#get data from the actuator
actuator_outputs = ulog.get_dataset('actuator_controls_0',).data
timestamp = actuator_outputs['timestamp']


#intialize size of plot 
plt.figure(figsize = (15,6))

#Add each timestamp and controller to plot  
for key, value in actuator_outputs.items():
	# only add to graph if == actuator_outputs (not for timestamps)
	if key.__contains__('control'):
		plt.plot(timestamp, value, label = key)

#messages can be viewed in cli "ulog_messages <filename.ulg> 
for mes in ulog.logged_messages: 
	#adjust timestamp for legend 
	scientificNotTime = "{:e}".format(mes.timestamp)
	scientificNotTime =  '{:.2e}'.format(float(scientificNotTime))[:3]
	
	plt.axvline( x=mes.timestamp, ls=':', lw=2, color='y', label = "{}: {} ".format(scientificNotTime, mes.message))
		
	#labeling vertical lines -->  messy result, and overlapping
	#plt.text(mes.timestamp,0.4, es.message, rotation=90)
	
	#testing - see timestamps and logged messages
	#print(mes.timestamp, mes.message)

# place legend outside
#plt.legend(bbox_to_anchor=(1, -0.1), loc='center left', ncol=1)
ax = plt.subplot(111)
# Shrink current axis's height by 20% on the bottom
box = ax.get_position()
# set_position[left, bottom, width, height]
ax.set_position([box.x0, box.y0 + box.height * 0.3,
                 box.width, box.height * 0.8])

# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3)

plt.ylabel('actuator_controls_0')
plt.xlabel('timestamps')
#plt.subplots_adjust(left=0.1, right=0.1, top=0.1, bottom=10)
plt.show()
