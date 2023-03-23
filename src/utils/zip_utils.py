import zipfile
from src.utils import has_file, remove


def check_if_has_unziped(file_exe, file_zip_path, extract_path):
    if not has_file(file_exe):
        zip_file_path = file_zip_path
        if has_file(zip_file_path):
            unzip_file(zip_file_path, extract_path)


def unzip_file(zip_file_path, extract_path):
    if has_file(zip_file_path):
        zip_file_obj = zipfile.ZipFile(zip_file_path)
        zip_file_obj.extractall(extract_path)
        zip_file_obj.close()
