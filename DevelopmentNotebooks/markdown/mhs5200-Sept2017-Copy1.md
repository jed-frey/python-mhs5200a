```python
%load_ext autoreload
%autoreload 1
```


```python
import serial
serial.__version__
```


```python
from mhs5200 import MHS5200
```


```python
%autoreload
```


```python
signal_generator.serial.close()
```


```python

```


```python
signal_generator = MHS5200('COM4')
```


```python
signal_generator.chan1
```




    Channel<1, 20.0V@1000.0Hz>




```python
signal_generator.chan2
```




    Channel<2, 5.0V@100.0Hz>




```python
chan1 = signal_generator.chan1
```


```python
chan2 = signal_generator.chan2
```


```python
chan1.frequency="10Hz"
```


```python
chan2.frequency="10Hz"
```


```python
from mhs5200.Enums import Wave
```


```python
chan1.wave = Wave.SINE
```


```python
chan2.wave = Wave.SQUARE
```


```python
chan1.amplitude=20
chan2.amplitude=20
```


```python
chan1.frequency="1kHz"
```


```python
chan1.frequency="1 kHz"
```


```python
chan1.frequency
```


```python
for attr in dir(chan1):
    if attr.startswith("__"):
        continue
    if attr.startswith("_"):
        v = getattr(chan1, attr)
        print("{}: {}".format(attr, v))
```


```python
chan1.duty_cycle
```


```python
chan1._offset
```


```python
chan1._phase
```


```python
chan1._on
```


```python
chan2._on
```


```python
chan1._on=0
```


```python
chan2._on=1
```


```python
s = signal_generator.serial
```


```python
cmd = "s1b0"

s.write((cmd+"\r\n").encode())
```


```python
s.readline()
```


```python
s.flushInput()
```


```python
signal_generator._set(1, "on", 1)
```


```python
s.readlines()
```


```python
s.flushInput()
```


```python
signal_generator._set(2, "on", 0)
```


```python
s.readline()
```


```python
chan1._on
```


```python
chan1._on=0
```


```python
signal_generator.send("r0c")[4:]
```


```python
signal_generator.send("r1c")
```


```python
signal_generator.send("r2c")
```


```python
signal_generator.off()
```


```python
f = ["1MHz", "1 MHz", "1kHz", "1 kHz"]
```


```python

```


```python
f[2].strip("MHz")
```


```python

```


```python

```
