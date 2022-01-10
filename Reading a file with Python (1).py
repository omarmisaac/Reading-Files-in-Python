#!/usr/bin/env python
# coding: utf-8

# # Reading Files

# ### Downloading Data

# In[2]:


import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)


# In[3]:


# Download Example file


get_ipython().system('wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt')


# <hr>
# 

# <h2 id="read">Reading Text Files</h2>
# 

# The mode argument is optional and the default value is **r**. In this notebook we only cover two modes:
# 
# <ul>
#     <li>**r**: Read mode for reading files </li>
#     <li>**w**: Write mode for writing files</li>
# </ul>
# 

# In[5]:


# Read the Example1.txt

example1 = "Example1.txt"
file1 = open(example1, "r")


# The name of the file:
# 

# In[6]:


file1.name


# The mode the file object is in:
# 

# In[7]:


file1.mode


# Reading the file and assign it to a variable :

# In[8]:


# Read the file

FileContent = file1.read()
FileContent


# In[9]:


print(FileContent)


# The file is of type string:
# 

# In[10]:


type(FileContent)


# In[12]:


# Close file after finish
file1.close()


# <hr>
# 

# <h2 id="better">A Better Way to Open a File</h2>
# 

# In[13]:


# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)


# In[14]:


# Verify if the file is closed
file1.closed


# We can see the info in the file:
# 

# In[15]:


# See the content of file
print(FileContent)


# In[16]:


# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))


# In[17]:


# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))


# We can also read one line of the file at a time using the method <code>readline()</code>:
# 

# In[19]:


# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())


# We can also pass an argument to <code> readline() </code> to specify the number of charecters we want to read. However, unlike <code> read()</code>, <code> readline()</code> can only read one line at most.
# 

# In[20]:


with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# We can use a loop to iterate through each line:
# 

# In[22]:


# Iterate through the lines

with open(example1,"r") as file1:
        #i = 0;
        for line in file1:
            print( line)
           # i = i + 1


# In[24]:


# Read all lines

with open(example1, "r") as file1:
    FileasList = file1.readlines()

