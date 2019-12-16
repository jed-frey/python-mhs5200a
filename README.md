# `python-mhs5200`

Python module for controlling inexpensive MHS5200 signal generators.

The MHS5200 are an inexpensive family of DDS signal generators that have 16 arbitrary wave functions. However, the software is for Windows and not especially good (giant Labview compiled program with lots of issues).

Developed using the [KKmoon High Precision Digital DDS Dual-channel Signal Source Generator Arbitrary Waveform Frequency Meter 200MSa/s 25MHz.](http://www.amznly.com/3nz).

## Installation

```
pip install git+https://github.com/jed-frey/python_mhs5200.git#egg=mhs5200
```

## Useage Examples:


```python
from mhs5200 import MHS5200
from mhs5200.enums import WAVE
signal_gen = MHS5200(port="/dev/ttyUSB0")
```

### Signal Generator Object:


```python
 for key in dir(signal_gen):
    if key.startswith("_"):
        continue
    value = getattr(signal_gen, key)
    print(f"{key}: {value}")
```

    cfg: {'port': '/dev/ttyUSB0', 'baudrate': 57600, 'xonxoff': False, 'rtscts': False, 'dsrdtr': False, 'timeout': 0.5, 'write_timeout': 0.5}
    chan1: 1
    chan2: 2
    channels: [Channel<1, 20.0V@1000.0Hz>, Channel<2, 10.0V@0.5Hz>]
    load: <bound method MHS5200.load of <mhs5200.mhs5200.MHS5200 object at 0x7fbde8341f70>>
    model: 5225A5040000
    off: <bound method MHS5200.off of <mhs5200.mhs5200.MHS5200 object at 0x7fbde8341f70>>
    on: <bound method MHS5200.on of <mhs5200.mhs5200.MHS5200 object at 0x7fbde8341f70>>
    save: <bound method MHS5200.save of <mhs5200.mhs5200.MHS5200 object at 0x7fbde8341f70>>
    send: <bound method MHS5200.send of <mhs5200.mhs5200.MHS5200 object at 0x7fbde8341f70>>
    serial: Serial<id=0x7fbde8341a30, open=True>(port='/dev/ttyUSB0', baudrate=57600, bytesize=8, parity='N', stopbits=1, timeout=0.5, xonxoff=False, rtscts=False, dsrdtr=False)


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

Save default settings for power on.


```python
signal_gen.save(0)
signal_gen.save()
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
chan1.wave = WAVE.SQUARE
```

Read Channels


```python
chan1.frequency
```




    1.0




```python
chan1.amplitude
```




    10.0




```python
chan1.offset
```




    0



### Set All Channels

For machine lab setup/teardown/make sure oscilloscope is the broken one.


```python
for channel in signal_gen.channels:
    channel.frequency = 0.5
    channel.amplitude = 10
    channel.offset=channel.amplitude/2
    channel.wave = WAVE.SQUARE
```

### Print All Channels & Attributes


```python
for channel in signal_gen.channels:
    print(f"Channel: {channel}")
for key in dir(channel):
        if key.startswith("_"):
            continue
        value = getattr(channel, key)
        print(f"{key}: {value}")
```

    Channel: 1
    Channel: 2
    amplitude: 10.0
    atten: 1
    dds: <mhs5200.mhs5200.MHS5200 object at 0x7fbde8341f70>
    duty_cycle: 50.0
    frequency: 0.5
    num: 2
    offset: 5
    phase: 0
    wave: 1



```python
signal_gen.off()
```

### WAVE enum types:

Supported waves


```python
list(WAVE)
```




    [<WAVE.SINE: 0>,
     <WAVE.SQUARE: 1>,
     <WAVE.TRI: 2>,
     <WAVE.UP: 3>,
     <WAVE.DOWN: 4>,
     <WAVE.ARB0: 100>,
     <WAVE.ARB1: 101>,
     <WAVE.ARB2: 102>,
     <WAVE.ARB3: 103>,
     <WAVE.ARB4: 104>,
     <WAVE.ARB5: 105>,
     <WAVE.ARB6: 106>,
     <WAVE.ARB7: 107>,
     <WAVE.ARB8: 108>,
     <WAVE.ARB9: 109>,
     <WAVE.ARB10: 110>,
     <WAVE.ARB11: 111>,
     <WAVE.ARB12: 112>,
     <WAVE.ARB13: 113>,
     <WAVE.ARB14: 114>,
     <WAVE.ARB15: 115>]



# Additional Links

Credit for all of the hard work goes to user `wd5gnr` from [EEV Blog](https://www.eevblog.com/) for reverse engineering the protcol and documenting it here: [MHS5200A Protocol](https://docs.google.com/document/d/1HbLQ4u87RJkD3Ktyw7k9U7Zh5BPNzbrhMlszNGdXiiY/edit)

- [MHS-5200A DDS Signal Generator](http://land-boards.com/blwiki/index.php?title=MHS-5200A_DDS_Signal_Generator)

- [MHS-5200A Serial Protocol Reverse Engineered](https://www.eevblog.com/forum/testgear/mhs-5200a-serial-protocol-reverse-engineered/)

- [MHS-5200A function generator teardown / review / reverse engineering](https://www.eevblog.com/forum/testgear/mhs-5200a-function-generator-teardown-review-reverse-engineering/)

# TODO

- Integrate with [python-ivi](https://github.com/python-ivi/python-ivi).
- Test on another MHS-5200 device.
- Arbitrary waveforms.
- External measurements.
- Better documentation.
