CONTAINER_NAME = "racerbot"
WORKSPACE_PATH = "/racerbot_ws"
SESSION_NAME = "f1tenth"

SOURCE_ENV_CMD = (
    f"source {WORKSPACE_PATH}/.venv/bin/activate && "
    f"source /opt/ros/humble/setup.bash && "
    f"source {WORKSPACE_PATH}/install/local_setup.bash"
)

RUN_SIM = "ros2 launch f1tenth_gym_ros gym_bridge_launch.py"
RUN_TELEOP = "ros2 run teleop_twist_keyboard teleop_twist_keyboard"
