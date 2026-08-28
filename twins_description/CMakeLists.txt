cmake_minimum_required(VERSION 3.10)
project(twins_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch meshes rviz urdf
  DESTINATION share/${PROJECT_NAME}
)

install(
  FILES README.md ../LICENSE
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
