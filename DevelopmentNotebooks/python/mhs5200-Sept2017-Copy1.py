#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '1')


# In[ ]:


import serial
serial.__version__


# In[1]:


from mhs5200 import MHS5200


# In[ ]:


get_ipython().run_line_magic('autoreload', '')


# In[ ]:


signal_generator.serial.close()


# In[ ]:





# In[3]:


signal_generator = MHS5200('COM4')


# In[4]:


signal_generator.chan1


# In[5]:


signal_generator.chan2


# In[6]:


chan1 = signal_generator.chan1


# In[7]:


chan2 = signal_generator.chan2


# In[8]:


chan1.frequency="10Hz"


# In[9]:


chan2.frequency="10Hz"


# In[10]:


from mhs5200.Enums import Wave


# In[11]:


chan1.wave = Wave.SINE


# In[12]:


chan2.wave = Wave.SQUARE


# In[13]:


chan1.amplitude=20
chan2.amplitude=20


# In[ ]:


chan1.frequency="1kHz"


# In[ ]:


chan1.frequency="1 kHz"


# In[ ]:


chan1.frequency


# In[ ]:


for attr in dir(chan1):
    if attr.startswith("__"):
        continue
    if attr.startswith("_"):
        v = getattr(chan1, attr)
        print("{}: {}".format(attr, v))


# In[ ]:


chan1.duty_cycle


# In[ ]:


chan1._offset


# In[ ]:


chan1._phase


# In[ ]:


chan1._on


# In[ ]:


chan2._on


# In[ ]:


chan1._on=0


# In[ ]:


chan2._on=1


# In[ ]:


s = signal_generator.serial


# In[ ]:


cmd = "s1b0"

s.write((cmd+"\r\n").encode())


# In[ ]:


s.readline()


# In[ ]:


s.flushInput()


# In[ ]:


signal_generator._set(1, "on", 1)


# In[ ]:


s.readlines()


# In[ ]:


s.flushInput()


# In[ ]:


signal_generator._set(2, "on", 0)


# In[ ]:


s.readline()


# In[ ]:


chan1._on


# In[ ]:


chan1._on=0


# In[ ]:


signal_generator.send("r0c")[4:]


# In[ ]:


signal_generator.send("r1c")


# In[ ]:


signal_generator.send("r2c")


# In[ ]:


signal_generator.off()


# In[ ]:


f = ["1MHz", "1 MHz", "1kHz", "1 kHz"]


# In[ ]:





# In[ ]:


f[2].strip("MHz")


# In[ ]:





# In[ ]:




