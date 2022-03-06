# Docker
- Docker helps with building, running and deploying applications on any machine running docker
- Docker achieves this with the help of containers which is an isolated environment

# Container vs Virtual Machine
## Container
- An isolated environment for running an application
- Sits on top of the OS
- Lightweight, needs less hardware resources

## Virtual Machine
- It acts like a seperate whole machine with an OS of your choice
- Sits on top of the hardware 
- Heavy and resource intensive

# Docker architecture
- Docker works with in two models client side and server side
- The server is daemon(background service/process) in your local machine

# Example
- Add a `dockerfile` in the project directory
```
FROM node:alpine
COPY . ./app
WORKDIR /app
CMD node app.js
```

- Then run the following command to build the image with a tag(-t) and the path to the dockerfile
```
docker build -t hello-docker .
```

- To view all the images created by docker
```
docker images
```

- To run the docker
```
docker run hello-docker
```

- To pull an image from dockerhub
```
docker pull jobin/hello-docker
```
