import yaml
import subprocess
import os

MAC_BLENDER_PATH = "/Applications/Blender.app/Contents/MacOS/Blender"


def read_config():
    with open("config.yaml", "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def gen_config():
    result = subprocess.run(["whereis", "blender"], capture_output=True)
    possible_blender_paths = result.stdout.decode().split()
    possible_blender_path = ""

    if len(possible_blender_paths) > 1:
        possible_blender_path = possible_blender_paths[1]
    else:
        if os.path.exists(MAC_BLENDER_PATH):
            possible_blender_path = MAC_BLENDER_PATH

    lib_path = os.path.join(os.getcwd(), "lib")

    print("Generating config file...")

    blender_path = input(f"Enter the path to Blender ({possible_blender_path}): ")

    if blender_path.strip() == "":
        blender_path = possible_blender_path

    config = {
        "paths": {
            "blender": blender_path,
            "libs": lib_path,
        }
    }

    config_str = yaml.dump(config)

    print("\nConfig file generated:")
    print("-" * 30 + "\n")
    print(config_str)
    print("-" * 30)
    print("Writing to config.yaml...")
    with open("config.yaml", "w") as f:
        f.write(config_str)