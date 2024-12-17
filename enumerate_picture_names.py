from pathlib import Path


current_dir = Path.cwd()
BASE_NAME = 'pict_'
count = 1

for file in current_dir.iterdir():
    try:
        if file.is_file() and file.stem != "enumerate_picture_names":
            new_name = f'{BASE_NAME}{count}{file.suffix}'
            new_path = file.with_name(new_name)
            file.rename(new_path)
            count += 1
    except Exception as e:
        count += 1
        continue
