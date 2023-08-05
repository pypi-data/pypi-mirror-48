Check Whitelisted IP
=============

This is a simple security package to check whether client IP is allowed to access the flask`s backend APIs.

Before every endpoint is served, it will check for the remote IP if it exists in the list of white listed IPs, it it exists, it returns the response otherwise throws abort error:

```
HTTPErr: 403 Abort
```


Setup
=====
``` python
from flask import Flask
from security.check_ip import IPCheck

# Initialize the Flask app
app = Flask(__name__)

# import IP_list from the config file or declare it here

ip_list = <>

ipcheck= IPCheck(app, ip_list)

```


Nginx Routing
====

By default headers of the incoming request gets updated with localhost IP when it is passed to the backend Nginx server.
In order to get the real IP of the client/LAN, we need to do following configurations in the nginx config:

```
server {
    real_ip_recursive on;
}

location / {
    proxy_set_header  Host $host;
    proxy_set_header  X-Real-IP $remote_addr;
    proxy_set_header  X-Forwarded-For $remote_addr;
    proxy_set_header  X-Forwarded-Host $remote_addr;
   }
   
```

**sample incoming request header dict after naking above changes in Nginx**
```
{'wsgi.version': (1, 0), 'wsgi.url_scheme': 'http', 
'wsgi.input': '<_io.BufferedReader name=5>', 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>,
'wsgi.multithread': True, 
'wsgi.multiprocess': False, 'wsgi.run_once': False, 
'werkzeug.server.shutdown': <function WSGIRequestHandler.make_environ.<locals>.shutdown_server at 0x7fba5d1bd598>, 
'SERVER_SOFTWARE': 'Werkzeug/0.14.1', 'REQUEST_METHOD': 'GET', 'SCRIPT_NAME': '', 'PATH_INFO': '/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': 39534, 'SERVER_NAME': '127.0.0.1', 'SERVER_PORT': '8002', 'SERVER_PROTOCOL': 'HTTP/1.0', 
'HTTP_HOST': '172.30.1.23', 
'HTTP_X_REAL_IP': '10.21.120.11', 
'HTTP_X_FORWARDED_FOR': '10.21.120.11', 
'HTTP_X_FORWARDED_HOST': '10.21.120.11', 
'HTTP_CONNECTION': 'close', 'HTTP_PRAGMA': 'no-cache', 
'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36', 
HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 
'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_ACCEPT_LANGUAGE': 'en-GB,en-US;q=0.9,en;q=0.8', 'werkzeug.request': <Request 'http://10.21.120.11/' [GET]>}

```