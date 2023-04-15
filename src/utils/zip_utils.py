import zipfile
from src.utils import has_file


def check_and_extract_zip(file_exe, extract_path):
    if not has_file(file_exe):
        base_path = '\\'.join(file_exe.split('\\')[:-1])
        unzip_file(f'{base_path}.zip', extract_path)


def unzip_file(zip_file_path, extract_path):
    if has_file(zip_file_path):
        zip_file_obj = zipfile.ZipFile(zip_file_path)
        zip_file_obj.extractall(extract_path)
        zip_file_obj.close()
