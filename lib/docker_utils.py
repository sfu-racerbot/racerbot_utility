import subprocess
from config import CONTAINER_NAME

def is_container_running() -> bool:
    result = subprocess.run(
        ["docker", "inspect", "-f", "{{.State.Running}}", CONTAINER_NAME],
        capture_output=True, text=True
    )
    return result.returncode == 0 and result.stdout.strip() == "true"

def _start_container() -> None:
    subprocess.run(
        ["docker", "start", CONTAINER_NAME],
        check=True
    )

def ensure_container_running() -> None:
    if not is_container_running():
        print(f"Starting container '{CONTAINER_NAME}'...")
        _start_container()
    else:
        print(f"Container '{CONTAINER_NAME}' already running.")

def end_container() -> None:
    subprocess.run(
        ["docker", "stop", CONTAINER_NAME],
        check=True
    )

def dexec(cmd: str) -> subprocess.CompletedProcess:
    return subprocess.run(["docker", "exec", CONTAINER_NAME, "bash", "-c", cmd])
