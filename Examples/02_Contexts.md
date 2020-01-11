# Signal Gen Contexts

Use the signal generator in a context.


```python
import mhs5200
import mhs5200.enums as WAVE
```


```python
with mhs5200.MHS5200(port="/dev/ttyUSB0") as signal_generator:
    for channel in signal_generator.channels:
        channel.frequency = 1
        channel.amplitude = 0
        channel.offset    = 0
        channel.wave = WAVE.SINE
```
