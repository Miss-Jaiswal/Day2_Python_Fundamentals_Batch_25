#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Introduction to list

students=["shraddha","shruti","shreya","raman","priya","rhuddhi","akshitha","trupti","manali"]
print(students)


# In[2]:


type(students)


# In[12]:


#To access particular name from the list
print(students[1])
print(students[8])
print(students[5])
print(students[6])
print(students[-2])
print(students[0])


# In[24]:


#req1:-To add new elements in the list
students.append("Dhanashree")
print(students)


# In[25]:


students.append("Neha")
print(students)


# In[27]:


students.append("vaibhav")
print(students)


# In[28]:


students.append("Aniket")
print(students)


# In[32]:


#req2:-To add a students on custom index position of a choice
students.insert(-2,"Sainath")
print(students)


# In[33]:


students.insert(12,"Nikhil")
print(students)


# In[35]:


#req3:-To delete the element from the list
del students[13]
print(students)


# In[37]:


#req4:- To delete list
del students
print(students)

