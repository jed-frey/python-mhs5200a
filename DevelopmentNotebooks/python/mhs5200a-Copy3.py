#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[13]:


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
        
    @property
    def model(self):
        return self.send("r0c")

sg = MHS5200A()
sg.init()
s = sg.serial
chan1 = sg.channels[0]


# In[15]:


chan1._offset


# In[16]:


chan1._amplitude


# In[26]:


for attribute, _ in cmd_map.items():
    print("""
    @property
    def {}(self):
        raw_value = self._{}
        return raw_value""".format(attribute, attribute))


# In[27]:


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
        self.dds._set(self, raw_value)
        
    @property
    def wave(self):
        raw_value = self._wave
        return raw_value
        
    @property
    def duty_cycle(self):
        raw_value = self._duty_cycle
        return raw_value
    
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
        return raw_value

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
    setattr(Channel, "_"+attribute, property(getter_gen(attribute),
                                             setter_gen(attribute)))


# In[28]:


chan1 = Channel(sg, 1)


# In[31]:


chan1.amplitude


# In[33]:


sg.send("r0e", return_line=True)


# In[34]:


sg.send("r1g", return_line=True)


# In[35]:


sg.send("r3f", return_line=True)


# In[36]:


sg.send("r4f", return_line=True)


# In[37]:


sg.send("r9b", return_line=True)


# In[38]:


sg.send("r1m", return_line=True)


# In[ ]:




