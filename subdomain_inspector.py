#!/usr/bin/env python

"""
subdomain_inspector
	@version : 0.1.0
	@author : Daniel Ríos Linares (c) 2018, hasbornasu@gmail.com
	@description : a very simple script to get a server subdomains
		around 150000 checks per hour

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

"""
Example:
	Berkeley's webpage subdomains found
	domain = 'https://www.ssl.berkeley.edu/~'

	the script will run from 0 to infinity (until you interrupt)
	Will test a,b,c,...,aa,ab,ac,...,ba,bb,bc,...,dashjdhasjdhjkasd,...

	number of checks per hour (approximation based on 1 hour running)
		150000

	subdomain vs index
		pcb     743
		seb     798
		ccc     1406
		dwc     1927
		ptf     3889
		eag     4060
		zog     4445
		pli     5709
		cmj     6398
		jwl     8017
		teq     10939
		sdt     12940
		ast     13312
		jvv     14751
		jmcd     54401
		wind     61746
		clee     73296
		bale     77741
		euve     85024
		jorg     117321
		echi     145396
		patj     171043
		fsmj     166769

"""

# Import the requests package to communicate with the internet
import requests
# HTML string manipulation
from lxml import html
# List of lowercase alphanumerics:
from string import ascii_lowercase, digits
# Thread boost
import _thread as thread

# Domain
domain = "https://www.ssl.berkeley.edu/~"

# Digits base
dig_db = ascii_lowercase

# From an url
def isAvailable(url):
	# Try to...
	try:
		# ...get page content
		pageContent = requests.get(url)
		tree = html.fromstring(pageContent.content)
		# ...get the text in the xpath selected
		x = tree.xpath('/html/body/h1/text()')[0]
		# ...if is not found or is forbidden
		if x[0] == 'N' or x[0] == 'F':
			# ...then the subdomain is not interesting
			return False
		else:
			return True
	# ...if cannot be found, then the subdomain exists! :D
	except: return True

# Given a number, a base and a digit list...
def int2base(x):
	# Get all the digits by dividing one after another
	digits = []
	base = len(dig_db)
	while abs(x) != 0:
		i = int(x % base)
		digits = digits + [dig_db[i]]
		x = int(x / base)

	# Return the digits
	return ''.join(digits)

def subdomain_travel(i_start, i_increment):

	# Counter start
	i = i_start
	# Forever...
	while 1 == 1:
		# ...get subdomain
		subdomain = int2base(i)
		# ...get url
		url = domain + subdomain
		# ...if it's available...
		if isAvailable(url):
			# ...print it
			print(subdomain,"   ",i)
		# ...if not...
		else:
			# ...do nothing
			pass
		# ...next
		i += i_increment

if __name__ == '__main__':

	# Number of parallel processes
	number_of_threads = 128

	# Initial index
	i_start = 1

	# Create the threads
	for i in range(i_start,number_of_threads+i_start):
		thread.start_new_thread(subdomain_travel, (i,number_of_threads))

	# Pause the sys.exit
	while 1 == 1:
		pass
