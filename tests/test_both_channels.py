import time
def test_both_freq_01(signal_generator):
    for frequency in [0.5, 1, 2, 5, 10]:
        for channel in signal_generator.channels:
            channel.frequency=frequency
            
