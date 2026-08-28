# TWINS Robot Description

This ROS 2 package contains URDF models and meshes for the TWINS leader and
follower robots.

## Models

- `urdf/twin_arms_leader.urdf`
- `urdf/twin_arms_follower.urdf`

The mesh filenames in both URDFs use `package://twins_description/meshes/...`
URIs, so they do not depend on the location of the workspace.

## Build

Place this repository in a ROS 2 workspace, then build and source it:

```bash
cd /path/to/ros2_ws
colcon build --packages-select twins_description
source install/setup.bash
```

## Display in RViz

The follower model is displayed by default:

```bash
ros2 launch twins_description display.launch.py
```

Select the leader model with the `model` launch argument:

```bash
ros2 launch twins_description display.launch.py model:=leader
```

The launch file starts `robot_state_publisher`, `joint_state_publisher_gui`,
and RViz 2 using `rviz/display.rviz`.

## License

This package is licensed under the CERN Open Hardware Licence Version 2 -
Weakly Reciprocal (`CERN-OHL-W-2.0`). See the repository's
[LICENSE](../LICENSE) file for details.
