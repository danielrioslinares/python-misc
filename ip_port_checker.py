#!/usr/bin/env python

"""
ip_port_checker
	@version : 0.1.0
	@author : Daniel Ríos Linares (c) 2018, hasbornasu@gmail.com
	@description : a very simple script to check open ports, is pretty slow

	@license : GPL-3.0
		This program is free software: you can redistribute it and/or modify
		it under the terms of the GNU General Public License as published by
		the Free Software Foundation, either version 3 of the License, or
		(at your option) any later version.
		This program is distributed in the hope that it will be useful,
		but WITHOUT ANY WARRANTY; without even the implied warranty of
		MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
		GNU General Public License for more details.
		You should have received a copy of the GNU General Public License
		along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Provides access to the socket interface
import socket

# Numpy for saving text
import numpy as np


# <function isIPPortOpen(ip, port)>
# 	@argument <string ip> : IP address you want to test
#
#	@returns <boolean IPPortOpen> : True if it's open, False if not
#
# 	@description : tests the IP address and the port
#
#	@name : isIPPortOpen
#		    | | |   |
#		    | | |   Open?
#		    | | Port
#		    | IP address
#		    Is
#
# 	@author : Daniel Ríos Linares
#
#	@version : 0.1.0
#
# 	@references : NONE
def isIPPortOpen(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect( (ip, int(port)) )
		s.shutdown(socket.SHUT_RD)
		print("Port",i,"is open")
		return 1
	except:
		print("Port",i,"is closed")
		return -1


if __name__ == '__main__':

	# Number of threads
	number_of_threads = 2

	# Initial and final ports
	ip_start = 0
	ip_finish = 65535

	# IP goes here
	IP = ""


	# Print out all ports at once
	for i in range(ip_start,ip_finish+1):
		isIPPortOpen(IP, i)
