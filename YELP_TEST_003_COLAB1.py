
# coding: utf-8

# In[1]:


#import dependencies
import json
import pprint
import requests
import sys


# In[2]:


def milestometers(num_miles):
    #mtm = 1.609 * num_miles
    mtm = 1609.34 * num_miles
    mtm = int(mtm)
    return mtm


# In[3]:


#testing miles to meters
#https://stackoverflow.com/questions/6569528/python-float-to-int-conversion/6569577
#print(round(milestometers(2),0))
num_meters = milestometers(2)
print(f'{num_meters}')


# In[4]:


API_KEY="YOUR API KEYHERE"

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


# In[5]:


term = 'Restaurants'
location = 'Irvine, California'
SEARCH_LIMIT = 10

#set the search radius equal to 2 miles around the location
SEARCH_RADIUS = milestometers(2)

url = 'https://api.yelp.com/v3/businesses/search'

headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),
    }

url_params = {
                'term': term.replace(' ', '+'),
                #'location': location.replace(' ', '+'),
                'latitude': '33.640495',
                'longitude': '-117.844296',
                'radius': SEARCH_RADIUS,
                'limit': SEARCH_LIMIT
            }
response = requests.get(url, headers=headers, params=url_params)
print(response)
print(type(response.text))
print(response.text[:1000])


# In[6]:


yelp_info = response.json()


# In[7]:


#print out json file
print(json.dumps(yelp_info, indent=4, sort_keys=True))


# In[8]:


for x in yelp_info:
    print(x)


# In[9]:


for x in yelp_info["businesses"]:
    print(x)


# In[10]:


for x in yelp_info["businesses"]:
    print(x["name"])

