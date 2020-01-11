"""Musical tests using speaker attached to Channel 2's output.

Test Speaker: 8W, 2Ohm.
"""
import time

import pytest

import mhs5200
from mhs5200.utils import get_freq
from mhs5200.utils import get_note_frequency

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def test_get_freq():
    assert get_freq(0) == 440.0


def test_scale(signal_generator):
    chan = signal_generator.channels[1]
    for note in notes:
        chan.amplitude = 20
        chan.frequency = get_note_frequency(note)
        chan.offset = 0
        chan.wave = 0
        time.sleep(0.5)


@pytest.mark.parametrize("note", notes)
def test_scale_parametrized(signal_generator, note):
    """
    Test playing the musicl scale
    """
    chan = signal_generator.channels[1]
    chan.amplitude = 20
    chan.frequency = get_note_frequency(note)
    chan.offset = 0
    chan.wave = 0
    time.sleep(0.5)


import re

# Regex to parse a coarse song.
song_re = re.compile("([A-G]?#?)")
# Some generic songs.
songs = [
    "CCGGAAGFFEEDDCGGFFEEDGGFFEEDCCGGAAGFFEEDDC",  # Twinkle Twinkle
    "CDFFFFFFFFCDFFFFFFFFCDFFFFFFFFFFE",  # Baby Shark
]
# For each of the songs.
@pytest.mark.parametrize("song", songs)
def test_songs(signal_generator, song):
    chan = signal_generator.channels[1]
    for note in song:
        chan.amplitude = 20
        chan.frequency = get_note_frequency(note)
        chan.offset = 0
        chan.wave = 0
        time.sleep(0.5)
