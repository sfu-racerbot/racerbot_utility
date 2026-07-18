# Contributing

> Make sure you've followed the [README setup](./README.md#how-to-use) first.

## Setup
```bash
pip install -r requirements.txt
pre-commit install
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
