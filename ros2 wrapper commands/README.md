## Useful Commands for ROS2 Wrapper

```bash
  ros2 launch realsense2_camera rs_launch.py
```
or, with parameters specified in rs_launch.py, for example - pointcloud enabled:
```bash
ros2 launch realsense2_camera rs_launch.py enable_pointcloud:=true device_type:=d435
```
or, without using the supplement launch files:
```bash
ros2 run realsense2_camera realsense2_camera_node --ros-args -p filters:=colorizer
```
or, with a demo config file:
```bash
ros2 launch realsense2_camera rs_launch.py config_file:="'$COLCON_PREFIX_PATH/realsense2_camera/share/realsense2_camera/config/d435i.yaml'"
```

### View and Modify Camera Controls Params in runtime:
The following command allow to change camera control values.
```bash
ros2 run rqt_reconfigure rqt_reconfigure
```
<p align="center"><img src="https://user-images.githubusercontent.com/40540281/122672659-6f458b80-d1d5-11eb-9262-545d2073e1da.png" /></p>