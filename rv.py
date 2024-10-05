#!/usr/bin/env python3

import argparse
import os
import yaml
import sys
import subprocess
import libs.rvutils as rvutils

def preview():
    config = rvutils.read_config()

    libs = config['paths']['libs']
    blender = config['paths']['blender']

    cmd = f"PYTHONPATH='{libs}' {blender} -b -P generate.py --python-use-system-env"
    print(cmd)
    os.system(cmd)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Command to run', choices=['preview', 'render', 'init', 'help'])

    args = parser.parse_args()
    if args.command == 'preview':
        preview()
    elif args.command == 'render':
        print("Not implemented")
    elif args.command == 'init':
        rvutils.gen_config()
    elif args.command == 'help':
        parser.print_help()

if __name__ == '__main__':
    main()