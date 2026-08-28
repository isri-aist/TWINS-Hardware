from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def launch_setup(context):
    model = LaunchConfiguration("model").perform(context)
    model_files = {
        "leader": "twin_arms_leader.urdf",
        "follower": "twin_arms_follower.urdf",
    }
    if model not in model_files:
        raise RuntimeError(
            f"Unknown model '{model}'. Expected one of: {', '.join(model_files)}"
        )

    package_share = Path(get_package_share_directory("twins_description"))
    robot_description = (package_share / "urdf" / model_files[model]).read_text()
    rviz_config = package_share / "rviz" / "display.rviz"

    return [
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": robot_description}],
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", str(rviz_config)],
            output="screen",
        ),
    ]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "model",
                default_value="follower",
                description="Robot model to display: leader or follower",
            ),
            OpaqueFunction(function=launch_setup),
        ]
    )
