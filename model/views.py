import os
import docker
from docker import APIClient
from io import BytesIO

from django.http import JsonResponse, HttpResponseServerError

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

client = docker.from_env()

def create_image(request, model, path=None):
    if not path:
        path = BASE_DIR

    try:

        with open(path, 'r') as d:
            dockerfile = [x.strip() for x in d.readlines()]
            dockerfile = ' '.join(dockerfile)
            dockerfile = bytes(dockerfile.encode('utf-8'))

        f = BytesIO(dockerfile)

        # Point to the Docker instance
        cli = APIClient(base_url='tcp://192.168.99.100:2376')

        response = [line for line in cli.build(
            fileobj=f, rm=True, tag=model
        )]

        return JsonResponse({'image': response})
    except:
        return HttpResponseServerError()

def create_container(request, code):
  client.create_container(
       image='python:3',
       command=['python','-c', 'my_code.py'],
       volumes=['/opt'],
       host_config=client.create_host_config(
           binds={ os.getcwd(): {
               'bind': '/opt',
               'mode': 'rw',
               }
           }
       ),
       name='predicting-altruism',
       working_dir='/opt'
  )

def run_container(request):
    client.containers.run("predicting-altruism", detach=True)
    return None