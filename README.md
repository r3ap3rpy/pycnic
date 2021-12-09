### Welcome 

This repository holds videos for my pycnic playlist on youtube.

The official documentation can be found [here](http://pycnic.nullism.com/).

In order to get started with this web framework you have to create a virtual environment and install the dependencies.

``` bash
virtualenv pynic
source pynic/bin/activate
pip install pycnic gunicorn requests sqlalchemy
```

##### First

You can execute the hello world example the following way.

``` bash
gunicorn hello_world:app
```

Using another terminal you can send post requests aswell to the **http://127.0.0.1:8000/** context route.

``` python
import requests
requests.post(url="http://127.0.0.1:8000/").text
#'{"message": "Thank you for your POST request!"}'
```

##### Second

You can run the second example with the following command.

``` bash
gunicorn request_data:app
```

Send your request the following way.

``` python
import requests
requests.post(url="http://127.0.0.1:8000/?arg=asdasd&arg2=asdasda",data=json.dumps({"a":"b"})).text
#'{"request_data": {"a": "b"}, "ip": "127.0.0.1", "method": "POST", "args": {"arg": "asdasd", "arg2": "asdasda"}, "json_args": {}, "header": null, "a": "b"}'
```

##### Third

To run this example you need to issue the following command.

``` bash
gunicorn error_handling:app
```

You can check the browser on the **http://127.0.0.1:8000/** link.

##### Fourth

To run this example use this command.

``` bash
gunicorn custom_error:app
```

After visiting the browser you should see this raw data.

``` bash
{"error": "This is my own custom error class!", "data": {"my_error_key": "my_error_value"}, "status_code": 469, "status": "469 Custom Error"}
```

##### Fifth

To run this example use this command.

``` bash
gunicorn cookie_demo:app
```

In order to try this out spin up a console and issue the following in python.

``` python
import requests
# Check the cookies sent by the client.
requests.get(url = "http://127.0.0.1:8000/", cookies={ "My gift is this" : "Cookie" }).text
# Send cookies to the API
requests.post(url = "http://127.0.0.1:8000/").cookies
```

##### Sixth

In order to run this example issue the following.

``` bash
gunicorn validation:app
```

To test it out spin up a python console and execute the following.

``` python
import requests, json
# before
requests.post(url="http://127.0.0.1:8000/before",data=json.dumps({'name':'Daniel'})).text
# decorator
requests.post(url="http://127.0.0.1:8000/decorator",data=json.dumps({'name':'Daniel'})).text
```

##### Seventh

In order to run this demo issue the following.

``` bash
gunicorn auth_wrapper:app
```

After visiting the **http://127.0.0.1:8000/** you should get the following response.

``` python
import requests
requests.get(url="http://127.0.0.1:8000/").text
# {"welcome": "administrator"}
```

##### Eighth

More info about [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

In order to run the example you need to issue the following command.

``` bash
gunicorn cors:app
```

To check the output issue the following command from a python console.

``` python
import requests
requests.get(url="http://127.0.0.1:8000/").text
# {"message": "CORS is working!", "origin": null}
```