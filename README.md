# `python-mhs5200`

Python module for controlling inexpensive MHS5200 signal generators.

The MHS5200 are an family of DDS signal generators that have 16 arbitrary wave functions. However, the software is for Windows and not especially good (giant Labview compiled program with lots of issues).

Developed using the [KKmoon High Precision Digital DDS Dual-channel Signal Source Generator Arbitrary Waveform Frequency Meter 200MSa/s 25MHz.](http://www.amznly.com/3nz).

## Installation

```
pip install git+https://github.com/dapperfu/python_mhs5200.git#egg=mhs5200
```

## Useage Examples:


```python
from mhs5200 import MHS5200
import mhs5200.enums as WAVE
signal_gen = MHS5200(port="/dev/ttyUSB0")
```

Disable Generator Output


```python
signal_gen.off()
```

Enable Generator Output


```python
signal_gen.on()
```

Save settings to a memory slot.


```python
signal_gen.save(1)
```

Load settings from a memory slot.


```python
signal_gen.load(1)
```

### Channels:


```python
signal_gen.chan1 == signal_gen.channels[0]
```




    True




```python
signal_gen.chan2 == signal_gen.channels[1]
```




    True




```python
chan1 = signal_gen.channels[0]

chan1.frequency = 1 # Hz
chan1.amplitude = 10 # V-pp
chan1.offset = 0 # V
chan1.wave = WAVE.SINE

chan2 = signal_gen.chan2
chan2.frequency = 2 # Hz
chan2.amplitude = 5 # V-pp
chan2.offset = 2.5 # V
chan2.wave = WAVE.SQUARE
```

Save default settings for power on. The above code block sets the power on settings.


```python
signal_gen.save(0)
signal_gen.save()
```

Read Channels


```python
for channel in signal_gen.channels:
    print(f"{channel.frequency}Hz, {channel.amplitude}V")
```

    1.0Hz, 10.0V
    2.0Hz, 5.0V



```python
signal_gen.off()
```

# Twinkle Twinkle Little Star


```python
from mhs5200.utils import songs, play_song
```


```python
play_song(signal_gen, songs["twinkle"])
```

# Tests

Multiple tests are included, TODO close loop with oscilloscope.


```python
!pytest --port=/dev/ttyUSB0
```

    [1m============================= test session starts ==============================[0m
    platform linux -- Python 3.8.0, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
    rootdir: /projects/OSH-HIL/components/python_mhs5200, inifile: setup.cfg
    plugins: metadata-1.8.0, csv-2.0.2, html-2.0.1
    collected 72 items                                                             [0m
    
    tests/test_amplitude.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m [ 66%]
    [0m[32m                                                                         [ 66%][0m
    tests/test_both_channels.py [32m.[0m[32m                                            [ 68%][0m
    tests/test_frequency.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                            [ 75%][0m
    tests/test_musical.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                   [ 97%][0m
    tests/test_speakertest.py [32m.[0m[32m.[0m[32m                                             [100%][0m
    
    ==================================== PASSES ====================================
    ----------------- CSV report: test-artifacts/test_artifact.csv -----------------
    - generated html file: file:///projects/OSH-HIL/components/python_mhs5200/test-artifacts/test_artifact.html -
    =========================== short test summary info ============================
    PASSED tests/test_amplitude.py::test_amp[100-0.2-0]
    PASSED tests/test_amplitude.py::test_amp[100-0.2-1]
    PASSED tests/test_amplitude.py::test_amp[100-1-0]
    PASSED tests/test_amplitude.py::test_amp[100-1-1]
    PASSED tests/test_amplitude.py::test_amp[100-2-0]
    PASSED tests/test_amplitude.py::test_amp[100-2-1]
    PASSED tests/test_amplitude.py::test_amp[100-5-0]
    PASSED tests/test_amplitude.py::test_amp[100-5-1]
    PASSED tests/test_amplitude.py::test_amp[100-10-0]
    PASSED tests/test_amplitude.py::test_amp[100-10-1]
    PASSED tests/test_amplitude.py::test_amp[100-20-0]
    PASSED tests/test_amplitude.py::test_amp[100-20-1]
    PASSED tests/test_amplitude.py::test_amp[200-0.2-0]
    PASSED tests/test_amplitude.py::test_amp[200-0.2-1]
    PASSED tests/test_amplitude.py::test_amp[200-1-0]
    PASSED tests/test_amplitude.py::test_amp[200-1-1]
    PASSED tests/test_amplitude.py::test_amp[200-2-0]
    PASSED tests/test_amplitude.py::test_amp[200-2-1]
    PASSED tests/test_amplitude.py::test_amp[200-5-0]
    PASSED tests/test_amplitude.py::test_amp[200-5-1]
    PASSED tests/test_amplitude.py::test_amp[200-10-0]
    PASSED tests/test_amplitude.py::test_amp[200-10-1]
    PASSED tests/test_amplitude.py::test_amp[200-20-0]
    PASSED tests/test_amplitude.py::test_amp[200-20-1]
    PASSED tests/test_amplitude.py::test_amp[500-0.2-0]
    PASSED tests/test_amplitude.py::test_amp[500-0.2-1]
    PASSED tests/test_amplitude.py::test_amp[500-1-0]
    PASSED tests/test_amplitude.py::test_amp[500-1-1]
    PASSED tests/test_amplitude.py::test_amp[500-2-0]
    PASSED tests/test_amplitude.py::test_amp[500-2-1]
    PASSED tests/test_amplitude.py::test_amp[500-5-0]
    PASSED tests/test_amplitude.py::test_amp[500-5-1]
    PASSED tests/test_amplitude.py::test_amp[500-10-0]
    PASSED tests/test_amplitude.py::test_amp[500-10-1]
    PASSED tests/test_amplitude.py::test_amp[500-20-0]
    PASSED tests/test_amplitude.py::test_amp[500-20-1]
    PASSED tests/test_amplitude.py::test_amp[1000-0.2-0]
    PASSED tests/test_amplitude.py::test_amp[1000-0.2-1]
    PASSED tests/test_amplitude.py::test_amp[1000-1-0]
    PASSED tests/test_amplitude.py::test_amp[1000-1-1]
    PASSED tests/test_amplitude.py::test_amp[1000-2-0]
    PASSED tests/test_amplitude.py::test_amp[1000-2-1]
    PASSED tests/test_amplitude.py::test_amp[1000-5-0]
    PASSED tests/test_amplitude.py::test_amp[1000-5-1]
    PASSED tests/test_amplitude.py::test_amp[1000-10-0]
    PASSED tests/test_amplitude.py::test_amp[1000-10-1]
    PASSED tests/test_amplitude.py::test_amp[1000-20-0]
    PASSED tests/test_amplitude.py::test_amp[1000-20-1]
    PASSED tests/test_both_channels.py::test_both_freq_01
    PASSED tests/test_frequency.py::test_freq_01
    PASSED tests/test_frequency.py::test_freq_10
    PASSED tests/test_frequency.py::test_freq_100
    PASSED tests/test_frequency.py::test_freq_1MHz
    PASSED tests/test_frequency.py::test_freq_1kHz
    PASSED tests/test_musical.py::test_get_freq
    PASSED tests/test_musical.py::test_scale
    PASSED tests/test_musical.py::test_scale_parametrized[C]
    PASSED tests/test_musical.py::test_scale_parametrized[C#]
    PASSED tests/test_musical.py::test_scale_parametrized[D]
    PASSED tests/test_musical.py::test_scale_parametrized[D#]
    PASSED tests/test_musical.py::test_scale_parametrized[E]
    PASSED tests/test_musical.py::test_scale_parametrized[F]
    PASSED tests/test_musical.py::test_scale_parametrized[F#]
    PASSED tests/test_musical.py::test_scale_parametrized[G]
    PASSED tests/test_musical.py::test_scale_parametrized[G#]
    PASSED tests/test_musical.py::test_scale_parametrized[A]
    PASSED tests/test_musical.py::test_scale_parametrized[A#]
    PASSED tests/test_musical.py::test_scale_parametrized[B]
    PASSED tests/test_musical.py::test_songs[CCGGAAGFFEEDDCGGFFEEDGGFFEEDCCGGAAGFFEEDDC]
    PASSED tests/test_musical.py::test_songs[CDFFFFFFFFCDFFFFFFFFCDFFFFFFFFFFE]
    PASSED tests/test_speakertest.py::test_both_square
    PASSED tests/test_speakertest.py::test_both_sine
    [32m======================== [32m[1m72 passed[0m[32m in 121.86s (0:02:01)[0m[32m ========================[0m


# Additional Links

Credit for all of the hard work goes to user `wd5gnr` from [EEV Blog](https://www.eevblog.com/) for reverse engineering the protcol and documenting it here: [MHS5200A Protocol](https://docs.google.com/document/d/1HbLQ4u87RJkD3Ktyw7k9U7Zh5BPNzbrhMlszNGdXiiY/edit)

- [MHS-5200A DDS Signal Generator](http://land-boards.com/blwiki/index.php?title=MHS-5200A_DDS_Signal_Generator)

- [MHS-5200A Serial Protocol Reverse Engineered](https://www.eevblog.com/forum/testgear/mhs-5200a-serial-protocol-reverse-engineered/)

- [MHS-5200A function generator teardown / review / reverse engineering](https://www.eevblog.com/forum/testgear/mhs-5200a-function-generator-teardown-review-reverse-engineering/)

# TODO

- Integrate / test against [python-ivi](https://github.com/python-ivi/python-ivi) &/| [InstrumentKit](https://github.com/Galvant/InstrumentKit)
- Test on another MHS-5200 device.
- Better crossplatfor testing.
- Arbitrary waveforms.
- External measurements.
- Better documentation.
- Closed loop testing.
