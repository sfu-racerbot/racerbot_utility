import argparse
from racerbot_utility.config import CONTAINER_NAME, SESSION_NAME
from racerbot_utility.lib.docker_utils import (
    ensure_container_running,
    end_container,
)
from racerbot_utility.lib.tmux_utils import (
    ensure_session_running,
    ensure_window_running,
    attach,
    end_session,
)
from racerbot_utility.lib.ros_actions import (
    launch_sim,
    launch_teleop,
    find_current_pose,
    reset_car,
)


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
        print(
            f"To attach: docker exec -it {CONTAINER_NAME} tmux attach -t {SESSION_NAME}"
        )


def cmd_end_sim(args: argparse.Namespace) -> None:
    end_session()
    print("Sim Ended.")

    if not args.session_only:
        end_container()
        print("Container Ended.")


def cmd_reset_car(args: argparse.Namespace) -> None:
    reset_car(x=args.x, y=args.y, yaw=args.yaw)
    print("Car reset.")


def cmd_find_pose(args: argparse.Namespace) -> None:
    find_current_pose()


def main() -> None:
    parser = argparse.ArgumentParser(prog="racerbot")
    sub = parser.add_subparsers(dest="command", required=True)

    p_start = sub.add_parser("start-sim", help="Start the simulator")
    p_start.add_argument(
        "--teleop", action="store_true", help="Also launch teleop keyboard control"
    )
    p_start.add_argument(
        "--attach", action="store_true", help="Attach to tmux session after starting"
    )
    p_start.set_defaults(func=cmd_start_sim)

    p_end = sub.add_parser("end-sim", help="End the simulator")
    p_end.add_argument(
        "--session-only",
        action="store_true",
        help="End the tmux session but leave the container running",
    )
    p_end.set_defaults(func=cmd_end_sim)

    p_reset = sub.add_parser("reset-car", help="Reset the car's pose and speed")
    p_reset.add_argument(
        "--x", type=float, default=None, help="X position (defaults to config)"
    )
    p_reset.add_argument(
        "--y", type=float, default=None, help="Y position (defaults to config)"
    )
    p_reset.add_argument(
        "--yaw", type=float, default=None, help="Yaw in radians (defaults to config)"
    )
    p_reset.set_defaults(func=cmd_reset_car)

    p_find_pose = sub.add_parser(
        "find-pose", help="Print the car's current pose (for picking a good default)"
    )
    p_find_pose.set_defaults(func=cmd_find_pose)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
