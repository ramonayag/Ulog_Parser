# Ulog_Parser

* [Extract_Plot_ulog.py](https://github.com/ramonayag/Ulog_Parser/blob/master/extract_plot_ulog.py)
  * Script parses and plots the ulog actuator_controls_0 data, as well as all of the log messages as a function of time

* [test.ulg](https://github.com/ramonayag/Ulog_Parser/blob/master/test.ulg)
  * ulog file data collection log: created every flight containing all data from/of sensors, odometry, and other vehicle operation statistics

* [actuator_message_plot.png](https://github.com/ramonayag/Ulog_Parser/blob/master/actuator_message_plot.png)
  * Time vs 7 Actuator Controllers + Log Messages 

**Assumption:**
* actuator data is labelled as "*controller*"
* timestamps are plotted in scientific notation with 1 sig fig (1 value after the decimal)

**Prelimainary Steps:**   
1. pip install pyulog


**Use scripts to analyze ulog data:**   
1. Download scripts from github [PX4/pyulog](https://github.com/PX4/pyulog#scripts) from github
2. Run in cli "python3 setup.py build install" 
3. Add ulog file (.ulg) to pyulog folder 
4. Now can run scripts 
* ulog_info {filename.ulg}
* ulog_messages {filename.ulg}
...


**Tasks**
- [ ] Indicate different type of log messages (commander, logger, ...) on graph with different colors, maybe even hover over vertical line for log message?
