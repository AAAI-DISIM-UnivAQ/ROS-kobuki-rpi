# ROS-kobuki-RPI
Learn ROS (kinetic) through the Kobuki base and the RaspberryPI

## Requirements

* Raspberry Pi 2 or 3
* Kobuki
* [Ubuntu Mate 16.04 (Raspberry Pi)](http://ubuntu-mate.org/download) 

## Install

1. Configure your Ubuntu repositories to allow "restricted", "universe", and "multiverse".

2. Setup the RPI to accept software from _packages.ros.org_ :

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc ) main" > /etc/apt/sources.list.d/ros-latest.list'
    
3. Setup the repository keys:

    sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-ke y 421C365BD9FF1F717815A3895523BAEEB01FA116
    
If you experience issues connecting to the keyserver, you can try substituting
hkp://pgp.mit.edu:80 or hkp://keyserver.ubuntu.com:80.


4. Make sure your package index is up-to-date

    sudo apt update
    sudp apt upgrade
    
5. There are many different libraries and tools in ROS. In our case, we use the _Desktop_ one:

    sudo apt-get install ros-kinetic-desktop

In this installation there are: ROS core, rqt, rviz and robot-generic libraries.

6. Before you can use ROS, you will need to initialize with _rosdep_ , which enables you to easily install all the system dependencies that are needed to compile and run basic ROS core components.

    sudo rosdep init
    rosdep update
    
 
