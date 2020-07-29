#!/usr/bin/env python
# coding: utf-8

# In[4]:


#List data types
students=["shraddha","shruti","shreya","raman","priya","rhuddhi","akshitha","trupti","manali"]
type(students)


# In[10]:


print(f"Keep up the good work , {students[1].title()}.") 


# In[11]:


print(f"Keep up the good work , {students[2].title()}.") 


# In[12]:


print(f"Keep up the good work , {students[0].title()}.") 


# In[14]:


print(f"Keep up the good work , {students[3].title()}.") 


# In[15]:


print(f"Keep up the good work , {students[-1].title()}.") 


# In[18]:


#Introduction to for loop
#implementation of for loop
for x in students:
    print(f"Keep up the good work , {x.title()}.") 
    #----->we can use any temp variable in place of x


# In[19]:


#further enhancement in code.
for x in students:
    print(f"Keep up the good work , {x.title()}.") 
    print(f"I will be looking forward to recieve your file of today , {x.title()}.")


# In[22]:


#Using \n delimileter
for x in students:
    print(f"Keep up the good work , {x.title()}.") 
    print(f"I will be looking forward to recieve your file of today , {x.title()}.\n")
# the for loop is also called as iteration over the elements.


# In[ ]:




