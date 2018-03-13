# Presentation

## Introduction
The presentation part serve the purpose of breaking the ice and give the basics
of Docker. In practice, that means explaining the technology and give its
vocabulary for a better and smoother experience down the road.


## Plan
The plan for the presentation is to give a small preface to the workshop,
introduce the technology and define the inherent vocabulary of Docker.

To do that, a small PDF presentation has been written, it is mainly composed of
images to be as pleasing and captivating as possible. However, the text that is
associated with each slides is on this page, the purpose of this design choice
is to explain with telling pictures backed up by explanation from the person
giving the workshop.


## Resources
The only resources needed for the presentation are the text associated with each
slides and the slides themselves. I wanted this presentation to be as simple and
minimalistic as possible, but if you feel that a more complex one is preferable,
you should create one and share it. It's also good to notes that the following
texts are nothing more than ideas that should be adapted in function of the
public, plus I didn't include examples here but you should use some.

### Slides
#### What's Docker?
Docker is a technology that aims to simplify the developers and sysadmins lives
by providing a way to develop and deploy without extensive configuration of the
development and deployment environment.

#### Containers
A container is a process that is isolated from the rest of the system, but what
does that mean? Well your computers all run processes, like firefox, your text
editor or even the initialization of the computer. Those processes communicate
between eachothers, but what if you want a process that is isolated, well here
comes the concept of containers.

#### Images
An image in the world of Docker is very much like an ISO. Indeed, It's nothing
more than a bunch of dependencies and instructions bundled together in an easy
to reproduce package (containers). Ease of reproduction is the key here, one of
the goal of docker being the repeatability of any environment onto any system.

#### Dockerfile
A Dockerfile is like a recipe, it's the file in which you can define which
dependencies and instructions you want on your image. It follows a very simple
syntax which allows for the use of existing images to be called as well.

#### How does it works?
Knowing the meaning of key words to Docker is interesting, but how does it
works? Well with the help of a Dockerfile Docker is able to create an image,
with that image you can produce as many containers as you need and inside those
containers live all the process you require for your work.

#### What can you do with it?
Now, that all sounds good, but what can you use it for? Well, as mentioned
before, it can be used to create a development or deployment environment. It can
also be used to use utilities that should require plenty of dependencies without
having to install them onto your own system.

---
[Home](../README.md) :
[previous](../Presentation/README.md) -
[next](../Docker/README.md)
