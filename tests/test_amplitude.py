import time
import pytest
import mhs5200

@pytest.mark.parametrize("channel", [0, 1])
@pytest.mark.parametrize("amplitude", [0.2, 1, 2, 5, 10, 20])
@pytest.mark.parametrize("frequency", [100, 200, 500, 1000])
def test_amp(signal_generator, channel, amplitude, frequency):
    chan = signal_generator.channels[channel]
    chan.amplitude = amplitude
    chan.frequency = frequency
    chan.wave = mhs5200.enums.SINE
    time.sleep(0.5)
    assert chan.amplitude == amplitude
    assert chan.frequency == frequency
