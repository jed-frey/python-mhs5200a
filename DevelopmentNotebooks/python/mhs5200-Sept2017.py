#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '1')


# In[2]:


import serial
serial.__version__


# In[3]:


from mhs5200 import MHS5200


# In[4]:


get_ipython().run_line_magic('autoreload', '')


# In[14]:


signal_generator.serial.close()


# In[ ]:





# In[6]:


signal_generator = MHS5200('COM4')


# In[7]:


signal_generator.chan1


# In[8]:


signal_generator.chan2


# In[9]:


chan1 = signal_generator.chan1


# In[10]:


chan2 = signal_generator.chan2


# In[11]:


chan1.frequency="1kHz"


# In[12]:


chan1.frequency="1 kHz"


# In[13]:


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




