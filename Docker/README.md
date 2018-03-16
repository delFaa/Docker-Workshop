# Docker

## Introduction
This would be the first interactive part, the idea here being to play with
simple container built from images like **busybox**, but also to be able to
create customized images and understand the core concept of Docker like the
isolation of containers from the system, their destructibility and their
flexibility.

## Plan
The plan for the initiation to Docker is to first install Docker, learn the 
basic commands, play with a container and create a Dockerfile. To achieve all
that the attendees should follow the Github page to guide them. The goal for
this part is to be as interactive and personal as possible.


## Installation
The install is the time to setup the machines all the participants for Docker
use. All the details can be found on the install section of the Github page.


## Commands
The commands displayed in the table below are the very basics that should be
explained, during this part of the workshop the attendees should probably not
play with more complex features, it will be discussed during the development
part. The attendees should be pushed towards the manual to research the full
power of the commands.

| **Commands** | **Descriptions**                                  |
|:------------:|:--------------------------------------------------|
| *pull*       | Pull an image on your local machine               |
| *run*        | Pull and run an image on your local machine       |
| *build*      | Create an image from a Dockerfile                 |
| *ps*         | List the containers on you system and their infos |
| *images*     | List the images on your system and their infos    |
| *rm*         | Remove a container from your system               |
| *rmi*        | Remove an image from your system                  |


## Dockerfile
The goal, during this part, is not to give a full course on Dockerfile but
rather the very basics in order for the attendees to have a first encounter with
the customisation of images before we go further in the development part.


## Exercises
The exercices that follow are examples of what could be given to the attendees
for them to practice and learn by mistakes and research.

```bash
## Pull the image "busybox"
docker pull busybox

## List the existing image(s)
docker images

## Run the image "hello-world"
docker run hello-world

## List all the existing container(s)
docker ps -a

## Run a container "busybox" with an interactive terminal
docker run -it busybox

## Run a container "busybox" with an interactive terminal and the current
## directory as mounted volume inside the "test" directory of the container
docker run -it -v $PWD:/test busybox

## Remove the existing container(s)
docker rm NameOrIdContainer

## Remove the existing image(s)
docker rmi NameOrIdImage

## Create, build and run a custom image with a Dockerfile based on "busybox" and
## make it output the sentence "I created my first custom image"
docker build -t myimage . && docker run myimage
```

```
## Dockerfile from the last command exercise
FROM busybox
CMD echo "I created my first custom image"
```


## Play time
If the attendees have finished the exercises before the end of this part they
should be left to play with what they've acquired and explore the development
part in advance.

---
[Home](../README.md) :
[previous](../Presentation/README.md) -
[next](../Development/README.md)
