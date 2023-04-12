#!/usr/bin/env python
# coding: utf-8

# ### Part II: Using Selenium

# ### Question 1: Google Search

# In[160]:


# Ensure that there are proper delays after each website interaction!


# In[161]:


# Get Selenium to work on my system
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# In[162]:


# Access the downloaded chromedriver.exe on macbook via document path
driver = webdriver.Chrome(executable_path='/Users/Administratoor/Documents/Winter/BAX 422 - Data Design & Representation/Class 5/chromedriver_mac_arm64/chromedriver')

# Specify the amount of time the webDriver should implicitly wait for an element to be found
driver.implicitly_wait(10)

# Set the amount of time that the script should wait during an execute_async_script call
driver.set_script_timeout(120)

# Sets the amount of time to wait for a page load to complete
driver.set_page_load_timeout(10)


# In[163]:


# Launch the website using the link provided
driver.get("https://google.com")

#         driver.find_element_by_class_name("className");
#         driver.find_element_by_css_selector".className");
#         driver.find_element_by_id("elementId");
#         driver.find_element_by_link_text("linkText");
#         driver.find_element_by_name("elementName");
#         driver.find_element_by_partial_link_text("partialText");
#         driver.find_element_by_tag_name("elementTagName");
#         driver.find_element_by_xpath("xPath");


# In[164]:


# Find the search box on Google via name="q"
search_bar = driver.find_element(By.NAME,"q")

# Enter the content we want to search
search_bar.send_keys("askew") 
time.sleep(0.5)

# Mimic a human clicking the ENTER buttom
search_bar.send_keys(Keys.ENTER) 
time.sleep(5)

# Clear the text in search box
# This step allows us to do separate searches, instead of searching for "askewgoogle in 1998" wrongly in the next step.
driver.find_element(By.NAME,"q").clear()
time.sleep(0.5)

# Close the window
# driver.close()
# driver.quit()


# In[165]:


# Separate searches on Google!
# Following the first search, perform a similar procedure for the second search.

# driver.get("https://google.com")

second = driver.find_element(By.NAME,"q") # identify search box

second.send_keys("google in 1998") # enter search text
time.sleep(0.5)

second.send_keys(Keys.ENTER) # perform Google search with Keys.ENTER
time.sleep(5)


# In[168]:


# Close the window
# driver.close()
driver.quit()

