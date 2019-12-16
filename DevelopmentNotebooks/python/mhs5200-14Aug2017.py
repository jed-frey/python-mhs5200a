#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '1')


# In[3]:


import serial
serial.__version__


# In[4]:


from mhs5200 import MHS5200, uuid


# In[5]:


get_ipython().run_line_magic('autoreload', '')
uuid


# In[6]:


signal_generator = MHS5200('COM12')
chan1 = signal_generator.channels[0]
s = signal_generator.serial


# In[7]:


chan1.frequency


# In[8]:


chan1.frequency=1


# In[9]:


chan1.amplitude


# In[10]:


chan1.amplitude=20

