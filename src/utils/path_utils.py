import os
import errno
import shutil


def has_folder(folder_path) -> bool:
    return os.path.exists(folder_path)


def has_file(file_path) -> bool:
    return os.path.isfile(file_path)


def rename(path, new_path):
    if has_folder(path) or has_file(path):
        os.rename(path, new_path)

    raise ValueError(f"file {path} is not a file or dir.")


def get_folders_name(path):
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]


def copy_folder(folder_path, dest_path, override=True):
    if not override:
        if has_folder(dest_path):
            return

    return shutil.copytree(folder_path, dest_path, dirs_exist_ok=override)


def get_all_files_from_path(path) -> list[str]:
    files = [
        os.path.join(parent, name)
        for (parent, subdirs, files) in os.walk(path)
        for name in files
        if os.path.isfile(os.path.join(parent, name))
    ]

    return files


def get_file_name(file_path, index=-1) -> str:
    return file_path.split('\\')[index]


def remove_files(files):
    for file in files:
        remove(file)


def remove(path):
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError(f"file {path} is not a file or dir.")


def make_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


def copy_file(file_path, dest_path):
    return shutil.copy(file_path, dest_path)


def copy_files(files_path, dest_path):
    for file in files_path:
        copy_file(file, dest_path)
