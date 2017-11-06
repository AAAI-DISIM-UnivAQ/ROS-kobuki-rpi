# ROS-kobuki-RPI

Learn ROS through the Kobuki mobile robotic base and RaspberryPI on board 

## Requirements

* [Raspberry Pi](http://www.raspberrypi.org) 2 or 3
* [Kobuki](http://kobuki.yujinrobot.com)
* [Ubuntu Mate 16.04 (Raspberry Pi)](http://ubuntu-mate.org/download) 

## Install

1. Configure your Ubuntu repositories to allow "restricted", "universe", and "multiverse".

2. Setup the RPI to accept software from _packages.ros.org_ :

       sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc ) main" > /etc/apt/sources.list.d/ros-latest.list'
    
3. Setup the repository keys:

       sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-ke y 421C365BD9FF1F717815A3895523BAEEB01FA116
    
   If you experience issues connecting to the keyserver, you can try substituting hkp://pgp.mit.edu:80 or hkp://keyserver.ubuntu.com:80.

4. Make sure your package index is up-to-date

       sudo apt update
       sudp apt upgrade
    
5. There are many different libraries and tools in ROS. In our case, we use the _Desktop_ one:

       sudo apt-get install ros-kinetic-desktop

   In this installation there are: ROS core, rqt, rviz and robot-generic libraries.

6. Before you can use ROS, you will need to initialize with _rosdep_ , which enables you to easily install all the system dependencies that are needed to compile and run basic ROS core components.

       sudo rosdep init
       rosdep update
    
7. Add the ROS environment variables to your bash session:
 
       echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc source ~/.bashrc 
       
8. Up to now you have installed what you need to run the core ROS packages. To create and manage your own ROS workspaces, there are various tools and requirements that are distributed separately. Install this tool and other dependencies for building ROS packages:

       sudo apt-get install python-rosinstall python-rosinstall-generator python- wstool build-essential

9. Create and build a _catkin_ building workspace:

       mkdir -p ~/catkin_ws/src 
       cd ~/catkin_ws 
       catkin_make
       
10. Add the ROS environment variables to your bash session:

        echo "source ~/catkin_ws /devel/setup.bash" >> ~/.bashrc 
        source ~/.bashrc
       
11. Move your Python source files into the folder “~/catkin_ws/src/kobuki_project”;

12.  Build the packages in the catkin workspace:

         cd ~/catkin_ws catkin_make
       
13. Install the Kobuki stardard ROS drivers:

        sudo apt-get install ros-kinetic-kobuki ros-kinetic-kobuki-core
       
14.  If not already in the dialout group:

         sudo usermod -a -G dialout $USER
       
    then logout and login again (or close and reopen your command shell)
    
15.  Set udev rules:

         rosrun kobuki_ftdi create_udev_rules
         
   Reinsert the Kobuki's USB cable. You should now find it show up at “/dev/kobuki”;


## Run your robotic project

1. Launch the main ROS node controlling the kobuki base:

       roslaunch kobuki_node minimal.launch --screen
       
2. Launch in three different terminals (or screen shell sessions):

       rosrun kobuki_project sense.py   
       ronrun kobuki_project think.py
       rosrun kobuki_project act.py
