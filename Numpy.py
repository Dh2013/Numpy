#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3,4,5,6])


# In[3]:


a


# In[5]:


np.array([[1,2],[3,4],[5,6]])


# In[6]:


np.array([1,2,3],"complex")


# In[7]:


np.array((1,2,3))


# In[8]:


np.arange(1,10)


# In[9]:


np.arange(3.0)


# In[10]:


np.arange(1,10,2)


# In[11]:


np.arange(20,dtype= "complex")


# In[12]:


np.arange(1,10,2,dtype="float")


# In[13]:


np.zeros(5)


# In[14]:


np.zeros(3,dtype="int")


# In[15]:


np.zeros((2,3))


# In[16]:


np.zeros([3,4])


# In[17]:


np.zeros(4,order="F")


# In[18]:


np.zeros((3,4),order="F")


# In[19]:


np.ones(8)


# In[20]:


np.ones(7,dtype="int")


# In[21]:


np.ones((3,4))


# In[22]:


np.empty(6)


# In[24]:


np.linspace(3,5)


# In[26]:


np.linspace(1,100,num=5)


# In[27]:


np.linspace(1,100,num=4,retstep=True)


# In[28]:


np.linspace(1,100,num=5,endpoint=False)


# In[29]:


np.linspace(1,100,num=4,dtype=int)


# In[30]:


np.linspace(1,100)


# In[31]:


np.eye(5)


# In[32]:


np.eye(2,3)


# In[38]:


np.eye (4,k=-1)


# In[39]:


np.eye (5, k=2)


# In[40]:


np.random.rand(5)


# In[41]:


np.random.rand(4,5)


# In[42]:


np.random.randn(5)


# In[43]:


a = np.array([1,2,3,4])


# In[44]:


a.ndim


# In[46]:


b=np.array([[1,2],[3,4]])


# In[47]:


b.ndim


# In[48]:


a=np.zeros(5)


# In[49]:


a


# In[50]:


a.shape


# In[51]:


a=np.array([[1,2],[3,4]])


# In[52]:


a.shape


# In[53]:


c=np.zeros((2,3,4))


# In[54]:


c.shape


# In[55]:


c.size


# In[56]:


a.size


# In[57]:


c.dtype


# In[58]:


a.dtype


# In[59]:


c.itemsize


# In[60]:


a.itemsize


# In[61]:


a=np.array([1,2,3,4,5,6,7,8,9])


# In[62]:


a


# In[63]:


a[5]


# In[64]:


a[3]


# In[65]:


a[-5]


# In[66]:


a[-2]


# In[67]:


n= np.array([[1,2],[3,4]])


# In[68]:


n


# In[71]:


n[0] [1]


# In[72]:


n[-2] [-2]


# In[73]:


a = np.array([1,2,3,4,5])


# In[74]:


a


# In[75]:


a[1:5]


# In[76]:


a[:]


# In[77]:


a[1::2]


# In[78]:


a[:3]


# In[79]:


a = np.arange(1,10)


# In[80]:


index=np.array([1,4,5])


# In[81]:


a[index]


# In[92]:


v = np.array([[1,2,-3],[4,-5,6],[7,8,9]])


# In[93]:


v[[0,2],[2,0]]


# In[94]:


v[[1,1,2],[0,2,1]]


# In[95]:


v[v<0]


# In[96]:


b[b>0]


# In[97]:


v[v<0]*2


# In[98]:


v+2


# In[99]:


v*3


# In[100]:


v/2


# In[101]:


v-1


# In[102]:


v**2


# In[103]:


v


# In[104]:


n


# In[105]:


b


# In[106]:


a


# In[107]:


v+b


# In[110]:


v*b


# In[111]:


v%b


# In[112]:


v/b


# In[113]:


v-b


# In[114]:


a = np.arange(10)


# In[115]:


a


# In[116]:


a.shape


# In[117]:


b = np.reshape(a, (5,2))


# In[118]:


b


# In[119]:


b.shape


# In[120]:


b = np.reshape(a, (5,2), order="F")


# In[122]:


b


# In[ ]:




