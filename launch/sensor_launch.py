from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor_comm',
            executable='i2c_sensor',
            output='screen'
        ),
        Node(
            package='sensor_comm',
            executable='uart_sensor',
            output='screen',
        )
    ])
