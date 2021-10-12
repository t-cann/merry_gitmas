#! /bin/python3.8

#pip install gitpython

import git
import os
import subprocess

def get_git_revision_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()

def get_git_revision_short_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

#os.chdir if not running from right dir

# import subprocess
# from pathlib import Path
# print(subprocess.check_output(["git", "describe", "--always"], cwd=Path(__file__).resolve().parent).strip().decode())

def get_hash_with_gitpython():
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    repo = git.Repo(dirpath)
    sha = repo.head.object.hexsha
    return sha

def main():
    print(get_hash_with_gitpython())

if __name__=="__main__":
    main()