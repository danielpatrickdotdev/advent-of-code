#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import shutil
import sys


if __name__ == '__main__':
    # Get solution folder name from argv
    try:
        solution_dir = sys.argv[1]
    except IndexError:
        print("Usage: copy_templates <path>")
        sys.exit(1)

    # Ensure templates exist in expected location
    templates_path = Path.cwd().joinpath("template")
    if not templates_path.exists():
        print("Aborting: unable to find path {}".format(templates_path))
        sys.exit(1)

    # Create solution folder if necessary
    solution_path = Path.cwd().joinpath(solution_dir)
    if not solution_path.exists():
        print("Creating directory: {}".format(solution_path))
        solution_path.mkdir()

    created = False

    # Copy template files (note: skips any that already exist)
    for child in templates_path.iterdir():
        if child.is_file() and child.suffix in (".py", ".txt"):
            to_create = solution_path.joinpath(child.name)
            if not to_create.exists():
                print("Creating file: {}".format(to_create.name))
                shutil.copy(child, to_create)
                created = True

    # Tell the user we're done
    if created:
        print("Done")
    else:
        print("No files created")
