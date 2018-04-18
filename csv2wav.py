#!/usr/bin/python

"""
csv2wav
	@version : 0.1.0
	@author : Daniel Ríos Linares (c) 2018, hasbornasu@gmail.com
	@description : a very simple script to convert .csv files to .wav (from an
        oscilloscope for example)

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

import csv
import wave
import struct
from datetime import datetime

# Target
filename = 'test.csv' # .csv file
f = 4000 # resampling frequency, minimum is 8*FS (in Hz)
gain = 2048*4 # gain from normalization to 1

# Data read and amplitude normalization
print('Normalizing data...')
data = [float(value) for time, value in csv.reader(open(filename, 'U'), delimiter=',')]
data = [d/abs(max(data)) for d in data]

# Create a new .wav named with the format "<name>_<date>"
print('Opening the file...')
wavfilename = filename + '_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.wav'
wavfile = wave.open(wavfilename, 'w')

# Audio file parameters
wavfile.setparams(
    (1, # mono
    2, # bytes
    f, # Sampling frequency
    len(data), # number of samples
    'NONE', # compression type (only 'NONE available')
    'not compressed' # compression method (only 'not compressed' available)
    ))

# Because Wave_file.writeframes(data) requires a "bytes-like" object
print('Converting to bytes...')
data_bytes = b''.join([struct.pack('<h', int(d*gain)) for d in data])

# Write the frames into the Wave_write file
print('Writing the .wav')
wavfile.writeframes(data_bytes)
wavfile.close()
