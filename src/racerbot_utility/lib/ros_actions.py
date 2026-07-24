import math
from racerbot_utility.config import (
    RUN_SIM,
    RUN_TELEOP,
    SESSION_NAME,
    INITIAL_POSE,
    DRIVE_TOPIC,
    ODOM_TOPIC,
    SOURCE_ENV_CMD,
)
from racerbot_utility.lib.tmux_utils import send_keys
from racerbot_utility.lib.docker_utils import dexec


def launch_sim(window_name: str) -> None:
    send_keys(f"{SESSION_NAME}:{window_name}", RUN_SIM)


def launch_teleop(window_name: str) -> None:
    send_keys(f"{SESSION_NAME}:{window_name}", RUN_TELEOP)


def reset_pose(x: float = None, y: float = None, yaw: float = None) -> None:
    x = INITIAL_POSE["x"] if x is None else x
    y = INITIAL_POSE["y"] if y is None else y
    yaw = INITIAL_POSE["yaw"] if yaw is None else yaw

    qz = math.sin(yaw / 2)
    qw = math.cos(yaw / 2)

    msg = (
        f"{{header: {{frame_id: 'map'}}, "
        f"pose: {{pose: {{position: {{x: {x}, y: {y}, z: 0.0}}, "
        f"orientation: {{x: 0.0, y: 0.0, z: {qz}, w: {qw}}}}}}}}}"
    )
    dexec(
        f'{SOURCE_ENV_CMD} && ros2 topic pub --once /initialpose geometry_msgs/msg/PoseWithCovarianceStamped "{msg}" > /dev/null 2>&1'
    )


def reset_speed() -> None:
    msg = "{drive: {speed: 0.0, steering_angle: 0.0}}"
    dexec(
        f'{SOURCE_ENV_CMD} && ros2 topic pub --once {DRIVE_TOPIC} ackermann_msgs/msg/AckermannDriveStamped "{msg}" > /dev/null 2>&1'
    )


def reset_car(x: float = None, y: float = None, yaw: float = None) -> None:
    reset_speed()
    reset_pose(x=x, y=y, yaw=yaw)


def find_current_pose() -> None:
    dexec(
        f"{SOURCE_ENV_CMD} && ros2 topic echo {ODOM_TOPIC} --once --field pose.pose.position"
    )
