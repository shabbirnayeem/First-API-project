# First-API-project
100daysofcode-day52_53


Working with API
What is API?
An application programming interface. Basically API is an messagener that takes your request and reponse to you with you with whatever you asked for.
There are tons of API's some are free for developers to use and some you have pay for. Alots paid API's comes for free tire versions.

My first time learning about API and acctully using to connect with a API system and make request. I am using python very popular API modules "requests"

What is requests?
Requests is a Python HTTP library, released under the Apache License 2.0. The goal of the project is to make HTTP

API's have four different functions:
  - GET: requests.get() : get data
  - Post: requests.post(): post something via API, like post on twitter
  - PUT: requests.put(): update something
  - DELETE: requests.delete() 

What is API parameters?
  - API parameters are the variable parts of a resource. They determine the type of action you want to take on the resource.
  - Different API requires different types of parameters.
  - Paramets are like python dictionaries, it has a key and a value.
    - the key must match with the key the API requires

# server response code summary
    # 1XX: Hold On
    # 2XX: Here You Go [everything is ok, successful]
    # 3XX: Go Away [You don't permission to access]
    # 4XX: You Screwed up or the thing you are looking for doesn't exits
    # 5XX: THe server Screwed up [server down, or website down]

EOD project
- I will using Pyhon request module and Open APIs From Space API to when a email to myself when International Space Station (ISS) is where I am located.
- Also using the "Sunset and sunrise times API" to determine night and day. B/c the ISS can only be seen at night.
- Sending email using the python smtplib module

What is Open APIs From Space?
From the website: "Open Notify is an open source project to provide a simple programming interface for some of NASA’s awesome data. I do some of the work to take raw data and turn them into APIs related to space and spacecraft."

What is Sunset and sunrise times API?
"We offer a free API that provides sunset and sunrise times for a given latitude and longitude."
You can deptermine sunset or sunrise by passing in latitude and longitude.
