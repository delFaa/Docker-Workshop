# Docker Workshop

![alt text](~/Images/docker.png "Docker")

## Introduction
This repository is a guideline to give a workshop on Docker, the goal being to
introduce **Docker** and explain it's importance on **development environment**
and **deployment**. The purpose for the attendees being to grasp the reason of
Docker success and understand how it simplify the development process as well
as the deployment of any, small or big, application.

To do all this, resources such as exercises, examples and small tutorial have
been put together in this repository. If you don't know Docker, these resources
can also be used for self-learning.

Small disclaimer, as we live in a dangerous world, I will protect myself by
stating that this workshop doesn't claim to be 100% accurate nor do I claim to
be an expert, moreover if you want to help me improve this course you are more
than welcome to contribute to it.


## Timetable
The workshop is designed to take a day of work, the idea being not to drawn in
theory and demonstration but rather to practice and understand by failure and
success.

| **Time** | **Content**                  |
|:--------:|:-----------------------------|
| *09:00*  | Welcome everyone             |
| *09:10*  | Presentation of the workshop |
| *09:30*  | Initiation to Docker         |
| *10:45*  | _Small break_                |
| *11:00*  | Development environment      |
| *12:30*  | _Lunch break_                |
| *13:30*  | Development environment      |
| *15:00*  | _Small break_                |
| *15:15*  | Deployment                   |
| *16:30*  | Conclusion                   |

For an in detail explanation of what will be done please refer to the content of
the workshop section.


## Content of the Workshop

### Presentation (20 min)
The presentation part serve the purpose of breaking the ice and give the basics
of Docker. In practice, that means explaining the technology and give its
vocabulary for a better and smoother experience down the road.
[Check the resources](./Presentation/README.md).

### Docker (75 min)
This would be the first interactive part, the idea here being to play with
simple container built from images like **busybox**, but also to be able to
create customized images and understand the core concept of Docker like the
isolation of containers from the system, their destructibility and their
flexibility.
[Check the resources](./Docker/README.md).

### Development environment (180 min)
The development environment part should be focused on how to create, configure
and use custom images. All that to end up with an appropriate and working
environment tailored for ones need. Which would demonstrate the potential of 
simplification of the development process. It's also important, during this 
phase, to emphasise the separation of service in different containers and 
therefore introduce **docker-compose** as a tool to bind an application
together.
[Check the resources](./Development/README.md).

### Deployment (75 min)
For this last interactive part the challenge would be to deploy a small project
with the help of Docker. The goal being to demonstrate the ease of not having to
configure the server since the custom image for the development environment and
the deployment environment are one and the same.
[Check the resources](./Deployment/README.md).

### Conclusion (30 min)
To finish the workshop I advice for a small discussion/debate between everyone
on what as been learned, how it might be useful and how they plan to use it or
not. That conclusion should, in my opinion, close the workshop in such a way
that everyone has more than his/her own opinion on the technology. It would also
serve the purpose of giving a feedback on the workshop.
[Check the resources](./Conclusion/README.md).
