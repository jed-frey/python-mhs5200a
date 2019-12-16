import time

import serial
from cached_property import cached_property

from .channel import Channel
from .utils import cmd_map


class MHS5200:
    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        # Create a list for the channels.
        self.channels = list()
        # Number of channels on the device.
        num_channels = 2
        # For each of the possible channels.
        for channel_number in range(num_channels):
            # Instantiate channel
            channel_obj = Channel(self, channel_number + 1)
            # Append to the channel list.
            self.channels.append(channel_obj)
            # Allow referencing channel by a parameter.
            setattr(self, "chan{}".format(channel_number + 1), channel_obj)

        # Send an empty string to flush buffers and set device to a known
        # state.
        self.send("")

    @cached_property
    def serial(self):
        # Serial configuration.
        cfg = dict()
        # Serial Basics
        cfg["port"] = self.port
        cfg["baudrate"] = 57600

        # Flow Control
        cfg["xonxoff"] = False
        cfg["rtscts"] = False
        cfg["dsrdtr"] = False

        # Timeouts.
        cfg["timeout"] = 0.5
        cfg["write_timeout"] = 0.5

        self.cfg = cfg
        # Open the serial port.
        self.serial = serial.Serial(**cfg)
        return self.serial

    def on(self):
        self._set(1, "on", 1)

    def off(self):
        self._set(1, "on", 0)

    @property
    def model(self):
        try:
            raw_model = self.send("r0c")
            return raw_model[4:]
        except:
            return ""

    def send(self, msg="", return_line=True):
        """
        Send message over the serial port to the MHS5200 device.

        Automatically adds the ':' prefix and CRLF to the message.        
        """
        # Flush input and output buffers.
        self.serial.flushInput()
        self.serial.flushOutput()
        # Create the message string.
        cmd_str = f":{msg}\r\n"
        # Send the message out the serial bus.
        self.serial.write(cmd_str.encode())
        # If a return line is expected
        if return_line:
            # Read the line.
            data = self.serial.readline()
            # Decode and strip the CRLF.
            data_clean = data.decode().strip()
            # Return the data string.
            return data_clean

    def _read(self, channel, prop):
        """
        Read a channel's value.
        """
        cmd_str = "r{}{}".format(channel, cmd_map[prop])
        return self.send(cmd_str, return_line=True)

    def _set(self, channel, prop, value):
        """
        Set a channel's value
        """
        cmd_str = "s{}{}{}".format(channel, cmd_map[prop], value)
        response = self.send(cmd_str, return_line=True)
        assert response == "ok"

    def save(self, slot=0):
        """
        Save settings to a memory slot.

        Memory slot 0 is the default when device is powered on.
        """
        response = self.send(f"s{slot}u")
        assert response == "ok"

    def load(self, slot=0):
        """
        Load settings from a memory slot.
        """
        response = self.send(f"s{slot}v")
        assert response == "ok"

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        t1 = time.time()
        while self.serial.isOpen():
            if time.time() > t1 + 5:
                break
            self.serial.close()
            time.sleep(0.2)
