import os
import errno
import shutil
from re import search
from contextlib import suppress


def has_folder(folder_path):
    return os.path.exists(folder_path)


def has_file(file_path):
    return os.path.isfile(file_path)


def rename(path, new_path):
    if has_folder(path) or has_file(path):
        os.rename(path, new_path)


def get_folders_name(path):
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]


def get_folders_with_same_name(path, name):
    return list(filter(lambda file_path: search(name, file_path), get_folders_name(path)))


def copy_folder(folder_path, dest_path, override=True):
    if not override:
        if has_folder(dest_path):
            return

    return shutil.copytree(folder_path, dest_path, dirs_exist_ok=override)


def get_all_files_path(path):
    files = [
        os.path.join(parent, name)
        for (parent, subdirs, files) in os.walk(path)
        for name in files + subdirs
    ]

    return files


def filter_files_from_lang(files, lang):
    def filter_file(file):
        with suppress(IndexError):
            return str(file).split('.')[-3] == lang

    result = list(filter(lambda file: filter_file(file), files))
    result.extend([
        f'{files[0]}\\..\\text_common\\nier_text.txd.csv',
        f'{files[0]}\\..\\talk_all\\talker_name.tnd.csv',
    ])
    return result


def get_file_name(file_path):
    return file_path.split('\\')[-1]


def remove_files(files):
    for file in files:
        remove(file)


def remove(path):
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError("file {} is not a file or dir.".format(path))


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
