#!/usr/bin/env python
# coding: utf-8

# In[8]:


for i in range (2,100):
    a=0
    for j in range (2,i-1):
        if not(i%j):
            a=1
            break
    if(a==0):
        print(i,' ')


# In[ ]:




