# example.launch.py

import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace

'''
realsense_camera_node (/camera)     R-TAB map param
                                    /odom
/color/image_raw                    /rgb/image
/depth/image_rect_raw               /depth/image
/color/camera_info                  /rgb/camera_info


                                    /rgb/image \
                                    /depth/image \
                                    /rgb/camera_info


When Using Launch File for RTABMAP
                                    [rtabmap-2] rtabmap subscribed to (exact sync):
                                    [rtabmap-2]    /rtabmap/odom \
                                    [rtabmap-2]    /camera/rgb/image_rect_color \
                                    [rtabmap-2]    /camera/depth_registered/image_raw \
                                    [rtabmap-2]    /camera/rgb/camera_info \
                                    [rtabmap-2]    /rtabmap/odom_info
'''

def generate_launch_description():
    ## for run file
    realsense_camera_node = Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='base',
            remappings=[
                ('/color/image_raw', '/rgb/image'),
                ('/color/camera_info', '/rgb/camera_info'),
                ('/depth/image_rect_raw', '/depth/image'),
            ],
            parameters=[
                #{"base_frame_id": "link"},
                #{"base_frame": "link"},
                {"camera_name": "base"},
                {"tf_publish_rate": 0.0},
                # {"enable_gyro": "true"},
                # {"enable_accel": "true"},

            ]
        )
    

    ## for rtabmap launch file

    # realsense_camera_node = Node(
    #         package='realsense2_camera',
    #         executable='realsense2_camera_node',
    #         name='base',
    #         remappings=[
    #             ('/color/image_raw', '/camera/rgb/image_rect_color'),
    #             ('/color/camera_info', '/camera/rgb/camera_info'),
    #             ('/depth/image_rect_raw', '/camera/depth_registered/image_raw'),
    #         ],
    #         parameters=[
    #             #{"base_frame_id": "link"},
    #             #{"base_frame": "link"},
    #             {"camera_name": "base"},
    #             {"tf_publish_rate": 0.0},
    #             # {"enable_gyro": "true"},
    #             # {"enable_accel": "true"},

    #         ]
    #     )

    return LaunchDescription([
        realsense_camera_node
    ])