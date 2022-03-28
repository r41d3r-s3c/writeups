# Wolvsec CTF 2022 - Sick Beat Bro

Writeup by: r41d3r

Playing with: idek

## Problem

Author: christiann

I don't think my friend understands MIDI format...

## Solution

Tricky puzzle.  We were given a midi file with the description that implies it wasn't created correctly.  Trying to open the file gives an error that it is not in the correct format. 

We tried for hours to correct the formatting.  In the process, the MIDI Specifications data and the MIDO library from python helped us out.  In the end, we decided to stop trying to correct the file and create a new one based on the notes in the original file since all corrections attempted wouldn't fix the corrupted status.

First, I pulled the actual bits that looked like notes out of the file.  That started with the first '90' and ended at the last one.  Copied that into a spreadsheet and tab separated all the values.  From that, wrote a python script that read all of those values, and returned a properly formatted midi file.  We ignored some pieces of data that seemed extraneous.

Running the python script, we get a working midi file, and when viewed in Audacity, it is clearly writing, but not written clearly!

Very hard to interpret, team effort here, and a couple tries came up with wsc{*****_**}

### Data Sample "hex_notes.txt"
```
C2	90	39	64	20	C2	90	38	64
20	C2	90	35	64	20	C2	90	36	64	20	C2	90	37	64	30	E2	82	AC	39	40	20	E2	82	AC	38	40	20	E2	82	AC	35	40	20	E2	82	AC	36	40	20
E2	82	AC	37	40	20	C2	90	34	64	30	E2	82	AC	34	40	20	C2	90	37	64	20	C2	90	36	64	20	C2	90	35	64	30	E2	82	AC	37	40	20	E2	82
A
```

### Python Script
```
from mido import Message, MidiFile, MidiTrack

notes = ''

f = open('hex_notes.txt')
for line in f:
    notes = notes + line.replace('\n', '\t')

notes = notes.split('\t')

note_groups = []

tmp = []

for i in range(0,len(notes)):
    if notes[i] == '90' or notes[i] == '82':
        note_groups.append(tmp)
        tmp = []
    if notes[i] == '82':
        tmp.append('80')
    elif notes[i] != 'AC':
        tmp.append(notes[i])

for itm in note_groups:
    print(itm)

counter = 0

for itm in note_groups:
    if itm[0] == '90':
        counter = counter + 1
    if itm[0] == '82':
        counter = 0

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
for itm in note_groups:
    if len(itm) > 3:
        note = itm[0] + ' ' + itm[1] + ' ' + itm[2] + ' ' + itm[3]
        note = itm[0], int(itm[1], 16), int(itm[2], 16), int(itm[3], 16) 
        print(note)
        if itm[0] == '90':
            track.append(Message('note_on', note=int(itm[1], 16), velocity=64, time=int(itm[3], 16) ) )
        elif itm[0] == '80':
            track.append(Message('note_off', note=int(itm[1], 16), velocity=64, time=int(itm[3], 16)))

for item in mid.tracks:
    print(item)

for msg in mid.tracks[0]:
    print(msg)

mid.save('new_song.mid')


```

### Resources

MIDI Specs:
https://www.cs.cmu.edu/~music/cmsip/readings/Standard-MIDI-file-format-updated.pdf

MIDO Python Docs:
https://mido.readthedocs.io/en/latest/
