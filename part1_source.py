#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NOTE: Set the full user agent in all of your requests.
# (e.g., “Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56”) 



### Part I: FlightAware Logging In

from bs4 import BeautifulSoup
import requests
import time

# 1. Access the URL using a standard GET request
session_requests = requests.session()

URL = "https://www.planespotters.net/user/login"
page1 = session_requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
page1

# Read and store the cookies received in the GET request response
cookies1 = session_requests.cookies.get_dict()
cookies1

# Parse the response
doc1 = BeautifulSoup(page1.content, 'html.parser')

# Read and store to a string variable the value of hidden inputs
input1 = doc1.select("div.planespotters-form input[name=csrf]")[0]
input2 = doc1.select("div.planespotters-form input[name=rid]")[0]

# Obtain hidden input values including csrf & rid
csrf = input1.get("value")
rid = input2.get("value")

# Print the stored values
print(csrf)
print(rid)

# 2. Make a post request using the cookies from (1) as well as all required name-value-pairs
respond = session_requests.post(URL, data = {"username" : "lucytest", # your username here
                                              "password" : "bax422", # your password here
                                              "csrf" : csrf, 
                                              "rid" : rid},
                                 cookies = cookies1,
                                 headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})

# 3. Get the cookies from the response of the POST request
cookies2 = session_requests.cookies.get_dict()
cookies2

# The two cookies are different in variable value; Replace the old one with the new one...
# Add cookies2 to cookies1?
# print(cookies2)

# Remain Logged in the website using the updated cookies (may skip these step; tried and successfully logged in without running this line of code)
page2 = session_requests.get(URL, cookies=cookies2, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
page2

# Always pause between two requests
time.sleep(5)

# 4. Verify that I am logged in by accessing the profile page with the saved cookies
profile_url = "https://www.planespotters.net/member/profile"

session_requests = requests.session()

page3 = session_requests.get(profile_url, cookies = cookies2, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
page3

# 5A. Print out the entire BeautifulSoup document of my profile page
doc3 = BeautifulSoup(page3.content, 'html.parser')
doc3

# 5B. Print out all cookies from previous steps
print(cookies1)
print(cookies2)

# 5C. Print a boolean value to show that my username is contained in the document of my profile page
print(bool(doc3.findAll(text = "lucytest")))
print(bool(doc3.select(":contains(lucytest)")))

# If boolean method does not work.... may choose to directly select the username from html content
# list_of_contents = doc3.select("     ")

