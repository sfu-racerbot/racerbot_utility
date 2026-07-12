import argparse
from config import CONTAINER_NAME, SESSION_NAME
from lib.docker_utils import ensure_container_running, end_container
from lib.tmux_utils import ensure_session_running, ensure_window_running, attach, end_session
from lib.ros_actions import launch_sim, launch_teleop

def cmd_start_sim(args: argparse.Namespace) -> None:
    ensure_container_running()

    ensure_session_running()
    ensure_window_running("sim")
    launch_sim("sim")

    if args.teleop:
        ensure_window_running("teleop")
        launch_teleop("teleop")

    print("Sim Ready.")
    print("Connect to Foxglove: https://app.foxglove.dev/")

    if args.attach:
        input("Press 'enter' to attach")
        attach()
    else:
        print(f"To attach: docker exec -it {CONTAINER_NAME} tmux attach -t {SESSION_NAME}")

def cmd_end_sim(args: argparse.Namespace) -> None:
    end_session()

    if not args.session_only:
        end_container()

def main() -> None:
    parser = argparse.ArgumentParser(prog="racerbot")
    sub = parser.add_subparsers(dest="command", required=True)

    p_start = sub.add_parser("start-sim", help="Start the simulator")
    p_start.add_argument("--teleop", action="store_true", help="Also launch teleop keyboard control")
    p_start.add_argument("--attach", action="store_true", help="Attach to tmux session after starting")
    p_start.set_defaults(func=cmd_start_sim)

    p_end = sub.add_parser("end-sim", help="End the simulator")
    p_end.add_argument("--session-only", action="store_true", help="End the tmux session but leave the container running")
    p_end.set_defaults(func=cmd_end_sim)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
