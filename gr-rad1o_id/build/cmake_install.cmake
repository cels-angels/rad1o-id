# Install script for directory: /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/cmake/rad1o_id" TYPE FILE FILES "/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/cmake/Modules/rad1o_idConfig.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/include/rad1o_id/cmake_install.cmake")
  include("/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/lib/cmake_install.cmake")
  include("/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig/cmake_install.cmake")
  include("/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/python/cmake_install.cmake")
  include("/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/grc/cmake_install.cmake")
  include("/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/apps/cmake_install.cmake")
  include("/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/docs/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

file(WRITE "/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/${CMAKE_INSTALL_MANIFEST}" "")
foreach(file ${CMAKE_INSTALL_MANIFEST_FILES})
  file(APPEND "/home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/${CMAKE_INSTALL_MANIFEST}" "${file}\n")
endforeach()
