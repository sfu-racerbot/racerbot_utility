from config import RUN_SIM, SOURCE_ENV_CMD, RUN_TELEOP, SESSION_NAME
from lib.tmux_utils import send_keys

def source_window(window_name: str) -> None:
    send_keys(f"{SESSION_NAME}:{window_name}", SOURCE_ENV_CMD)

def launch_sim(window_name: str) -> None:
    source_window(window_name)
    send_keys(f"{SESSION_NAME}:{window_name}", RUN_SIM)

def launch_teleop(window_name: str) -> None:
    source_window(window_name)
    send_keys(f"{SESSION_NAME}:{window_name}", RUN_TELEOP)
