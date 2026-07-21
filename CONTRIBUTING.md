# Contributing

> Make sure you've followed the [README setup](./README.md#how-to-use) first.

## Setup

1. Create and activate virtual environment.

```bash
git clone https://github.com/sfu-racerbot/racerbot_utility.git
cd racerbot_utility                            # Change directory to racerbot_utility
python3 -m venv .venv                          # (use `python` on Windows)
source .venv/bin/activate                      # macOS/Linux
.\.venv\Scripts\activate.ps1                   # Windows PowerShell
```

2. Install dependencies with `pip`.

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
