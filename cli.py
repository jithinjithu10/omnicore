import argparse
import os

PROJECT_TEMPLATE = """from omnicore.core.app import OmniApp

app = OmniApp("{name}")

if __name__ == "__main__":
    app.start()
    print("App running")
    app.stop()
"""

def init_project(name):
    os.makedirs(name, exist_ok=True)
    with open(os.path.join(name, "main.py"), "w") as f:
        f.write(PROJECT_TEMPLATE.format(name=name))
    with open(os.path.join(name, "config.yaml"), "w") as f:
        f.write("app:\n  name: {}\n".format(name))
    print(f"✔ Project '{name}' created")

def run_project():
    os.system("python main.py")

def main():
    parser = argparse.ArgumentParser("omnicore")
    sub = parser.add_subparsers(dest="cmd")

    init = sub.add_parser("new")
    init.add_argument("name")

    run = sub.add_parser("run")

    args = parser.parse_args()

    if args.cmd == "new":
        init_project(args.name)
    elif args.cmd == "run":
        run_project()
    else:
        parser.print_help()
