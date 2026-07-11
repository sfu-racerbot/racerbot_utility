import argparse
from lib.docker_utils import ensure_container_running
from lib.tmux_utils import ensure_session_running, ensure_window_running
from lib.ros_actions import launch_sim, launch_teleop

def cmd_start_sim(args: argparse.Namespace) -> None:
    ensure_container_running()

    ensure_session_running()
    ensure_window_running("sim")
    launch_sim("sim")

    if args.teleop:
        ensure_window_running("teleop")
        launch_teleop("teleop")

    # TODO: attach

def main() -> None:
    parser = argparse.ArgumentParser(prog="racerbot")
    sub = parser.add_subparsers(dest="command", required=True)

    p_start = sub.add_parser("start-sim", help="Start the simulator")
    p_start.add_argument("--teleop", action="store_true")
    p_start.set_defaults(func=cmd_start_sim)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
