# Speaker Tests

- 8Ohm, 2W toy speaker connected to channel 2 with BNC test leads.


```python
import mhs5200
```


```python
from mhs5200.enums import SINE, SQUARE, UP, DOWN, TRI
# sine, square, ramp up, ramp down, triangle.
```


```python
import time
```


```python
signal_gen = mhs5200.MHS5200(port="/dev/ttyUSB0")
signal_gen.on()
channel = signal_gen.chan2
```

1 Hz square wave.


```python
channel.amplitude=1
channel.frequency=1
channel.wave=SQUARE
```

1 Hz square wave, louder.


```python
channel.amplitude=2
channel.frequency=1
channel.wave=SQUARE
```


```python
channel.amplitude=0.5
channel.frequency=2
channel.wave=SQUARE
```

This is only a test.


```python
channel.amplitude=0.5
channel.frequency=1000
channel.wave=SINE
```

What 1kHz sounds like in different wave forms.


```python
for wave in [SINE, SQUARE, UP, DOWN, TRI]:
    channel.amplitude=0.5
    channel.frequency=1000
    channel.wave=wave
    time.sleep(5)
```
