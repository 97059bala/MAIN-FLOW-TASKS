#!/usr/bin/env python
# coding: utf-8

# In[2]:


#creating a list
list=[20,13,29,17,18]

#Printing Original list
print("Original list",list)

#Perform basic operations
#adding an element in the list
list.append(14)

#removing an element from the list
list.remove(29)

#Modify an element in the list
list[1]=27

print("Updated list:",list)


# In[6]:


#Creating a dictionary
dict={'name':'Cherry','age':20,'place':'Uravakonda','Pincode':515812}

#Printing Original Dictionary
print("Original Dictionary:",dict)

#Adding an element in the dictionary
dict['gender']='Female'

#Removing an element in the dictionary
del dict['age']

#Modifying an element in the dictionary
dict['Place']='Madanapalle'

#Printing Updated Dictionary
print('Updated Dictionary:',dict)


# In[8]:


#Creating a set
set={56,78,90,22,21}

#printing original set
print("Original Set:",set)

#Adding an element in the set
set.add(32)

#Removing an element from the set
set.remove(90)

#Modifying an element from the set
set.discard(56)
set.add(10)

#Printing Updated Set
print('Updated Set:',set)


# In[ ]:




