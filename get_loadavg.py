#!/usr/bin/python
import os
def load_stat():
	loadavg = {}
	f = open('/proc/loadavg')
	con = f.read().split()
	f.close()
	loadavg['lavg_1'] = con[0]
	loadavg['lavg_5'] = con[1]
	loadavg['lavg_15'] = con[2]
	loadavg['nr'] = con[3]
	loadavg['last_pid'] = con[4]
	return loadavg

loadavg = load_stat()
print 'CPU and IO utilization in 1 min: %s' % loadavg['lavg_1']
print 'CPU and IO utilization in 5:mins %s' % loadavg['lavg_5']
print 'CPU and IO utilization in 15 mins %s' % loadavg['lavg_15']
print 'Current Running Process/Total Running Process %s' % loadavg['nr']
print 'Last Used PID: %s' % loadavg['last_pid']
