### Python Mexico

Exploratory Django wrapper around docker-py for:
- Creating Docker image with Jupyter notebook
- Running Docker container

For more information on how to setup a Dockerfile for a Jupyter notebook with a mountable data volume read [here](https://github.com/lorenanicole/jupyter_docker).

#### Install the app

```
virtualenv -p python3 venv
source venv/bin/activate
(venv) pip3 install -r requirements
(venv) python3 manage.py runserver
```

To create an image call `http://localhost:8000/api/model/create/imagename`, updating the `model.views` `create_image` endpoint with a URL for instance of Docker.

Slides for talk [here](http://bit.ly/2s5R01V)
