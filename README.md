# `python-mhs5200`

Python module for controlling inexpensive MHS5200 signal generators.

The MHS5200 are an inexpensive family of DDS signal generators that have 16 arbitrary wave functions. However, the software is for Windows and not especially good (giant Labview compiled program with lots of issues).

Developed using the $43.25 - [KKmoon High Precision Digital DDS Dual-channel Signal Source Generator Arbitrary Waveform Frequency Meter 200MSa/s 25MHz.](http://www.amznly.com/3nz) [Amazon affiliate link benefiting EFF.]

Unit tests require the [python-ds1000de](https://github.com/jed-frey/python-ds1000de) for controlling Rigol DS1000DE scopes.

## Installation

    pip install git+https://github.com/jed-frey/python-mhs5200.git#egg=mhs5200


## Usage

Generate a 1 Hz, 10 V-pp square wave with 0V offset:

    from MHS5200 import MHS5200
    from MHS5200.Enums import Wave
    signal_gen = MHS5200(port="/dev/ttyUSB0")

    chan1 = signal_gen.channels[0]

    chan1.frequency = 1 # Hz
    chan1.amplitude = 10 # V-pp
    chan1.offset = 0 # V
    chan1.wave = Wave.SQUARE


# Additional Links

Credit for all of the hard work goes to user `wd5gnr` from [EEV Blog](https://www.eevblog.com/) for reverse engineering the protcol and documenting it here: [MHS5200A Protocol](https://docs.google.com/document/d/1HbLQ4u87RJkD3Ktyw7k9U7Zh5BPNzbrhMlszNGdXiiY/edit)

- [MHS-5200A DDS Signal Generator](http://land-boards.com/blwiki/index.php?title=MHS-5200A_DDS_Signal_Generator)

- [MHS-5200A Serial Protocol Reverse Engineered](https://www.eevblog.com/forum/testgear/mhs-5200a-serial-protocol-reverse-engineered/)

- [MHS-5200A function generator teardown / review / reverse engineering](https://www.eevblog.com/forum/testgear/mhs-5200a-function-generator-teardown-review-reverse-engineering/)


# TODO

- Test on another MHS-5200 device.
- Arbitrary waveforms.
- External measurements.
- Better documentation.