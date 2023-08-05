# Flask App

Simple multi staged dockerized flask Rest API project.

## Getting Started

Follow these steps to get your project up and running.

### Building the Docker Image

```
   docker build --build-arg BASE_IMG=python:3.11.4-alpine3.17 -t flask-app:latest .
```

### Run the Project
```
   docker run --rm --name app -p "8080:8080" flask-app
```
