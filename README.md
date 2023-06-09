# **API-scraping-Demo**

This is the demonstration showing how the LinkedIn data breach has occured
It's done by using third party API scraping and retrieving data illegally
Here we are going to display the data on the localhost api endpoint.
And retrieval is done when there is no security.
And demo is done to show that there are errors when security measures like Authentication APIs ans Rate Limiting are implemented


## There are five files
userdata.py has the profile_details data with Name, Email, etc.
retrievaldata.py will rerieve the requests module in python

Rate Limit will limit the number of times the data is being accessed in a time period.
Well, it is essential but still the attackers may be able to access it. (ratelimit.py)

(Authentication.py) will ask anyone requesting for data an API key, then only if we enter the correct one will we be able to se the data.
So this is an increment to current security measures and may increase authorization.

