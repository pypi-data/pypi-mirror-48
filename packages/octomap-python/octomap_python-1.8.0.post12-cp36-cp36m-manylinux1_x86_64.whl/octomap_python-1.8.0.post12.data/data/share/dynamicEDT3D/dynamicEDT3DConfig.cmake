# - Config file for the dynamicEDT3D package
# (example from http://www.vtk.org/Wiki/CMake/Tutorials/How_to_create_a_ProjectConfig.cmake_file)
#
#  Usage from an external project:
#    In your CMakeLists.txt, add these lines:
#
#    FIND_PACKAGE(dynamicedt3d REQUIRED )
#    INCLUDE_DIRECTORIES(${DYNAMICEDT3D_INCLUDE_DIRS})
#    TARGET_LINK_LIBRARIES(MY_TARGET_NAME ${DYNAMICEDT3D_LIBRARIES})
#
# It defines the following variables
#  DYNAMICEDT3D_INCLUDE_DIRS - include directories for dynamicEDT3D
#  DYNAMICEDT3D_LIBRARY_DIRS - library directories for dynamicEDT3D (normally not used!)
#  DYNAMICEDT3D_LIBRARIES    - libraries to link against
 
# Tell the user project where to find our headers and libraries
set(DYNAMICEDT3D_INCLUDE_DIRS "/tmp/pip-req-build-aqtw3g4x/_skbuild/linux-x86_64-3.6/cmake-install/include")
set(DYNAMICEDT3D_LIBRARY_DIRS "/tmp/pip-req-build-aqtw3g4x/_skbuild/linux-x86_64-3.6/cmake-install/lib")
 
# Our library dependencies (contains definitions for IMPORTED targets)
# include("/FooBarLibraryDepends.cmake")
 
set(DYNAMICEDT3D_LIBRARIES "/tmp/pip-req-build-aqtw3g4x/_skbuild/linux-x86_64-3.6/cmake-install/lib/libdynamicedt3d.so")
