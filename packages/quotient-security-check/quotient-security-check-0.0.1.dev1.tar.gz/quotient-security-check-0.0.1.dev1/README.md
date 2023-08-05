Check Whitelisted IP
=============

This is a simple security package to check whether client IP is allowed to access the flask`s backend APIs.


Setup
=====
``` python
from flask import Flask
from security.check_ip import IPCheck

# Initialize the Flask app
app = Flask(__name__)

# import IP_list from the config file or declare it here

ip_list = <>

"""Set up IPCheck, there is no need to pass third argument which is "logging_enabled"
By default it is set to false, but if you want to see the incoming request IP then make it true, and it will
be printed in the log

optional
----------
IPBlock(app, ip_list, logging_enabled=True)
"""

ipcheck= IPBlock(app, ip_list)
```