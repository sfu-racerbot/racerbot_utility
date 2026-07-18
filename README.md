# Racerbot Utility

Racerbot Utility is a Python CLI that streamlines ROS 2 development and testing.

## How to Use

1. Create and activate a virtual environment

> Use `python3` on macOS/Linux and `python` on Windows, depending on your system's PATH setup. Check with `python3 --version` or `python --version`.

```bash
python3 -m venv .venv           # (use `python` on Windows)
source .venv/bin/activate       # macOS/Linux
.\.venv\Scripts\activate.ps1    # Windows PowerShell
```

2. Install the utility with `pip`
```bash
pip install git+https://github.com/sfu-racerbot/racerbot_utility
```

3. Make sure your `racerbot` Docker container exists (see [Racerbot Workspace](https://github.com/sfu-racerbot/racerbot_ws)).

## Commands

Run commands via the CLI:

```bash
racerbot-utility --help
```

### Start the simulator
```bash
racerbot-utility start-sim
```

Options:
- `--teleop` — also launch keyboard teleop control
- `--attach` — attach to the tmux session after starting

```bash
racerbot-utility start-sim --teleop --attach
```

### End the simulator
```bash
racerbot-utility end-sim
```

Options:
- `--session-only` — end the tmux session but leave the container running

```bash
racerbot-utility end-sim --session-only
```

## Project Structure

```
racerbot_utility/
├── LICENSE
├── pyproject.toml   # Project configuration for pip
├── README.md
├── requirements.txt # Python dependencies (managed via pip)
├── src/
│   └── racerbot_utility/
│       ├── __init__.py
│       ├── config.py            # Container/session names, ROS commands
│       ├── main.py              # CLI entrypoint (argparse subcommands)
│       └── lib/
│           ├── __init__.py
│           ├── docker_utils.py  # Docker container management
│           ├── ros_actions.py   # ROS 2 commands
│           └── tmux_utils.py    # tmux session/window management
```
