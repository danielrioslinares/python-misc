


from svgwrite.shapes import Rect
import svgwrite
import os
from collections import namedtuple
import cairosvg



class GuitarMeasure:

	# Sizes
	MEASURES_PER_LINE = 6
	MEASURE_HEIGHT = 1.0
	MEASURE_WIDTH = 1.2
	MEASURE_VERTICAL_GAP = 0.35

	# Colors
	COLORS__ACOUSTIC_GUITAR_STRINGS = tuple( [svgwrite.rgb(90, 90, 90, '%')] * 3 + [svgwrite.rgb(100, 50, 0, '%')] * 3 )
	COLORS__ACOUSTIC_GUITAR_FINGERS = ( svgwrite.rgb(100, 40, 0, '%'), svgwrite.rgb(80, 0, 80, '%'), svgwrite.rgb(0, 0, 100, '%'), svgwrite.rgb(100, 0, 0, '%') )
	COLOR__ACOUSTIC_GUITAR_MEASURE = svgwrite.rgb(15, 15, 15, '%')
	COLOR__ACOUSTIC_GUITAR_BARLINE = svgwrite.rgb(80, 80, 80, '%')

	# String width
	WIDTHS__ACOUSTIC_GUITAR_STRINGS = (1.2,1.4,1.6,1.6,1.8,2.0)

	# Text
	SIZE_FONT = 0.075

	def __init__(self, dwg_file='test.svg', string_widths=None, string_colors=None, measure_color=None, barline_color=None, finger_colors=None ):

		# Position of the measures
		self._cnt = 0

		# Overwrite
		try:
			os.remove(dwg_file)
			os.remove(dwg_file + str(".pdf"))
		except: pass

		# Create drawing
		self.dwg_file = dwg_file
		self.dwg = svgwrite.Drawing( dwg_file )

		# Colors
		self.string_colors = self.COLORS__ACOUSTIC_GUITAR_STRINGS if string_colors is None else string_colors
		self.string_widths = self.WIDTHS__ACOUSTIC_GUITAR_STRINGS if string_widths is None else string_widths
		self.finger_colors = self.COLORS__ACOUSTIC_GUITAR_FINGERS if finger_colors is None else finger_colors
		self.measure_color = self.COLOR__ACOUSTIC_GUITAR_MEASURE if measure_color is None else measure_color
		self.barline_color = self.COLOR__ACOUSTIC_GUITAR_BARLINE if barline_color is None else barline_color

		# String count
		self.string_count = min( [len(self.string_widths), len(self.string_colors)] )

		# Drawing scale
		self.scale = 25

	def notes(self, x0_y0, *notes):

		# Position
		x0,y0 = x0_y0

		# Title dy
		dy = -6 * self.SIZE_FONT

		# Measure
		r = self.dwg.rect( (self.scale * x0, self.scale * (y0 - dy)), (self.scale * (self.MEASURE_WIDTH), self.scale * (self.MEASURE_HEIGHT)), fill=self.measure_color )
		self.dwg.add( r )

		# Strings
		for s in range(self.string_count):
			ys = y0 + (s+1) * self.MEASURE_HEIGHT / (self.string_count + 1)
			ls = self.dwg.line( (self.scale * x0, self.scale * (ys - dy)), (self.scale * x0 + self.scale * self.MEASURE_WIDTH, self.scale * (ys - dy)), stroke=self.string_colors[s], stroke_width=0.005 * self.scale * self.string_widths[s] )
			self.dwg.add( ls )

		# Bar lines
		bl1 = self.dwg.line( (self.scale * x0, self.scale * (y0 - dy)), (self.scale * x0, self.scale * (y0 - dy) + self.scale * self.MEASURE_HEIGHT), stroke=self.barline_color, stroke_width=0.005 * self.scale )
		self.dwg.add( bl1 )
		bl2 = self.dwg.line( (self.scale * x0 + self.scale * self.MEASURE_WIDTH, self.scale * (y0 - dy)), (self.scale * x0 + self.scale * self.MEASURE_WIDTH, self.scale * (y0 - dy) + self.scale * self.MEASURE_HEIGHT), stroke=self.barline_color, stroke_width=0.005 * self.scale )
		self.dwg.add( bl2 )

		# Notes
		for note in notes:
			# Coordinates top-left (xs0,ys0) and bottom-right (xs1,ys1)
			xs0 = self.scale * (x0 + self.MEASURE_WIDTH * note.start)
			ys0 = self.scale * ((y0 - dy) + note.string * self.MEASURE_HEIGHT / (self.string_count + 1) - self.MEASURE_HEIGHT / (self.string_count + 1) / 2 )
			wid = self.scale * self.MEASURE_WIDTH * (note.finish - note.start)
			hei = self.scale * (self.MEASURE_HEIGHT / (self.string_count + 1))

			# Actual note
			r = self.dwg.rect( (xs0,ys0), (wid,hei), fill = self.finger_colors[note.string - 1], rx=hei/2, ry=hei/2 )
			self.dwg.add( r )

			# Text
			t = self.dwg.text( note.name, insert=(xs0 + wid / 2 ,ys0 + hei / 2 + self.scale * self.SIZE_FONT / 2 ), fill='white', font_size=self.scale * self.SIZE_FONT, style="text-align:center;text-anchor:middle" )
			self.dwg.add( t )


	def notes_next(self, *notes):

		x,y = self._cnt % self.MEASURES_PER_LINE,self._cnt // self.MEASURES_PER_LINE

		xy = ( x * self.MEASURE_WIDTH, y * (self.MEASURE_HEIGHT + self.MEASURE_VERTICAL_GAP) )

		self.notes( xy, *notes )

		self._cnt += 1


	def header(self, x0_y0, message):

		# Position
		x0,y0 = x0_y0

		# Title dy
		dy = -6 * self.SIZE_FONT

		# Text
		t = self.dwg.text( message, insert=(self.scale * x0 ,self.scale * (y0 - dy) - 0.5 * self.scale * self.SIZE_FONT), fill='black', font_size=self.scale * self.SIZE_FONT )
		self.dwg.add( t )


	def header_next(self, message):

		x,y = self._cnt % self.MEASURES_PER_LINE,self._cnt // self.MEASURES_PER_LINE

		xy = ( x * self.MEASURE_WIDTH, y * (self.MEASURE_HEIGHT + self.MEASURE_VERTICAL_GAP) )

		self.header( xy, message )

	def verse_next(self):

		self._cnt = (self._cnt // self.MEASURES_PER_LINE + 1) * self.MEASURES_PER_LINE


	def set_title(self, title, subtitle=None):

		# Title dy
		dy = -6 * self.SIZE_FONT

		t = self.dwg.text( title, insert=(0 ,-4 * self.scale * self.SIZE_FONT - dy * self.scale), fill='black', font_size=2 * self.scale * self.SIZE_FONT )
		self.dwg.add( t )

		if subtitle is not None:
			t2 = self.dwg.text( title, insert=(0 ,-2 * self.scale * self.SIZE_FONT - dy * self.scale), fill='black', font_size=1.5 * self.scale * self.SIZE_FONT )
			self.dwg.add( t2 )

	def save(self):

		# Title dy
		dy = -6 * self.SIZE_FONT

		# Save
		self.dwg.save()

		# Resize to content
		wid = self.scale * self.MEASURES_PER_LINE * self.MEASURE_WIDTH
		hei = self.scale * ((self._cnt // self.MEASURES_PER_LINE - 1) * (self.MEASURE_HEIGHT + self.MEASURE_VERTICAL_GAP) - self.MEASURE_VERTICAL_GAP - dy)

		with open(self.dwg_file, 'r+') as f:
			data = f.read().replace('<svg baseProfile="full" height="100%" version="1.1" width="100%"', '<svg baseProfile="full" height="' + str(hei) + '" version="1.1" width="' + str(wid) + '"')

		with open(self.dwg_file, 'w') as f:
			f.write(data)

		# Export as pdf
		cairosvg.svg2pdf(url=self.dwg_file, write_to=self.dwg_file + str(".pdf"))

Note = namedtuple("Note", "string name finger start finish")
