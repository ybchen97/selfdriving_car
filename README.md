# Making a Self-driving toy car
Project I worked on during 2018. Hardware hookup is complete, just left with the software side of things. Credits to [Ryan Zotti](https://github.com/RyanZotti) for the inspiration and the general walkthrough


### Current State
Server:

-   Works fine, is able to accept data from [driving client](udp_driving_client.py)
-   Can pass commands to car motor from laptop keyboard
-   Can save commands into a single log entry

Car:

-   Finish up the chassis
-   Buy some batteries, test the speed of the motor using the server

Camera:

-   Can stream videos, but not sure if I can save each individual frame together with it's respective timestamp or not
-   Learn OpenCV and find out how to actually analyze the videos in order to find out which video format to use and record in (i.e. h264 or mjpg or bgr using picamera)
<br>

### To-do:

-   Learn OpenCV and find out how to actually analyze the videos in order to find out which video format to use and record in (i.e. h264 or mjpg or bgr using picamera)
-   Try OpenCV video streaming with the RPi and save timestamping data
-   Saving log entries to different sessions
-   Learn sockets
-   Handling complex commands (right-forward, left-forward etc.)
