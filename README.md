# Medical Treatments Storage

## Tech Stack

1. Backend: Python, FastApi
1. Frontend: Angular + Material
1. DB: MongoDB
1. Infrastructure: K8S + Docker + Minikube (for the local launch)

## Installation

For the installation, you'll need Docker and Minikube installed. Ensure that you're running docker daemon.

Use `$ make init` command to initialize minikube cluster and install all the deps.

## Dev installation

To install server: `$ cd server && make install`

To run server: `$ cd server && make run`

## Accessing the app

1. Access the app: `$ make url` to run a proxy (don't close terminal window) and access the given URL. Swagger and ReDoc work fine.
1. Access Minikube Dashboard: `$ make dash`. The Dashboard will open automatically. 

### Local instance:

1. **Swagger:** http://127.0.0.1:8000/docs
1. **ReDoc:** http://127.0.0.1:8000/redoc
