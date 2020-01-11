# Generate Musical Notes

- 8Ohm, 2W toy speaker.


```python
def get_freq(n:int =-21) -> float:
    """ Generate a frequency from an 'n'.
    
    Based on an equation: 
      https://www.intmath.com/trigonometric-graphs/music.php
    """
    return 440.*2.**(n/12.0)

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def get_note_frequency(note: str, octave: int=0):
    """Get the frequency of a note:
    
    note: Musical note.
    octave: Setup so octave=0, A = 440 Hz.   
    """
    n = notes.index(note)-9.0-octave*12.0
    return get_freq(n)
```


```python
# A
get_freq(0)
```




    440.0




```python
import mhs5200
inst = mhs5200.MHS5200(port="/dev/ttyUSB0")
```


```python
get_note_frequency(note="A", octave=0)
```




    440.0



## Run Musical Scale

Since A=0, go from -9 to 3 (C to B)


```python
import time
```


```python
inst.on()
for n in range(-9, 3):
    for chan in inst.channels:
        chan.amplitude=20
        chan.frequency=get_freq(n)
        chan.offset=0
        chan.wave=0
    time.sleep(0.5)
inst.off()
```


```python
inst.on()
get_note_frequency("C")
```




    261.6255653005986




```python
inst.off()
```


```python
for note in notes:
    chan = inst.channels[1]
    chan.amplitude=5
    print(f"note: {note}")
    chan.frequency=get_note_frequency(note)
    chan.offset=0
    chan.wave=0
    time.sleep(0.5)
```

    note: C
    note: C#
    note: D
    note: D#
    note: E
    note: F
    note: F#
    note: G
    note: G#
    note: A
    note: A#
    note: B


# Twinkle Twinkle Little Star


```python
song = "CCGGAAGFFEEDDCGGFFEEDGGFFEEDCCGGAAGFFEEDDC"
inst.on()
for note in song:
    chan = inst.channels[1]
    chan.amplitude=0
    time.sleep(0.0)
    print(f"note: {note}")
    chan.frequency=get_note_frequency(note, -1)
    chan.amplitude=1
    chan.offset=0
    chan.wave=0
    time.sleep(0.1)
inst.off()
```

    note: C
    note: C
    note: G
    note: G
    note: A
    note: A
    note: G
    note: F
    note: F
    note: E
    note: E
    note: D
    note: D
    note: C
    note: G
    note: G
    note: F
    note: F
    note: E
    note: E
    note: D
    note: G
    note: G
    note: F
    note: F
    note: E
    note: E
    note: D
    note: C
    note: C
    note: G
    note: G
    note: A
    note: A
    note: G
    note: F
    note: F
    note: E
    note: E
    note: D
    note: D
    note: C



```python
import re 
song_re = re.compile("([A-G]?#?)")
```


```python
def play_song(inst, song):
    inst.on()
    for note in song:
        chan = inst.channels[1]
        chan.amplitude=0
        # Between beats
        time.sleep(0.1)
        chan.frequency=get_note_frequency(note, -1)
        chan.amplitude=1.0
        chan.offset=0
        chan.wave=0
        time.sleep(0.2)
    inst.off()
```


```python
twinkle = "CCGGAAGFFEEDDCGGFFEEDGGFFEEDCCGGAAGFFEEDDC"
baby_shark = "CDFFFFFFFFCDFFFFFFFFCDFFFFFFFFFFE"
```


```python
for song in [twinkle, baby_shark]:
    play_song(inst=inst, song=song)
```
