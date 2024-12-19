import os
from pathlib import Path

def with_os():
    current_dir = os.path.dirname(os.path.abspath(__name__)) 
    internal_path = os.path.join(current_dir, '_internal')
    print(internal_path)

def _internal():
    app_dir = Path('Generic-Password-Generator').absolute()
    files = app_dir.glob('*')
    exist: bool = False
    internal_path = None

    for file_path in files:
        if '_internal' in file_path.absolute().as_posix():
            exist = True
            internal_path = file_path
    return [exist, internal_path]