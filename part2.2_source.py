#!/usr/bin/env python
# coding: utf-8

# ### Part II: Using Selenium

# ### Question 2: Bestbuy "Deal of the day"

# In[11]:


# Ensure that there are proper delays after each website interaction!


# In[12]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# In[13]:


# Use Selenium to invoke the executable file which will then invoke an actual browser
driver = webdriver.Chrome(executable_path='/Users/Administratoor/Documents/Winter/BAX 422 - Data Design & Representation/Class 5/chromedriver_mac_arm64/chromedriver')

# driver.implicitly_wait(10)
# driver.set_script_timeout(120)
# driver.set_page_load_timeout(10)


# In[14]:


# Launch a new website
driver.get("https://www.bestbuy.com")


# In[15]:


# Click on "Deal of the Day" buttom on the webpage
deal_of_day = driver.find_element(By.XPATH, "//a[@data-lid='hdr_dotd']")
deal_of_day.click()

time.sleep(5)


# In[16]:


# Read and print to screen how much time is left for the Deal of the Day (1)
count_down = driver.find_element(By.CLASS_NAME, "sr-only.sale-timer")
print(count_down.text)

time.sleep(0.5)


# In[17]:


# Read and print to screen how much time is left for the Deal of the Day (2)
clock_hrs = driver.find_element(By.XPATH, "//span[@class='hours cdnumber']")
clock_min = driver.find_element(By.XPATH, "//span[@class='minutes cdnumber']")
clock_sec = driver.find_element(By.XPATH, "//span[@class='seconds cdnumber']")

# A more accurate time of the countdown clock
print(clock_hrs.text + ":" + clock_min.text + ":" + clock_sec.text)

time.sleep(0.5)


# In[18]:


# Click on the actual product of "Deal of the Day"
deal_product = driver.find_element(By.CLASS_NAME, "wf-offer-link.v-line-clamp")
deal_product.click()

time.sleep(5)


# In[19]:


# Find the reviews part, which is the fourth element on the selected list
elements = driver.find_elements(By.XPATH,"//span[@class='c-accordion-trigger-label']")
product_reviews = elements[3]
time.sleep(5)

# Note that:
# overview = driver.find_element(By.XPATH,"//span[@class='c-accordion-trigger-label']")
# This line of code actually finds the "Overview", not the "Reviews" on the product page!
# That's why we select from a list of elements above.


# In[21]:


# Then, click on reviews
product_reviews.click()
time.sleep(5)

# Click again to show reviews results
product_reviews.click()


# In[22]:


# Obtain the current url with webdriver
get_url = driver.current_url
print("The current url is: " + str(get_url))


# In[23]:


# Access the current webpage via url
import requests
page = requests.get(get_url, headers={"User-Agent": "Mozilla/5.0"})


# In[24]:


# Save the resulting HTML to local hard drive
with open('bestbuy_deal_of_the_day.htm', 'wb') as file: 
    file.write(page.content) 
    time.sleep(5) # give a 5 second pause after each page request
    file.close()


# In[25]:


driver.quit()

