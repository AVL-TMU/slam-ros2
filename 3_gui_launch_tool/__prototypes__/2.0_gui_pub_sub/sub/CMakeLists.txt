cmake_minimum_required(VERSION 3.5)
project(sub)

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
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(sub
  src/sub.cpp
)

ament_target_dependencies(sub
  rclcpp
  std_msgs
)

install(TARGETS
  sub
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
