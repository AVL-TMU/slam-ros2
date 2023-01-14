## Simple Graphical Pub-Sub

This program is graphical implementation of the ROS2 pub-sub functionality using rclcpp and QtWidgets.
To run this program you need to build the packages `pub` and `sub` using the command `colcon build` in the dir this `README.md` is in. Once that's done you can open two terminals with and run the command `. install/setup.bash` on both of them. Then you can run `ros2 run pub pub` on one and `ros2 run sub sub` on another and your gui and subscriber should start.