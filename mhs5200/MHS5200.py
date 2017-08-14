# -*- coding: utf-8 -*-
import serial
from .utils import cmd_map
from .Channel import Channel


class MHS5200(object):
    def __init__(self, port="/dev/ttyUSB0"):
        # Serial configuration.
        cfg=dict()
        cfg["port"]=port
        cfg["baudrate"]=57600
        cfg["xonxoff"]=False        
        cfg["timeout"]=0.5
        cfg["write_timeout"]=0.5
        cfg["rtscts"]=False
        cfg["dsrdtr"]=False
        
        self.cfg = cfg
        # Open the serial port.
        self.serial = serial.Serial(**cfg)
        
        # Create list of channels.
        self.channels = list()
        self.channels.append(Channel(self, 1))    
        self.channels.append(Channel(self, 2))  
        # Send an empty string to flush buffers and set device to a known state.
        self.send("")
        
    def send(self, msg="", return_line = True):
        """
        Send message over the serial port to the MHS5200 device.
        
        Automatically adds the ':' prefix and CRLF to the message.        
        """
        
        # Flush input and output buffers.
        self.serial.flushInput()
        self.serial.flushOutput()
        # Create the message string.
        cmd_str = ":{}\r\n".format(msg)
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
        assert(response=="ok")
        
    def save(self, memory_slot=0):
        """
        Save settings to a slot
        """
        response = self.send("s{}u".format(memory_slot))
        assert(response=="ok")

    def load(self, memory_slot=0):
        """
        Load settings from a slot
        """
        response = self.send("s{}v".format(memory_slot))
        assert(response=="ok")