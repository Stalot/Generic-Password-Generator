from pathlib import Path
import os

def generate_path(*args, absolute: bool = True):
    files_path = []
    for path in args:
        files_path.append(path)
    pathString: str = '/'.join(files_path)
    result_path: Path = Path(pathString)
    if absolute:
        result_path = result_path.absolute()
    
    return result_path

def assets_folder():
    app_dir = Path.cwd()
    files = app_dir.glob('*')
    folder_path = None

    file_path = Path.joinpath(app_dir, 'assets').absolute()
    if file_path.exists():
            folder_path = file_path
    return folder_path

def _internal():
    app_dir = Path.cwd()
    files = app_dir.glob('*')
    exist: bool = False
    internal_path = None

    file_path = Path.joinpath(app_dir, '_internal').absolute()
    if file_path.exists():
        exist = True
        internal_path = file_path
    if not exist:
        return None
    return internal_path

if __name__ == "__main__":
    a = assets_folder()
    print(a)