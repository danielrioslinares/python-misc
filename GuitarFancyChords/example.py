
from GuitarFancyChords import *

note1 = Note(1, "1"  , 0, 0.25, 0.5)
note2 = Note(2, "3h5", 2, 0.50, 1.0)
note3 = Note(3, "1"  , 0, 0.25, 0.5)
note4 = Note(4, "3h5", 2, 0.50, 1.0)


table = GuitarMeasure()
table.set_title("Title", "Subtitle")

table.header_next( "[Verse 1]" )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.verse_next()

table.header_next( "[Verse 2]" )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.verse_next()

table.header_next( "[Verse 3]" )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )

table.header_next( "Slide here!" )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.notes_next( note1, note2, note3, note4 )
table.verse_next()

table.save()
