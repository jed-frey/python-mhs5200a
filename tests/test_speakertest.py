"""Tests using a speaker
"""
import time

import pytest

import mhs5200


def test_both_square(signal_generator):
    for frequency in [0.5, 1, 2, 5, 10]:
        for channel in signal_generator.channels:
            channel.frequency = frequency
            channel.amplitude = 20
            channel.wave = mhs5200.enums.SQUARE
            channel.offset = 0
        time.sleep(5)


def test_both_sine(signal_generator):
    for frequency in [100, 500, 1000, 2000]:
        for channel in signal_generator.channels:
            channel.frequency = frequency
            channel.amplitude = 20
            channel.wave = mhs5200.enums.SINE
        time.sleep(2)
