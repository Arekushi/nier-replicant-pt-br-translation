import zipfile
from src.utils import has_file, has_folder


def check_and_extract_zip(zip_file, extract_path):
    if not has_folder(zip_file[0:-4]):
        unzip_file(zip_file, extract_path)


def unzip_file(zip_file_path, extract_path):
    if has_file(zip_file_path):
        zip_file_obj = zipfile.ZipFile(zip_file_path)
        zip_file_obj.extractall(extract_path)
        zip_file_obj.close()
