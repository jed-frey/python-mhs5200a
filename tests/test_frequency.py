def test_freq_01(signal_generator):
    chan1 = signal_generator.channels[0]
    freq = 1
    chan1.frequency = freq
    assert(chan1.frequency == freq)
    
    
def test_freq_10(signal_generator):
    chan1 = signal_generator.channels[0]
    freq = 10
    chan1.frequency = freq
    assert(chan1.frequency == freq)
    
    
def test_freq_100(signal_generator):
    chan1 = signal_generator.channels[0]
    freq = 100
    chan1.frequency = freq
    assert(chan1.frequency == freq)