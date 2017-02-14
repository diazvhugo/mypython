#!/usr/bin/python

SSH_LOG_FILE_NAME = '/var/log/syslog'

for line in open(SSH_LOG_FILE_NAME):
      print "Time: ", line.split()[2], "Process: ", line.split()[3]
      print "Session: ", line.split()[4]
