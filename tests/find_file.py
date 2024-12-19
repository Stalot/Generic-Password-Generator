from pathlib import Path

def file_search(target_path):
    result = None
    cwd = Path.cwd()
    app_folder = Path('application').glob('**/*')
    files = [file for file in app_folder]

    for path in files:
        if path == Path(target_path):
            asset_folder_path = Path.joinpath(cwd, path)
            if asset_folder_path.exists():
                result = asset_folder_path
    
    return result