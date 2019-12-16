#!/usr/bin/env python
# coding: utf-8

# In[1]:


import serial


# In[2]:





# In[6]:


try:
    s.close()
except:
    pass

serialcfg=dict()
serialcfg["port"]="/dev/ttyUSB2"
serialcfg["baudrate"]=57600
serialcfg["xonxoff"]=False
serialcfg["rtscts"]=False
serialcfg["dsrdtr"]=False
serialcfg["timeout"]=1.5

s = serial.Serial(**serialcfg)


# In[16]:


s.write(":\r\n".encode())
s.write(":r1c\r\n".encode())
s.write(":r2c\r\n".encode())


# In[14]:


s.readline()


# In[15]:


s.readline()


# In[10]:


s.readline()


# In[19]:


s.write(":r1c\r\n".encode())
s.readline()


# In[22]:


s.close()


# In[2]:


import serial


# In[12]:


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
        
    def send(self, msg="", return_line = False):
        self.serial.write((msg+"\r\n").encode())
        if return_line:
            return self.serial.readline()
        
    def get(self, )
    
        
    def init(self):
        self.send(":")
        self.send(":r1c")
        self.send(":r2c")


# In[23]:


sg = MHS5200A()
sg.init()
s = sg.serial


# In[ ]:





# In[ ]:





# In[28]:


s.readline()


# In[30]:


sg.send(":r1f", return_line=True)


# Frequency!

# In[31]:


sg.send(":r1w", return_line=True)


# 
# Read wave type
# NN=00-04 as  above but returns 32-47 for arb0...15
# 

# In[34]:


cmd = dict()
cmd["frequency"]="f"
cmd["wave"]="w"
cmd["duty_cycle"]="d"
cmd["offset"]="o"
cmd["phase"]="p"
cmd["atten"]="y"
cmd["amplitude"]="a"
cmd["on"]="b"


# In[35]:


def getter_gen(parameter):
    def getter_fcn(self):
        pass
    
    
    return getter_fcn
    


# In[ ]:


def setter_gen(parameter):
    pass


# In[21]:


s.close()setattr(cls,
                prop_name.lower(),
                property(getter_gen(prop_name),
                         setter_gen(prop_name)))


# In[37]:


class Channel(object):
    def __init__(self, num):
        self.num = num
        
    def __str__(self):
        return "{}".format(self.num)
    
    def __repr__(self):
        return "Channel<{}>".format(self.num)
    
    @property
    def frequency(self)
    


# In[38]:


chan1 = Channel(1)


# In[39]:


chan1


# In[40]:


s.close()


# In[ ]:




