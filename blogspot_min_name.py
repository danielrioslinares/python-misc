#!/usr/bin/env python

"""
blogspot_min_name
	@version : 0.1.0

	@author : Daniel Ríos Linares (c) 2018, hasbornasu@gmail.com

	@description : a very simple script to test the minimal length domain on
		blospot (blogger)
		
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

# Import the requests package to communicate with the internet
import requests
# HTML string manipulation
from lxml import html
# List of lowercase alphanumerics:
from string import ascii_lowercase, digits


# <function isBlogspotAvailable(url)>
# 	@argument <string url> : url to test
#
#	@returns <boolean blogspotAvailable> : True if it's available, False if not
#
# 	@description : tests the url for XPATH of unavailable
#
#	@example :
#		isBlogspotAvailable('a.blogspot.com') should return False
#
#	@name : isBlogspotAvailable
#		    | |       |
#		    | |       Available?
#		    | Blogspot
#		    Is
#
# 	@author : Daniel Ríos Linares
#
#	@version : 0.1.0
#
# 	@references : NONE
def isBlogspotAvailable(url):
	pageContent = requests.get(url)
	tree = html.fromstring(pageContent.content)
	try:
		x = tree.xpath('//*[@id="maia-main"]/h1/text()')[0]
		if x == 'No se ha encontrado el blog.':
			return False
		if x == 'El blog se ha eliminado.' or 'Vas a ser redireccionado':
			return True
	except:
		return True

if __name__ == '__main__':
	C = list(ascii_lowercase) + list(digits)
	L = C + [l1+l2+l3+l4 for l1 in C for l2 in C for l3 in C for l4 in C]
	for l in L:
		if l is not 'aau2':
			url = 'http://' + str(l) + '.blogspot.com.es'
			if not isBlogspotAvailable(url):
				print(l)

# End of blogspot_min_name.py
