#!/usr/bin/env python
# coding: utf-8

# In[1]:


import serial


# In[11]:


cmd_map = dict()
cmd_map["frequency"]="f"
cmd_map["wave"]="w"
cmd_map["duty_cycle"]="d"
cmd_map["offset"]="o"
cmd_map["phase"]="p"
cmd_map["atten"]="y"
cmd_map["amplitude"]="a"
cmd_map["on"]="b"


# In[12]:


import logging


# In[13]:


logger=logging.Logger(__name__)
logger.setLevel(logging.DEBUG)
info=logger.info
debug=logger.debug


# In[14]:


class Channel(object):
    def __init__(self, dds, num):
        self.dds = dds
        self.num = num
        
        
    def __str__(self):
        return "{}".format(self.num)
    
    def __repr__(self):
        return "Channel<{}>".format(self.num)
        
    @property
    def frequency(self):
        return self.dds.get(self, "frequency")

def getter_gen(parameter):
    def getter_fcn(self):
        value = self.dds._read(self, parameter)
        return value    
    return getter_fcn

for attribute, _ in cmd_map.items():
    setattr(Channel, "_"+attribute, property(getter_gen(attribute)))


# In[53]:


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
        
    def send(self, msg="", return_line = False):
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
   
    def init(self):
        self.send(":")
        self.send(":r1c")
        self.send(":r2c")

sg = MHS5200A()
sg.init()
s = sg.serial
chan1 = sg.channels[0]


# In[54]:


chan1._frequency


# In[55]:


for attribute, _ in cmd_map.items():
    if hasattr(chan1, "_"+attribute):
        print("{}: {}".format(attribute, getattr(chan1, "_"+attribute)))


# In[56]:


class Channel(object):
    def __init__(self, dds, num):
        self.dds = dds
        self.num = num

    def __str__(self):
        return "{}".format(self.num)
    
    def __repr__(self):
        return "Channel<{}>".format(self.num)
        
    @property
    def frequency(self):
        return self.dds.get(self, "frequency")

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
    setattr(Channel, "_"+attribute, property(getter_gen(attribute),
                                             setter_gen(attribute)))


# In[57]:


chan1 = Channel(sg, 1)

chan1._frequency


# In[58]:


for attribute, _ in cmd_map.items():
    if hasattr(chan1, "_"+attribute):
        print("{}: {}".format(attribute, getattr(chan1, "_"+attribute)))


# In[59]:


chan1._frequency = 200


# In[60]:


sg._set(1, 'frequency', 200)


# In[62]:


chan1._frequency


# In[63]:


chan1._frequency = 50


# In[64]:


chan1._frequency


# In[ ]:




