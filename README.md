### Welcome 

This repository holds videos for my pycnic playlist on youtube.

In order to get started with this web framework you have to create a virtual environment and install the dependencies.

``` bash
virtualenv pynic
source pynic/bin/activate
pip install pycnic gunicorn requests
```

You can execute the hello world example the following way.

``` bash
gunicorn hello_world:app
```

Using another terminal you can send post requests aswell to the **http://127.0.0.1:8000/** context route.

``` bash
import requests
requests.post(url="http://127.0.0.1:8000/").text
#'{"message": "Thank you for your POST request!"}'
```
