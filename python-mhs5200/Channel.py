# -*- coding: utf-8 -*-
from .utils import cmd_map

class Channel(object):
    def __init__(self, dds, num):
        self.dds = dds
        self.num = num
        
    @property
    def frequency(self):
        raw_value = self._frequency
        return float(raw_value)/100
        
    @frequency.setter
    def frequency(self, value):
        raw_value = int(value*100)
        self._frequency = raw_value
    
    @property
    def wave(self):
        raw_value = self._wave
        return raw_value
        
    @property
    def duty_cycle(self):
        raw_value = self._duty_cycle
        return float(raw_value)/10
    
    @duty_cycle.setter
    def duty_cycle(self, value):
        raw_value = int(value*10)
        self.dds._set(self, "duty_cycle", raw_value)
        
    @property
    def offset(self):
        raw_value = self._offset
        return raw_value - 120
    
    @property
    def phase(self):
        raw_value = self._phase
        return self._phase
    
    @property
    def atten(self):
        raw_value = self._atten
        return raw_value   
    
    @property
    def on(self):
        raw_value = self._on
        return raw_value
    
    @property
    def amplitude(self):
        raw_value = self._amplitude
        return float(raw_value)/100
    
    @amplitude.setter
    def amplitude(self, value):
        raw_value = int(value*100)
        self.dds._set(self, "amplitude", raw_value)
        
    def __str__(self):
        return "{}".format(self.num)
    
    def __repr__(self):
        return "Channel<{}>".format(self.num)
        
def getter_gen(parameter):
    def getter_fcn(self):
        cmd = cmd_map[parameter]
        raw_value = self.dds._read(self, parameter)
        value = raw_value.split(cmd)[1]
        return int(value)
        
    return getter_fcn

def setter_gen(parameter):
    def setter_fcn(self, value):
        return self.dds._set(self, parameter, value)
        
    return setter_fcn

for attribute, _ in cmd_map.items():
    setattr(Channel, "_{}".format(attribute), property(
        getter_gen(attribute),
        setter_gen(attribute),))