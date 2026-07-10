import subprocess
from config import CONTAINER_NAME, SESSION_NAME, SOURCE_ENV_CMD

def has_session() -> bool:
    result = subprocess.run(
        ["docker", "exec", CONTAINER_NAME, "tmux", "has-session", "-t", SESSION_NAME],
        capture_output=True
    )
    return result.returncode == 0

def _new_session(window_name: str = "sim") -> None:
    subprocess.run(
        ["docker", "exec", "-d", CONTAINER_NAME, "tmux", "new-session", "-d", "-s",
          SESSION_NAME, "-n", window_name], check=True
    )

def ensure_session_running() -> None:
    if not has_session():
        print(f"Creating tmux session '{SESSION_NAME}'...")
        _new_session()
    else:
        print(f"tmux session '{SESSION_NAME}' already exists.")

def has_window(window_name: str) -> bool:
    result = subprocess.run(
        ["docker", "exec", CONTAINER_NAME, "tmux", "list-windows", "-t", SESSION_NAME, "-F", "#{window_name}"],
        capture_output=True, text=True
    )
    return window_name in result.stdout.split()

def _new_window(window_name: str) -> None:
    subprocess.run(
        ["docker", "exec", CONTAINER_NAME, "tmux", "new-window", "-t", SESSION_NAME, "-n", window_name],
        check=True
    )

def ensure_window_running(window_name: str) -> None:
    if not has_window(window_name):
        print(f"Creating tmux window '{window_name}'...")
        _new_window(window_name)
    else:
        print(f"tmux window '{window_name}' already exists.")

def send_keys(target: str, command: str) -> None:
    subprocess.run(
        ["docker", "exec", CONTAINER_NAME, "tmux", "send-keys", "-t", target, command, "C-m"],
        check=True
    )
