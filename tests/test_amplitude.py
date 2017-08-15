def test_amp_002(signal_generator):
    chan1 = signal_generator.channels[0]
    amplitude = 0.2
    chan1.amplitude = amplitude
    assert(chan1.amplitude == amplitude)
    
def test_amp_020(signal_generator):
    chan1 = signal_generator.channels[0]
    amplitude = 2
    chan1.amplitude = amplitude
    assert(chan1.amplitude == amplitude)
    
def test_amp_200(signal_generator):
    chan1 = signal_generator.channels[0]
    amplitude = 20
    chan1.amplitude = amplitude
    assert(chan1.amplitude == amplitude)