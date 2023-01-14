
cmake_minimum_required(VERSION 3.5)
project(pub)

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

add_executable(pub
  src/pub.cpp
)

ament_target_dependencies(pub
  rclcpp
  std_msgs
)

target_link_libraries(pub
  ${QT_LIBRARIES}
)

install(TARGETS
  pub
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
