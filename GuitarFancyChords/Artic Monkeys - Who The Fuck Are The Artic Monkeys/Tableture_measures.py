
from GuitarFancyChords import *


turner_guita_lick_part01 = [
	# Rest (augmented crotchet)
	Note(5, "0" , 1, ( 1.5 * c         ) / 4, ( q ) / 4 ),
	Note(5, "2" , 3, ( 1.5 * c + q     ) / 4, ( q ) / 4 ),
	Note(5, "0" , 1, ( 1.5 * c + 2 * q ) / 4, ( c ) / 4 ),
	Note(5, "2" , 3, ( 2.5 * c + 2 * q ) / 4, ( c ) / 4 ),
]
turner_guita_lick_part02 = [
	Note(5, "2" , 3, ( -q              ) / 4, ( c       ) / 4 ),
	Note(5, "0" , 1, ( q               ) / 4, ( c       ) / 4 ),
	Note(6, "2" , 3, ( c + q           ) / 4, ( c       ) / 4 ),
	Note(5, "0" , 1, ( 2 * c + q       ) / 4, ( 1.5 * c ) / 4 ),
]
jamiec_guita_FSMinor_part01 = [
	# Rest (crotchet)
	Note(1, "5" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(2, "7" , 2, ( c               ) / 4, ( c ) / 4 ),
	Note(3, "6" , 3, ( c               ) / 4, ( c ) / 4 ),
]
jamiec_guita_FSMinor_part02 = [
	# Rest (minim)
	# Rest (quaver)
	Note(1, "5" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(2, "7" , 2, ( m + q           ) / 4, ( q ) / 4 ),
	Note(3, "6" , 3, ( m + q           ) / 4, ( q ) / 4 ),
	Note(1, "5" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(2, "7" , 2, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(3, "6" , 3, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(1, "5" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(2, "7" , 2, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(3, "6" , 3, ( m + 3 * q       ) / 4, ( q ) / 4 ),
]
jamiec_guita_FSMinor = jamiec_guita_FSMinor_part01 + jamiec_guita_FSMinor_part02
jamiec_guita_BMinor_part01 = [
	# Rest (crotchet)
	Note(1, "7" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(2, "7" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(3, "7" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(4, "9" , 2, ( c               ) / 4, ( c ) / 4 ),
]
jamiec_guita_BMinor_part02 = [
	# Rest (minim)
	# Rest (quaver)
	Note(1, "7" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(2, "7" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(3, "7" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(4, "9" , 2, ( m + q           ) / 4, ( q ) / 4 ),
	Note(1, "7" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(2, "7" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(3, "7" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(4, "9" , 2, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(1, "7" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(2, "7" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(3, "7" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(4, "9" , 2, ( m + 3 * q       ) / 4, ( q ) / 4 ),
]
jamiec_guita_BMinor = jamiec_guita_BMinor_part01 + jamiec_guita_BMinor_part02

turner_guita_verse01_part01 = [
	# Rest (quaver)
	Note(1, "0" , 0, ( q               ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( 2 * q           ) / 4, ( c ) / 4 ),
	Note(1, "5" , 1, ( 2 * q + c       ) / 4, ( q ) / 4 ),
	Note(1, "7" , 3, ( 3 * q + c       ) / 4, ( q ) / 4 ),
	# Rest (quaver)
	Note(1, "7" , 1, ( 5 * q + c       ) / 4, ( q ) / 4 ),
]
turner_guita_verse01_part02 = [
	Note(1, "9" , 3, ( 0               ) / 4, ( c       ) / 4 ),
	Note(1, "5" , 1, ( c               ) / 4, ( q       ) / 4 ),
	Note(1, "7" , 3, ( c + q           ) / 4, ( 1.5 * c ) / 4 ),
	# Rest (crotchet)
]
turner_guita_verse01_part03 = [
	# Rest (quaver)
	Note(1, "0" , 0, ( q               ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( 2 * q           ) / 4, ( c ) / 4 ),
	Note(1, "5" , 1, ( 2 * q + c       ) / 4, ( q ) / 4 ),
	Note(1, "7" , 3, ( 3 * q + c       ) / 4, ( q ) / 4 ),
	# Rest (quaver)
	Note(1, "5" , 1, ( 5 * q + c       ) / 4, ( q ) / 4 ),
]
turner_guita_verse01_part04 = [
	Note(2, "2" , 1, ( 0               ) / 4, ( 1.5 * c ) / 4 ),
	Note(3, "2" , 1, ( 1.5 * c         ) / 4, ( m       ) / 4 ),
	# Rest (quaver)
]
turner_guita_verse01_part05 = [
	Note(1, "0" , 0, ( 0               ) / 4, ( 1.5 * c ) / 4 ),
	Note(2, "3" , 1, ( 1.5 * c         ) / 4, ( 1.5 * c ) / 4 ),
	Note(1, "5" , 1, ( 3 * c           ) / 4, ( c       ) / 4 ),
]
turner_guita_verse01_part06 = [
	Note(1, "2" , 1, ( 0               ) / 4, ( 1.5 * c ) / 4 ),
]
turner_guita_refrain_part01 = [
	Note(2, "0" , 0, ( 0               ) / 4, ( 1.5 * m ) / 4 ),
	Note(2, "2" , 1, ( 1.5 * m         ) / 4, ( c       ) / 4 ),
]
turner_guita_refrain_part02 = [
	Note(3, "2" , 1, ( 0               ) / 4, ( m       ) / 4 ),
	Note(4, "4" , 3, ( m               ) / 4, ( m       ) / 4 ),
]
turner_guita_refrain_part03 = turner_guita_refrain_part01
turner_guita_refrain_part04 = turner_guita_refrain_part02
turner_guita_refrain_part05 = turner_guita_refrain_part01
turner_guita_refrain_part06 = turner_guita_refrain_part02
turner_guita_refrain_part07 = turner_guita_refrain_part01
turner_guita_refrain_part08 = [
	# Rest (quaver)
	Note(4, "4" , 1, ( q               ) / 4, ( c       ) / 4 ),
	Note(4, "4" , 1, ( c + q           ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
]
turner_guita_refrain_part09 = [
	Note(4, "4" , 1, ( q               ) / 4, ( c       ) / 4 ),
	Note(4, "4" , 1, ( c + q           ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 1, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 3, ( q               ) / 4, ( c       ) / 4 ),
	Note(1, "2" , 3, ( c + q           ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 3, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 3, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 3, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 3, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
]
turner_guita_refrain_part10 = [
	Note(1, "14", 1, ( q               ) / 4, ( c       ) / 4 ),
	Note(1, "14", 1, ( c + q           ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
	#Note(1, "2" , 3, ( q               ) / 4, ( c       ) / 4 ),
	#Note(1, "2" , 3, ( c + q           ) / 4, ( q       ) / 4 ),
	#Note(1, "2" , 3, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	#Note(1, "2" , 3, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	#Note(1, "2" , 3, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	#Note(1, "2" , 3, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
]
turner_guita_refrain_part11 = [
	Note(1, "14", 1, ( 0               ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( q               ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c               ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + q           ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	Note(1, "14", 1, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( 0               ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( q               ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( c               ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( c + q           ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	#Note(3, "11", 3, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
]

turner_guita_lalala_lick_part01 = turner_guita_lick_part01
turner_guita_lalala_lick_part02 = turner_guita_lick_part02
turner_guita_lalala_lick_part03 = turner_guita_lick_part01
turner_guita_lalala_lick_part04 = [
	Note(5, "2" , 3, ( -q              ) / 4, ( c       ) / 4 ),
	Note(5, "0" , 0, ( q               ) / 4, ( c       ) / 4 ),
	Note(6, "2" , 3, ( c + q           ) / 4, ( 2.5 * c ) / 4 ),

]
turner_guita_lalala_lick_part05 = [
	Note(6, "5" , 4, ( 0               ) / 4, ( 1.5 * c ) / 4 ),
	Note(6, "0" , 0, ( 1.5 * c         ) / 4, ( m       ) / 4 ),

]
turner_guita_lalala_lick_part06 = [
	Note(6, "2" , 1, ( 0               ) / 4, ( 1.5 * c ) / 4 ),
	Note(6, "0" , 0, ( 1.5 * c         ) / 4, ( 1.5 * c ) / 4 ),
	Note(5, "2" , 1, ( 3 * c           ) / 4, ( c       ) / 4 ),
]
turner_guita_lalala_lick_part07 = [
	Note(6, "4" , 4, ( 0               ) / 4, ( 2 * w   ) / 4 ),
]
turner_guita_lalala_lick_part08 = [
	Note(6, "4" , 4, ( -w              ) / 4, ( 2 * w   ) / 4 ),
]
turner_guita_verse03_part01 = [
	Note(6, "4" , 4, ( -w              ) / 4, ( 2 * w   ) / 4 ),
]
turner_guita_verse03_part01 = []
turner_guita_verse03_part02 = [
	# Rest (quaver)
	Note(3, "11", 1, ( 0 * c + 0 * q   ) / 4, ( q ) / 4 ),
	Note(3, "13", 3, ( 0 * c + 1 * q   ) / 4, ( c ) / 4 ),
	Note(2, "12", 2, ( 1 * c + 1 * q   ) / 4, ( q ) / 4 ),
	Note(2, "14", 4, ( 1 * c + 2 * q   ) / 4, ( q ) / 4 ),
	# Rest (quaver)
	Note(2, "14", 1, ( 1 * c + 4 * q   ) / 4, ( q ) / 4 ),
]
turner_guita_verse03_part03 = [
	# Rest (quaver)
	Note(2, "16", 3, ( 0 * c + 0 * q   ) / 4, ( c       ) / 4 ),
	Note(2, "12", 1, ( 1 * c + 0 * q   ) / 4, ( q       ) / 4 ),
	Note(2, "14", 3, ( 1 * c + 1 * q   ) / 4, ( 1.5 * c ) / 4 ),
	# Rest (crotchet)
]
turner_guita_verse03_part04 = [
	# Rest (quaver)
	Note(3, "11", 1, ( 0 * c + 0 * q   ) / 4, ( q ) / 4 ),
	Note(3, "13", 3, ( 0 * c + 1 * q   ) / 4, ( c ) / 4 ),
	Note(2, "12", 1, ( 1 * c + 1 * q   ) / 4, ( q ) / 4 ),
	Note(2, "14", 3, ( 1 * c + 2 * q   ) / 4, ( q ) / 4 ),
	# Rest (quaver)
	Note(2, "12", 1, ( 1 * c + 4 * q   ) / 4, ( q ) / 4 ),
]
turner_guita_verse03_part05 = [
	Note(3, "13", 2, ( 0 * c + 0 * q   ) / 4, ( 1.5 * c ) / 4 ),
	Note(4, "14", 3, ( 1.5 * c         ) / 4, ( m       ) / 4 ),
	# Rest (quaver)
]
turner_guita_verse03_part06 = [
	Note(3, "11", 3, ( 0 * c + 0 * q   ) / 4, ( 1.5 * c ) / 4 ),
	Note(3, "9" , 1, ( 1.5 * c + 0 * q ) / 4, ( 1.5 * c ) / 4 ),
	Note(2, "12", 4, ( 3 * c + 0 * q   ) / 4, ( c       ) / 4 ),
	# Rest (quaver)
]
turner_guita_verse03_part07 = [
	# Rest (quaver)
	Note(3, "13", 3, ( 0 * c + 1 * q   ) / 4, ( m + q   ) / 4 ),
]
turner_guita_itsnotyou1_part01 = [
	Note(4, "9" , 1, ( 0               ) / 4, ( 1.5 * w ) / 4 ),
]
turner_guita_itsnotyou1_part02 = [
	Note(4, "9" , 3, ( -w              ) / 4, ( 1.5 * w ) / 4 ),
	Note(6, "7" , 1, ( m               ) / 4, ( m       ) / 4 ),
]
turner_guita_itsnotyou1_part03 = [
	Note(5, "8" , 2, ( 0               ) / 4, ( 2 * w   ) / 4 ),
]
turner_guita_itsnotyou1_part04 = [
	Note(5, "8" , 2, ( -w              ) / 4, ( 2 * w   ) / 4 ),
]
turner_guita_itsnotyou2_part01 = [
	Note(4, "9" , 1, ( 0               ) / 4, ( 1.5 * w ) / 4 ),
]
turner_guita_itsnotyou2_part02 = [
	Note(4, "9" , 3, ( -w              ) / 4, ( 1.5 * w ) / 4 ),
	Note(5, "8" , 2, ( m               ) / 4, ( m       ) / 4 ),
]
turner_guita_itsnotyou2_part03 = [
	Note(6, "7" , 1, ( 0               ) / 4, ( 2 * w   ) / 4 ),
]
turner_guita_itsnotyou2_part04 = [
	Note(6, "7" , 1, ( -w              ) / 4, ( 2 * w   ) / 4 ),
]
turner_guita_turinturu01 = [
	Note(6, "7" , 1, ( 0               ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "9" , 3, ( 1.5 * q         ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "7" , 3, ( 3 * q           ) / 4, ( q       ) / 4 ),
	Note(5, "8" , 3, ( 4 * q           ) / 4, ( m       ) / 4 ),
]
turner_guita_turinturu02 = [
	Note(6, "7" , 1, ( 0               ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "9" , 3, ( 1.5 * q         ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "7" , 1, ( 3 * q           ) / 4, ( q       ) / 4 ),
	Note(5, "8" , 2, ( 4 * q           ) / 4, ( q       ) / 4 ),
	Note(5, "7" , 3, ( 5 * q           ) / 4, ( s       ) / 4 ),
	Note(5, "5" , 1, ( 5 * q + s       ) / 4, ( s       ) / 4 ),
	Note(5, "7" , 3, ( 5 * q + 2 * s   ) / 4, ( q       ) / 4 ),
]
turner_guita_outro_part01 = [
	Note(5, "2" , 1, ( 0               ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "0" , 0, ( 1.5 * q         ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "4" , 3, ( 3 * q           ) / 4, ( q + m   ) / 4 ),
]
turner_guita_outro_part02 = [
	Note(4, "0" , 0, ( 0               ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "2" , 1, ( 1.5 * q         ) / 4, ( 1.5 * q ) / 4 ),
	Note(4, "2" , 1, ( 3 * q           ) / 4, ( c       ) / 4 ),
	Note(4, "0" , 0, ( 3 * q + c       ) / 4, ( 1.5 * c ) / 4 ),
]


turner_vocal_verse01_part01 = [
	# Rest (quaver)
	Note(4, "4" , 3, ( q               ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 2 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 3 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 4 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 5 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 6 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 7 * q           ) / 4, ( c ) / 4 ),
]
turner_vocal_verse01_part02 = [
	# Rest (quaver)
	Note(3, "2" , 1, ( -q              ) / 4, ( c ) / 4 ),
	# Rest (augmented crotchet)
	Note(4, "4" , 3, ( 2 * c + q       ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( 3 * c + q       ) / 4, ( q ) / 4 ),
]
turner_vocal_verse01_part03 = [
	Note(3, "4" , 3, ( 0 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 1 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 2 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 3 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 4 * q           ) / 4, ( c ) / 4 ),
	Note(4, "4" , 1, ( 4 * q + c       ) / 4, ( q ) / 4 ),
	Note(4, "4" , 1, ( 5 * q + c       ) / 4, ( q ) / 4 ),
]
turner_vocal_verse01_part04 = [
	Note(3, "2" , 1, ( 0 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 1 * q           ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( 1 * q + 1 * c   ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( 1 * q + 2 * c   ) / 4, ( q ) / 4 ),
	Note(4, "4" , 3, ( 2 * q + 2 * c   ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 3 * q + 2 * c   ) / 4, ( c ) / 4 ),
]
turner_vocal_verse01_part05 = [
	Note(3, "2" , 1, ( -q              ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( q               ) / 4, ( c ) / 4 ),
	Note(4, "2" , 1, ( q + c           ) / 4, ( q ) / 4 ),
	Note(4, "0" , 0, ( 2 * q + c       ) / 4, ( c ) / 4 ),
	Note(4, "2" , 1, ( 3 * q + 2 * c   ) / 4, ( q ) / 4 ),
]
turner_vocal_verse01_part06 = [
	Note(4, "4/", 3, ( 0               ) / 4, ( c       ) / 4 ),
	Note(1, "2" , 1, ( 1 * c           ) / 4, ( q       ) / 4 ),
	Note(1, "0" , 0, ( 1 * c + q       ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 1, ( 1 * c + 2 * q   ) / 4, ( c       ) / 4 ),
	Note(1, "0" , 0, ( 2 * c + 2 * q   ) / 4, ( c + q   ) / 4 ),
]
turner_vocal_verse01_part07 = [
	Note(1, "0" , 0, ( -c              ) / 4, ( c + q   ) / 4 ),
	Note(1, "5" , 1, ( q               ) / 4, ( c       ) / 4 ),
	Note(2, "7" , 3, ( c + q           ) / 4, ( c       ) / 4 ),
	Note(2, "s0", 3, ( 2 * c + q       ) / 4, ( 1.5 * c ) / 4 ),
]

turner_vocal_verse02_part01 = [
	# Rest (quaver)
	Note(4, "4" , 3, ( q               ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 2 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 3 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 4 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 5 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 6 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 7 * q           ) / 4, ( q ) / 4 ),
]
turner_vocal_verse02_part02 = [
	Note(4, "4" , 3, ( 0               ) / 4, ( m ) / 4 ),
]
turner_vocal_verse02_part03 = [
	# Rest (quaver)
	Note(4, "4" , 3, ( q               ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 2 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 3 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 4 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 5 * q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( 6 * q           ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( 7 * q           ) / 4, ( c ) / 4 ),
]
turner_vocal_verse02_part04 = [
	Note(3, "2" , 1, ( -q              ) / 4, ( c       ) / 4 ),
	Note(4, "4" , 3, ( q               ) / 4, ( 1.5 * c ) / 4 ),
	# Rest (quaver)
	Note(4, "4" , 3, ( 1.5 * c + 2 * q ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 3, ( 1.5 * c + 3 * q ) / 4, ( q       ) / 4 ),
	Note(3, "2" , 1, ( 1.5 * c + 4 * q ) / 4, ( c       ) / 4 ),
]
turner_vocal_verse02_part05 = [
	Note(3, "2" , 1, ( -q              ) / 4, ( c       ) / 4 ),
	Note(4, "4" , 3, ( q               ) / 4, ( c       ) / 4 ),
	Note(4, "4" , 3, ( c + q           ) / 4, ( 1.5 * c ) / 4 ),
]
turner_vocal_verse02_part06 = [
	# Rest quaver
	Note(4, "4" , 3, ( q               ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 1, ( 2 * q           ) / 4, ( q       ) / 4 ),
	Note(1, "0" , 0, ( 3 * q           ) / 4, ( q       ) / 4 ),
	Note(1, "2" , 1, ( 4 * q           ) / 4, ( c       ) / 4 ),
	Note(1, "0" , 1, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	Note(2, "3" , 2, ( c + 5 * q       ) / 4, ( c       ) / 4 ),
]
turner_vocal_verse02_part07 = [
	# Rest quaver
	Note(2, "3" , 2, ( -q              ) / 4, ( c       ) / 4 ),
	Note(2, "3" , 2, ( q               ) / 4, ( c       ) / 4 ),
	Note(2, "s0", 2, ( q + c           ) / 4, ( m       ) / 4 ),
]
turner_vocal_refrain_part01 = [
	# Rest (crotchet)
	Note(3, "4" , 3, ( c               ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( c + q           ) / 4, ( q ) / 4 ),
	Note(3, "4" , 3, ( c + 2 * q       ) / 4, ( c ) / 4 ),
	Note(2, "2" , 1, ( 2 * c + 2 * q   ) / 4, ( c ) / 4 ),
]
turner_vocal_refrain_part02 = [
	Note(3, "2" , 1, ( 0               ) / 4, ( c ) / 4 ),
	Note(3, "2" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( 2 * c           ) / 4, ( m ) / 4 ),
]
turner_vocal_refrain_part03 = turner_vocal_refrain_part01
turner_vocal_refrain_part04 = [
	Note(3, "2" , 1, ( 0               ) / 4, ( m ) / 4 ),
	# Rest (augmented crotchet)
	Note(4, "4" , 3, ( m + 1.5 * c     ) / 4, ( q ) / 4 ),
]
turner_vocal_refrain_part05 = [
	Note(3, "4" , 3, ( 0               ) / 4, ( c ) / 4 ),
	Note(3, "4" , 3, ( c               ) / 4, ( c ) / 4 ),
	Note(3, "4" , 3, ( 2 * c           ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( 3 * c           ) / 4, ( c ) / 4 ),
]
turner_vocal_refrain_part06 = [
	Note(3, "2" , 1, ( 0               ) / 4, ( q ) / 4 ),
	Note(3, "2" , 1, ( q               ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( c + q           ) / 4, ( c ) / 4 ),
	Note(4, "4" , 3, ( 2 * c + q       ) / 4, ( q ) / 4 ),
	Note(4, "4" , 3, ( 2 * c + 2 * q   ) / 4, ( c ) / 4 ),
]
turner_vocal_refrain_part07 = [
	Note(1, "0" , 0, ( 0                 ) / 4, ( q ) / 4 ),
	Note(1, "0" , 0, ( q                 ) / 4, ( s ) / 4 ),
	Note(1, "0" , 0, ( q + s             ) / 4, ( s ) / 4 ),
	Note(1, "0" , 0, ( q + 2 * s         ) / 4, ( c ) / 4 ),
	Note(2, "3" , 3, ( c + q + 2 * s     ) / 4, ( q ) / 4 ),
	Note(2, "3" , 3, ( c + 2 * q + 2 * s ) / 4, ( q ) / 4 ),
	Note(2, "2" , 1, ( c + 3 * q + 2 * s ) / 4, ( q ) / 4 ),
	Note(2, "2" , 1, ( c + 4 * q + 2 * s ) / 4, ( q ) / 4 ),
]
turner_vocal_refrain_part08 = [
	Note(2, "0" , 0, ( 0               ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( q               ) / 4, ( c ) / 4 ),
	Note(1, "2" , 1, ( c + q           ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 2 * q       ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 3 * q       ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 4 * q       ) / 4, ( q ) / 4 ),
	Note(2, "3" , 2, ( c + 5 * q       ) / 4, ( q ) / 4 ),
]
turner_vocal_refrain_part09 = turner_vocal_refrain_part08
turner_vocal_refrain_part10 = [
	Note(2, "0" , 0, ( 0               ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( q               ) / 4, ( c ) / 4 ),
	Note(1, "2" , 1, ( c + q           ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 2 * q       ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 3 * q       ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 4 * q       ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 5 * q       ) / 4, ( q ) / 4 ),
]
turner_vocal_refrain_part11 = [
	Note(1, "2" , 1, ( 0               ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( q               ) / 4, ( c ) / 4 ),
	Note(1, "2" , 1, ( c + q           ) / 4, ( q ) / 4 ),
	Note(1, "2" , 1, ( c + 2 * q       ) / 4, ( c ) / 4 ),
	Note(1, "2" , 1, ( 2 * c + 2 * q   ) / 4, ( c ) / 4 ),
]
turner_vocal_lalala_part01 = [
	# Rest (crotchet)
	Note(2, "2" , 1, ( 2 * q           ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 3 * q           ) / 4, ( q ) / 4 ),
	Note(2, "2" , 1, ( 4 * q           ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 5 * q           ) / 4, ( q ) / 4 ),
	Note(3, "1" , 1, ( 6 * q           ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 7 * q           ) / 4, ( c ) / 4 ),
]
turner_vocal_lalala_part02 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( c ) / 4 ),
	Note(3, "1" , 1, ( q               ) / 4, ( c ) / 4 ),
]
turner_vocal_verse03_part01 = turner_vocal_lalala_part01
turner_vocal_verse03_part02 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( c ) / 4 ),
	Note(3, "1" , 1, ( q               ) / 4, ( c ) / 4 ),
	# Rest (augmented crotchet)
	Note(3, "1" , 1, ( 4 - q           ) / 4, ( q ) / 4 ),
]
turner_vocal_verse03_part03 = [
	# Rest (crotchet)
	Note(2, "2" , 1, ( 0 * q           ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 1 * q           ) / 4, ( q ) / 4 ),
	Note(2, "2" , 1, ( 2 * q           ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 3 * q           ) / 4, ( q ) / 4 ),
	Note(2, "2" , 1, ( 4 * q           ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 5 * q           ) / 4, ( q ) / 4 ),
	Note(3, "1" , 1, ( 6 * q           ) / 4, ( c ) / 4 ),
]
turner_vocal_verse03_part04 = [
	# Rest (crotchet)
	Note(2, "0" , 0, ( 0               ) / 4, ( q ) / 4 ),
	Note(2, "2" , 2, ( q               ) / 4, ( c ) / 4 ),
	Note(3, "1" , 1, ( c + q           ) / 4, ( c ) / 4 ),
	Note(3, "1" , 1, ( 2 * c + q       ) / 4, ( q ) / 4 ),
	Note(3, "1" , 1, ( 2 * c + 2 * q   ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 2 * c + 3 * q   ) / 4, ( c ) / 4 ),
]
turner_vocal_verse03_part05 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( c ) / 4 ),
	Note(3, "1" , 1, ( q               ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( q + q           ) / 4, ( c ) / 4 ),
	Note(3, "1" , 1, ( 1 * c + 2 * q   ) / 4, ( q ) / 4 ),
	Note(3, "1" , 1, ( 1 * c + 3 * q   ) / 4, ( q ) / 4 ),
	Note(3, "1" , 1, ( 1 * c + 4 * q   ) / 4, ( q ) / 4 ),
	Note(2, "0" , 0, ( 1 * c + 5 * q   ) / 4, ( q ) / 4 ),
]
turner_vocal_verse03_part06 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( c       ) / 4 ),
	Note(3, "1" , 1, ( q               ) / 4, ( c       ) / 4 ),
	Note(3, "1" , 1, ( c + q           ) / 4, ( q       ) / 4 ),
	Note(3, "1" , 1, ( c + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 3, ( c + 3 * q       ) / 4, ( q       ) / 4 ),
	Note(4, "2" , 1, ( c + 4 * q       ) / 4, ( q       ) / 4 ),
	Note(2, "0" , 0, ( c + 5 * q       ) / 4, ( c       ) / 4 ),
]
turner_vocal_verse03_part07 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( c       ) / 4 ),
	Note(3, "1" , 1, ( q               ) / 4, ( 1.5 * c ) / 4 ),
]
turner_vocal_itsnotyou_part01 = [
	Note(1, "2" , 1, ( 0               ) / 4, ( c       ) / 4 ),
	Note(1, "2" , 1, ( c               ) / 4, ( c       ) / 4 ),
	Note(1, "2" , 1, ( 2 * c           ) / 4, ( c       ) / 4 ),
	Note(1, "2" , 1, ( 3 * c           ) / 4, ( c       ) / 4 ),
]
turner_vocal_itsnotyou_part02 = [
	Note(1, "2" , 0, ( 0               ) / 4, ( m       ) / 4 ),
	Note(2, "0" , 0, ( m               ) / 4, ( q       ) / 4 ),
	Note(3, "2" , 1, ( m + q           ) / 4, ( c       ) / 4 ),
	Note(2, "0" , 0, ( m + q + c       ) / 4, ( q + m   ) / 4 ),
]
turner_vocal_itsnotyou_part03 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( q + m   ) / 4 ),
	Note(2, "0" , 0, ( m               ) / 4, ( q       ) / 4 ),
	Note(3, "2" , 1, ( m + q           ) / 4, ( c       ) / 4 ),
	Note(2, "0" , 0, ( m + q + c       ) / 4, ( c       ) / 4 ),
]
turner_vocal_itsnotyou_part04 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( c       ) / 4 ),
	Note(3, "2" , 1, ( q               ) / 4, ( c       ) / 4 ),
	Note(2, "0" , 0, ( c + q           ) / 4, ( c       ) / 4 ),
	Note(2, "3" , 2, ( 2 * c + q       ) / 4, ( c       ) / 4 ),
	Note(2, "0" , 0, ( 3 * c + q       ) / 4, ( q + m   ) / 4 ),
]
turner_vocal_itsnotyou_part05 = turner_vocal_itsnotyou_part03
turner_vocal_itsnotyou_part06 = turner_vocal_itsnotyou_part04
turner_vocal_itsnotyou_part07 = [
	Note(2, "0" , 0, ( -q              ) / 4, ( q + m   ) / 4 ),
]
turner_vocal_bringonthebacklash_part01 = [
	Note(2, "0" , 0, ( 4 - q           ) / 4, ( q       ) / 4 ),
]
turner_vocal_bringonthebacklash_part02 = [
	Note(2, "s5", 1, ( 0              ) / 4, ( 1.5 * m ) / 4 ),
	# Rest (crotchet + quaver)
	Note(3, "7" , 1, ( 1.5 * m         ) / 4, ( 1.5 * q     ) / 4 ),
	Note(3, "s0", 1, ( 1.5 * m + 1.5 * q ) / 4, ( s         ) / 4 ),
]






jamiec_guita_refrain_part01 = [
	Note(1, "7" , 2, ( 0               ) / 4, ( 1.5 * m ) / 4 ),
	Note(2, "8" , 3, ( 0               ) / 4, ( 1.5 * m ) / 4 ),
	Note(3, "7" , 1, ( 0               ) / 4, ( 1.5 * m ) / 4 ),
	Note(1, "7" , 2, ( 1.5 * m         ) / 4, ( c       ) / 4 ),
	Note(2, "8" , 3, ( 1.5 * m         ) / 4, ( c       ) / 4 ),
	Note(3, "7" , 1, ( 1.5 * m         ) / 4, ( c       ) / 4 ),
]
jamiec_guita_refrain_part02 = [
	Note(1, "5" , 1, ( 0               ) / 4, ( m ) / 4 ),
	Note(2, "7" , 2, ( 0               ) / 4, ( m ) / 4 ),
	Note(3, "6" , 3, ( 0               ) / 4, ( m ) / 4 ),
	Note(1, "9" , 2, ( m               ) / 4, ( m ) / 4 ),
	Note(2, "10", 3, ( m               ) / 4, ( m ) / 4 ),
	Note(3, "9" , 1, ( m               ) / 4, ( m ) / 4 ),
]
jamiec_guita_C = [
	# Rest (crotchet)
	Note(1, "7" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(2, "8" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(3, "7" , 1, ( c               ) / 4, ( c ) / 4 ),
	# Rest (quaver)
	Note(1, "7" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(2, "8" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(3, "7" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(1, "7" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(2, "8" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(3, "7" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(1, "7" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(2, "8" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(3, "7" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
]
jamiec_guita_refrain_part03 = jamiec_guita_C
jamiec_guita_refrain_part04 = jamiec_guita_refrain_part02
jamiec_guita_refrain_part05 = jamiec_guita_C
jamiec_guita_refrain_part06 = jamiec_guita_refrain_part03
jamiec_guita_refrain_part07 = jamiec_guita_C

jamiec_guita_jamiec_solo_part01 = [
	Note(5, "2" , 1, ( 0               ) / 4, ( 1.5 * c ) / 4 ),
	Note(5, "2" , 1, ( 1.5 * c         ) / 4, ( q       ) / 4 ),
	Note(4, "4" , 3, ( 1.5 * c + q     ) / 4, ( c       ) / 4 ),
	Note(4, "2" , 1, ( 2.5 * c + q     ) / 4, ( c       ) / 4 ),
]
jamiec_guita_jamiec_solo_part02 = [
	Note(4, "0" , 0, ( 0               ) / 4, ( w       ) / 4 ),
]
jamiec_guita_jamiec_solo_part03 = jamiec_guita_jamiec_solo_part01
jamiec_guita_jamiec_solo_part04 = [
	Note(4, "0" , 0, ( 0               ) / 4, ( m + q   ) / 4 ),
	Note(5, "0" , 0, ( m + q           ) / 4, ( q       ) / 4 ),
	Note(5, "2" , 1, ( m + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(5, "0" , 0, ( m + 3 * q       ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part05 = [
	Note(5, "2" , 1, ( 0               ) / 4, ( 1.5 * c ) / 4 ),
	Note(5, "0" , 0, ( 1.5 * c         ) / 4, ( q       ) / 4 ),
	Note(5, "2" , 1, ( 1.5 * c + q     ) / 4, ( 1.5 * c ) / 4 ),
	Note(5, "0" , 0, ( 3 * c + q       ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part06 = [
	Note(5, "2" , 1, ( 0               ) / 4, ( q       ) / 4 ),
	Note(5, "0" , 0, ( q               ) / 4, ( q       ) / 4 ),
	Note(6, "2" , 1, ( 2 * q           ) / 4, ( 1.5 * c ) / 4 ),
	Note(6, "2" , 1, ( 1.5 * c + 2 * q ) / 4, ( q       ) / 4 ),
	Note(6, "2" , 1, ( 1.5 * c + 3 * q ) / 4, ( q       ) / 4 ),
	Note(5, "0" , 0, ( 1.5 * c + 4 * q ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part07 = [
	Note(5, "2" , 1, ( 0               ) / 4, ( m + q   ) / 4 ),
	Note(5, "2" , 1, ( m + 1 * q       ) / 4, ( q       ) / 4 ),
	Note(5, "2" , 1, ( m + 2 * q       ) / 4, ( q       ) / 4 ),
	Note(5, "s5", 1, ( m + 3 * q       ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part08 = [
	Note(5, "5" , 1, ( 0               ) / 4, ( q       ) / 4 ),
	Note(5, "s7", 3, ( 1 * q           ) / 4, ( q       ) / 4 ),
	Note(5, "7" , 3, ( 2 * q           ) / 4, ( q       ) / 4 ),
	Note(5, "s9", 3, ( 3 * q           ) / 4, ( q       ) / 4 ),
	Note(5, "9" , 3, ( 4 * q           ) / 4, ( c + q   ) / 4 ),
	Note(4, "7" , 3, ( c + 5 * q       ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part09 = [
	Note(4, "9" , 3, ( 0               ) / 4, ( c       ) / 4 ),
	Note(4, "7" , 1, ( c               ) / 4, ( c       ) / 4 ),
	Note(5, "9" , 3, ( 2 * c           ) / 4, ( c       ) / 4 ),
	Note(5, "7" , 1, ( 3 * c           ) / 4, ( c       ) / 4 ),
]
jamiec_guita_jamiec_solo_part10 = [
	Note(5, "5" , 1, ( 0               ) / 4, ( 2/3 * c ) / 4 ),
	Note(5, "7" , 3, ( 1/3 * 2 * c     ) / 4, ( 2/3 * c ) / 4 ),
	Note(5, "9" , 3, ( 2/3 * 2 * c     ) / 4, ( 2/3 * c ) / 4 ),
	Note(5, "7" , 1, ( 2 * c           ) / 4, ( m       ) / 4 ),
]
jamiec_guita_jamiec_solo_part11 = [
	Note(3, "9" , 3, ( 0               ) / 4, ( c       ) / 4 ),
	Note(3, "7" , 1, ( c               ) / 4, ( c       ) / 4 ),
	Note(4, "9" , 3, ( 2 * c           ) / 4, ( c       ) / 4 ),
	Note(4, "7" , 1, ( 3 * c           ) / 4, ( c       ) / 4 ),
]
jamiec_guita_jamiec_solo_part12 = [
	Note(5, "7" , 3, ( 0               ) / 4, ( 1.5 * q ) / 4 ),
	Note(5, "7" , 3, ( 1.5 * q         ) / 4, ( s       ) / 4 ),
	Note(5, "s9", 3, ( 1.5 * q + s     ) / 4, ( q       ) / 4 ),
	Note(5, "7" , 3, ( 2.5 * q + s     ) / 4, ( q       ) / 4 ),
	Note(5, "5" , 1, ( 3.5 * q + s     ) / 4, ( m       ) / 4 ),
]
jamiec_guita_jamiec_solo_part13 = [
	Note(5, "5" , 1, ( 0               ) / 4, ( s       ) / 4 ),
	Note(5, "s7", 1, ( s               ) / 4, ( 1.5 * q ) / 4 ),
	Note(5, "7" , 1, ( 1.5 * q + s     ) / 4, ( q       ) / 4 ),
	Note(5, "5" , 1, ( 2.5 * q + s     ) / 4, ( q       ) / 4 ),
	Note(5, "7" , 3, ( 3.5 * q + s     ) / 4, ( c       ) / 4 ),
	Note(5, "7" , 3, ( 3.5 * q + s + c ) / 4, ( q       ) / 4 ),
	Note(5, "5" , 1, ( 4.5 * q + s + c ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part14 = [
	Note(5, "7" , 3, ( 0               ) / 4, ( q       ) / 4 ),
	Note(5, "5" , 1, ( q               ) / 4, ( m       ) / 4 ),
	Note(5, "0" , 0, ( q + m           ) / 4, ( q       ) / 4 ),
	Note(5, "2" , 1, ( 2 * q + m       ) / 4, ( q       ) / 4 ),
	Note(5, "0" , 0, ( 3 * q + m       ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part15 = [
	Note(5, "2" , 1, ( 0               ) / 4, ( c       ) / 4 ),
	Note(5, "2" , 1, ( c               ) / 4, ( q       ) / 4 ),
	Note(5, "0" , 0, ( c + q           ) / 4, ( q       ) / 4 ),
	Note(5, "2" , 1, ( c + 2 * q       ) / 4, ( c       ) / 4 ),
	Note(5, "2" , 1, ( 2 * c + 2 * q   ) / 4, ( q       ) / 4 ),
	Note(5, "0" , 0, ( 2 * c + 3 * q   ) / 4, ( q       ) / 4 ),
]
jamiec_guita_jamiec_solo_part16 = [
	Note(6, "2" , 1, ( 0               ) / 4, ( q       ) / 4 ),
	*jamiec_guita_FSMinor_part02
]

jamiec_guita_C2 = [
	# Rest (crotchet)
	Note(1, "7" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(2, "9" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(3, "8" , 1, ( c               ) / 4, ( c ) / 4 ),
	# Rest (quaver)
	Note(1, "7" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(2, "9" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(3, "8" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(1, "7" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(2, "9" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(3, "8" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(1, "7" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(2, "9" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(3, "8" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
]
jamiec_guita_C3 = [
	# Rest (crotchet)
	Note(1, "9" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(2, "9" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(3, "9" , 1, ( c               ) / 4, ( c ) / 4 ),
	Note(4, "11", 1, ( c               ) / 4, ( c ) / 4 ),
	# Rest (quaver)
	Note(1, "9" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(2, "9" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(3, "9" , 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(4, "11", 1, ( m + q           ) / 4, ( q ) / 4 ),
	Note(1, "9" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(2, "9" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(3, "9" , 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(4, "11", 1, ( m + 2 * q       ) / 4, ( q ) / 4 ),
	Note(1, "9" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(2, "9" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(3, "9" , 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
	Note(4, "11", 1, ( m + 3 * q       ) / 4, ( q ) / 4 ),
]
jamiec_guita_verse03_ending_part01 = [
	# Rest (crotchet)
	Note(1, "9" , 1, ( q               ) / 4, ( q + 1.5 * m ) / 4 ),
	Note(2, "9" , 1, ( q               ) / 4, ( q + 1.5 * m ) / 4 ),
	Note(3, "9" , 1, ( q               ) / 4, ( q + 1.5 * m ) / 4 ),
	Note(4, "11", 1, ( q               ) / 4, ( q + 1.5 * m ) / 4 ),
]
jamiec_guita_verse03_ending_part02 = [
	# Rest (crotchet)
	Note(1, "9" , 1, ( 0               ) / 4, ( m ) / 4 ),
	Note(2, "9" , 1, ( 0               ) / 4, ( m ) / 4 ),
	Note(3, "9" , 1, ( 0               ) / 4, ( m ) / 4 ),
	Note(4, "11", 1, ( 0               ) / 4, ( m ) / 4 ),
	Note(1, "9" , 1, ( m               ) / 4, ( m ) / 4 ),
	Note(2, "9" , 1, ( m               ) / 4, ( m ) / 4 ),
	Note(3, "9" , 1, ( m               ) / 4, ( m ) / 4 ),
	Note(4, "11", 1, ( m               ) / 4, ( m ) / 4 ),
]

#
