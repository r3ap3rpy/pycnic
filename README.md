### Welcome 

This repository holds videos for my pycnic playlist on youtube.

In order to get started with this web framework you have to create a virtual environment and install the dependencies.

``` bash
virtualenv pynic
source pynic/bin/activate
pip install pycnic gunicorn requests
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

###### Third

To run this example you need to issue the following command.

``` bash
gunicorn error_handling:app
```

You can check the browser on the **http://127.0.0.1:8000/** link.