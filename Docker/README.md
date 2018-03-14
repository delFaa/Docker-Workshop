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
that the attendees should follow the Github page to guide them. The goal for the
course is to be as interactive and personal as possible.


## Resources
The resources for this part are a tutorial on how to install Docker, a list of
the basic commands, some exercises and an example of a Dockerfile.

### Installation
#### Linux
On a linux distribution Docker is as simple to install as using your package
manager:
  * **Ubuntu** : `sudo apt-get install docker`
  * **Archlinux** : `sudo pacman -S docker`

You could also install Docker manually, refer to the website for more info.

#### Windows
For windows, you can find the Docker community edition by following this link
and the instruction to install,
[download](https://store.docker.com/editions/community/docker-ce-desktop-windows).

#### Mac OS
For Mac, you can find the Docker community edition by following this link and
the instruction to install,
[download](https://store.docker.com/editions/community/docker-ce-desktop-mac).

### Commands
The commands displayed in the table below are the very basics that should be
explained, during this part of the workshop the attendees should probably not
play with more complex features, it will be discussed during the development
part. More in details descriptions will be given in the Github page, but the
attendees should be pushed towards the manual to research the full power of the
commands.

| **Commands** | **Descriptions**                                  |
|:------------:|:--------------------------------------------------|
| *pull*       | Pull an image on your local machine               |
| *run*        | Pull and run an image on your local machine       |
| *build*      | Create an image from a Dockerfile                 |
| *ps*         | List the containers on you system and their infos |
| *images*     | List the images on your system and their infos    |
| *rm*         | Remove a container from your system               |
| *rmi*        | Remove an image from your system                  |

### Dockerfile
Once again the goal is not to give a full course on the syntax of Dockerfile but
rather the basics, for that a small tutorial as been written in the Github page.

Following this link will guide you to a Dockerfile that can be used as a more
complex example, [link to the Dockerfile](./Dockerfile).

### Exercises
The exercices that follow are example of what could be given to the attendees
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

## Remove the existing images(s)
docker rmi NameOrIdImage

## Create, build and run a custom image with a Dockerfile based on "busybox" and
## make it output the sentence "I created my first custom image"
docker build -t MyImage .
```

---
[Home](../README.md) :
[previous](../Presentation/README.md) -
[next](../Development/README.md)
