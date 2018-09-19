
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
import pandas as pd


# In[15]:


get_ipython().magic('matplotlib inline')


# In[16]:


recent_grads = pd.read_csv("recent-grads.csv")


# In[17]:


print(recent_grads.iloc[0])


# In[42]:


print(recent_grads.head())
print(recent_grad.count())


# In[19]:


print(recent_grads.describe())


# In[21]:


recent_grads = recent_grads.dropna()


# In[22]:


print(recent_grads)


# In[23]:


print(recent_grads.dropna())


# In[34]:


print(recent_grads["Rank"].value_counts)


# In[35]:


print(recent_grads.dropna() == True)


# In[37]:


print(recent_grads.iloc[0])


# In[39]:


recent_grads.dropna(inplace= True)

print(recent_grads)
# In[40]:


print(recent_grads)


# In[41]:


print(recent_grads.count())


# In[43]:


print(recent_grads.describe())


# In[44]:


cleaned_data_count = recent_grads.count()
print(cleaned_data_count)


# In[45]:


get_ipython().magic('matplotlib inline')


# In[46]:


print(recent_grads.columns)


# In[58]:


ax1 = recent_grads.plot(x="Women" , y="Median" ,kind = "scatter")
plt.show()


# In[63]:


ax2 = recent_grads["Employed"].hist(bins = 25, range = (0,5000))
plt.show()


# In[65]:


from pandas.plotting import scatter_matrix


# In[66]:


ax3 = scatter_matrix(recent_grads[["Sample_size", "Median"]], figsize = (10,10))


# In[67]:


ax4 = scatter_matrix(recent_grads[["Sample_size", "Median", "Unemployment_rate"]], figsize = (10,10))


# In[71]:


ax5 = recent_grads["ShareWomen"].sort_values()


# In[72]:


print(ax5)


# In[73]:


ax6 = recent_grads.plot(x=recent_grads["Women"][:10], y = recent_grads["Women"].tail(10), kind = "bar")

