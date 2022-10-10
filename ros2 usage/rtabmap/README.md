## Installations (instructions for Focal Fossa on VM)

### Install Nav2
https://navigation.ros.org/build_instructions/index.html
```
sudo apt install ros-<distro>-navigation2 ros-<distro>-nav2-bringup ros-<distro>-turtlebot3*
```
where `<distro>` = `foxy`

### Install Octomap
https://github.com/OctoMap/octomap/tree/ros2

create `octomap` dir in home folder and open in terminal.
```
git clone --branch ros2 https://github.com/OctoMap/octomap.git
cd octomap
mkdir build
cd build
cmake ..
make
```

```
sudo apt-get install ros-foxy-octomap ros-foxy-octomap-msgs
```

### Build RTAB-Map for Ros2
https://github.com/introlab/rtabmap/tree/foxy-devel

```
cd ~/ros2_ws
git clone https://github.com/introlab/rtabmap.git src/rtabmap
git clone --branch ros2 https://github.com/introlab/rtabmap_ros.git src/rtabmap_ros
colcon build --symlink-install
```
Do NOT use  `export MAKEFLAGS="-j6"`

do overlay
```
. install/setup.bash
```
and use 

## Instructions for usage of RTABMapping solution