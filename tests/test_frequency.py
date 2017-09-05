def test_freq_01(chan1):
    freq = 1
    chan1.frequency = freq
    assert(chan1.frequency == freq)


def test_freq_10(chan1):
    freq = 10
    chan1.frequency = freq
    assert(chan1.frequency == freq)


def test_freq_100(chan1):
    freq = 100
    chan1.frequency = freq
    assert(chan1.frequency == freq)


def test_freq_1MHz(chan1):
    chan1.frequency = "1MHz"
    assert(chan1.frequency == 1000000)


def test_freq_1kHz(chan1):
    chan1.frequency = "1kHz"
    assert(chan1.frequency == 1000)
