# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_launch_tool_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED launch_tool_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(launch_tool_FOUND FALSE)
  elseif(NOT launch_tool_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(launch_tool_FOUND FALSE)
  endif()
  return()
endif()
set(_launch_tool_CONFIG_INCLUDED TRUE)

# output package information
if(NOT launch_tool_FIND_QUIETLY)
  message(STATUS "Found launch_tool: 0.0.0 (${launch_tool_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'launch_tool' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${launch_tool_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(launch_tool_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${launch_tool_DIR}/${_extra}")
endforeach()
