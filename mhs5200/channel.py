from .utils import cmd_map


class Channel:
    def __init__(self, dds, num):
        self.dds = dds
        self.num = num

    @property
    def frequency(self):
        raw_value = self._frequency
        return float(raw_value) / 100

    @frequency.setter
    def frequency(self, value):
        if isinstance(value, str):
            if value.endswith("MHz"):
                multiplier = 1000000
            elif value.endswith("kHz"):
                multiplier = 1000
            elif value.endswith("Hz"):
                multiplier = 1
            else:
                raise (Exception("Frequency does not end with known unit"))
            value = value.strip("MkHz ")
            value = int(value) * multiplier

        raw_value = int(value * 100)

        self._frequency = raw_value

    @property
    def wave(self):
        raw_value = self._wave
        return raw_value

    @wave.setter
    def wave(self, value):
        raw_value = value
        self._wave = raw_value

    @property
    def duty_cycle(self):
        raw_value = self._duty_cycle
        return float(raw_value) / 10

    @duty_cycle.setter
    def duty_cycle(self, value):
        raw_value = int(value * 10)
        self._duty_cycle = raw_value

    @property
    def offset(self):
        raw_value = self._offset
        return raw_value - 120

    @offset.setter
    def offset(self, value):
        raw_value = int(value + 120)
        self._offset = raw_value

    @property
    def phase(self):
        raw_value = self._phase
        return raw_value

    @phase.setter
    def phase(self, value):
        raw_value = int(value)
        self._phase = raw_value

    @property
    def atten(self):
        raw_value = self._atten
        return raw_value

    @property
    def amplitude(self):
        raw_value = self._amplitude
        return float(raw_value) / 100

    @amplitude.setter
    def amplitude(self, value):
        raw_value = int(value * 100)
        self.dds._set(self, "amplitude", raw_value)

    def __str__(self):
        return f"{self.num}"

    def __repr__(self):
        return f"Channel<{self.num}, {self.amplitude}V@{self.frequency}Hz>"


# Function generator for get functions.


def getter_gen(parameter):
    def getter_fcn(self):
        cmd = cmd_map[parameter]
        raw_value = self.dds._read(self, parameter)
        value = raw_value.split(cmd)[1]
        return int(value)

    return getter_fcn


# Function generator for set functions.


def setter_gen(parameter):
    def setter_fcn(self, value):
        return self.dds._set(self, parameter, value)

    return setter_fcn


# Add each of the set & get methods to the Channel class.
for attribute, _ in cmd_map.items():
    setattr(Channel, f"_{attribute}", property(getter_gen(attribute), setter_gen(attribute)))  # Add to the channel class  # Prefix the attribute as 'internal'.  # Add as a property.  # Define getter  # Define setter
