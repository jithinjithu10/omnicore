import argparse
from omnicore.core.app import OmniApp

def main():
    parser = argparse.ArgumentParser(prog="omnicore")
    sub = parser.add_subparsers(dest="command")

    init_cmd = sub.add_parser("init")
    init_cmd.add_argument("name")

    run_cmd = sub.add_parser("run")
    run_cmd.add_argument("name")

    args = parser.parse_args()

    if args.command == "init":
        init_project(args.name)
    elif args.command == "run":
        run_app(args.name)
    else:
        parser.print_help()

def init_project(name):
    print(f"Initializing OmniCore project: {name}")
    with open("main.py", "w") as f:
        f.write(
            "from omnicore.core.app import OmniApp\n\n"
            f"app = OmniApp('{name}')\n"
            "app.start()\n"
            "app.stop()\n"
        )

def run_app(name):
    app = OmniApp(name)
    app.start()
    app.stop()
