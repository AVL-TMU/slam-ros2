# Pre-Req Install
If jetson linux is a fresh jetpack install you may want to purge libopencv before continuing with any other installations as it causes instability with certain ros2 packages such as RTAB-Map </br>
https://github.com/introlab/rtabmap_ros/issues/548 </br>
Do this using
```
sudo apt-get purge *libopencv*
``
And build opencv using these instructions: </br>
https://github.com/teamr3/getting-started/tree/master/jetson%20nano%204gb/opencv_source%20(os-depend)
