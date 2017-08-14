# -*- coding: utf-8 -*-
from .utils import cmd_map
from .Channel import Channel


class MHS5200A(object):
    def __init__(self, port="/dev/ttyUSB2"):
        cfg=dict()
        cfg["port"]=port
        cfg["baudrate"]=57600
        cfg["xonxoff"]=False        
        cfg["timeout"]=0.5
        cfg["rtscts"]=True
        cfg["dsrdtr"]=False
        self.cfg = cfg
        self.serial = serial.Serial(**cfg)
        self.channels = list()
        self.channels.append(Channel(self, 1))    
        self.channels.append(Channel(self, 2))        
        self.send("")
        
    def send(self, msg="", return_line = True):
        self.serial.flushInput()
        self.serial.flushOutput()
        cmd_str = ":{}\r\n".format(msg)
        self.serial.write(cmd_str.encode())
        if return_line:
            data = self.serial.readline()
            data_clean = data.decode().strip()
            return data_clean
        
    def _read(self, channel, prop):
        cmd_str = "r{}{}".format(channel, cmd_map[prop])
        return self.send(cmd_str, return_line=True)
    
    def _set(self, channel, prop, value):
        cmd_str = "s{}{}{}".format(channel, cmd_map[prop], value)
        response = self.send(cmd_str, return_line=True)
        assert(response=="ok")
        
    def save(self, memory_slot=0):
        response = self.send("s{}u".format(memory_slot))
        assert(response=="ok")

    def load(self, memory_slot=0):
        response = self.send("s{}v".format(memory_slot))
        assert(response=="ok")