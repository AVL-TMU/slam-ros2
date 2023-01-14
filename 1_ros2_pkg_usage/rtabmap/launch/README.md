# Using RGB-D odometry wirelessly using ROS2
lorem ipsum dolor sit ameit

## Instructions

launch `realsense_node`
```
ros2 launch launch_realsense/launch.py approx_sync:=false
```
run `rgbd_odometry node`
```
ros2 run rtabmap_ros rgbd_odometry approx_sync:=false
```
run `rtabmap` server:
```
ros2 run rtabmap_ros rtabmap approx_sync:=false
```

run `rtabmapviz` client:
```
ros2 run rtabmap_ros rtabmapviz
```

## Tools

Use `rqt_graph` to visualise remapping:
```
ros2 run rqt_graph rqt_graph
```

Use `view_frames` to visualise tf frames:
```
ros2 run tf2_tools view_frames.py
```
## Misc.// To Be amended later
```
ros2 launch rtabmap_ros rtabmap.launch.py rtabmap_args:="--delete_db_on_start" frame_id:=camera_link
```