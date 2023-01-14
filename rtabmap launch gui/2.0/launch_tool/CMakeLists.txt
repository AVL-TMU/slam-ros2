
cmake_minimum_required(VERSION 3.5)
project(launch_tool)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

find_package(Qt5Core)
find_package(Qt5Widgets)

set(QT_LIBRARIES Qt5::Widgets)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

include_directories(launch_tool
  ${Qt5Core_INCLUDE_DIRS}
  ${Qt5Widgets_INCLUDE_DIRS}
)

add_executable(launch_tool
  src/tool.cpp
)

ament_target_dependencies(launch_tool
  rclcpp
  std_msgs
)

target_link_libraries(launch_tool
  ${QT_LIBRARIES}
)
#target_link_libraries(launch_tool_node Qt5::Widgets)

install(TARGETS
  launch_tool
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
