# Racerbot Utility

Racerbot Utility provides automation scripts and tools that streamline ROS 2 development and testing.

## How to Use

1. Clone this repository
```bash
git clone https://github.com/sfu-racerbot/racerbot_utility.git
```

2. Move into the project directory
```bash
cd racerbot_utility
```

3. Create and activate a virtual environment

> Use `python3` on macOS/Linux and `python` on Windows, depending on your system's PATH setup. Check with `python3 --version` or `python --version`.

```bash
python3 -m venv .venv           # (use `python` on Windows)
source .venv/bin/activate       # macOS/Linux
.\.venv\Scripts\activate.ps1    # Windows PowerShell
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Make sure your `racerbot` Docker container exists (see [Racerbot Workspace](https://github.com/sfu-racerbot/racerbot_ws)).

## Commands

Run commands via the CLI:

```bash
python cli.py --help
```

### Start the simulator
```bash
python cli.py start-sim
```

Options:
- `--teleop` — also launch keyboard teleop control
- `--attach` — attach to the tmux session after starting

```bash
python cli.py start-sim --teleop --attach
```

### End the simulator
```bash
python cli.py end-sim
```

Options:
- `--session-only` — end the tmux session but leave the container running

```bash
python cli.py end-sim --session-only
```

## Project Structure

```
racerbot_utility/
├── cli.py               # CLI entrypoint (argparse subcommands)
├── config.py            # Container/session names, ROS commands
├── lib/
│   ├── docker_utils.py  # Docker container management
│   ├── tmux_utils.py    # tmux session/window management
│   └── ros_actions.py   # ROS 2 commands
├── tests/               # Unit tests
└── requirements.txt     # Python dependencies (managed via pip)
```
