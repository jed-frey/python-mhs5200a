"""
Mapping from the command name to the initialism used in the protocol.
"""
cmd_map = dict()
cmd_map["frequency"] = "f"
cmd_map["wave"] = "w"
cmd_map["duty_cycle"] = "d"
cmd_map["offset"] = "o"
cmd_map["phase"] = "p"
cmd_map["atten"] = "y"
cmd_map["amplitude"] = "a"
cmd_map["on"] = "b"


import time
import re

song_re = re.compile("([A-G]?#?)")

from typing import List


def get_freq(n=-21):
    """ Generate a frequency from an 'n'.

    Based on an equation:
      https://www.intmath.com/trigonometric-graphs/music.php
    """
    return 440.0 * 2.0 ** (n / 12.0)


def get_note_frequency(note, octave=0):
    """Get the frequency of a note:

    note: Musical note.
    octave: Setup so octave=0, A = 440 Hz.
    """
    n = notes.index(note) - 9.0 - octave * 12.0
    return get_freq(n)


def play_song(inst, song, octave=0):
    inst.on()
    for note in song:
        chan = inst.channels[1]
        chan.amplitude = 0
        # Between beats
        time.sleep(0.1)
        chan.frequency = get_note_frequency(note, octave)
        chan.amplitude = 1.0
        chan.offset = 0
        chan.wave = 0
        time.sleep(0.2)
    inst.off()


notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def play_scale(inst, octave=0):
    play_song(notes)


songs = {
    "twinkle": "CCGGAAGFFEEDDCGGFFEEDGGFFEEDCCGGAAGFFEEDDC",
    "baby_shark": "CDFFFFFFFFCDFFFFFFFFCDFFFFFFFFFFE",
}
