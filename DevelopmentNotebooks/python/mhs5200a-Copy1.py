#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import serial


# In[ ]:


cmd_map = dict()
cmd_map["frequency"]="f"
cmd_map["wave"]="w"
cmd_map["duty_cycle"]="d"
cmd_map["offset"]="o"
cmd_map["phase"]="p"
cmd_map["atten"]="y"
cmd_map["amplitude"]="a"
cmd_map["on"]="b"


# In[3]:


import logging


# In[4]:


logger=logging.Logger(__name__)
logger.setLevel(logging.DEBUG)
info=logger.info
debug=logger.debug


# In[5]:


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


# In[9]:


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
        print(cmd_str)
        return self.send(cmd_str, return_line=True)
    
    def _set(self, channel, prop,value):
        cmd_str = "r{}{}{}".format(channel, cmd_map[prop], value)
        print(cmd_str)
        return self.send(cmd_str, return_line=True)
   
    def init(self):
        self.send(":")
        self.send(":r1c")
        self.send(":r2c")

sg = MHS5200A()
sg.init()
s = sg.serial
chan1 = sg.channels[0]


# In[10]:


sg.send(":s1f0000000100", return_line=True)


# In[11]:


data = sg.send(":r1f", return_line=True)
data


# In[13]:


sg._read(1, 'frequency')


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


# In[15]:


chan1 = Channel(sg, 1)


# In[17]:


for attribute, cmd in cmd_map.items():
    break
(attribute, cmd)


# In[18]:


def getter_gen(parameter):
    def getter_fcn(self):
        value = self.dds._read(self, parameter)
        return value    
    return getter_fcn


# In[22]:


setattr(Channel, "_"+attribute, property(getter_gen(attribute)))


# In[23]:


chan1._offset


# In[ ]:




