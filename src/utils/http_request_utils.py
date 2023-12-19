import requests

from .path_utils import make_dir


def download_file(url: str, dest_path: str):
    file_name = url.split('/')[-1]
    
    make_dir(dest_path)
    
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        
        with open(f'{dest_path}\\{file_name}', 'wb') as file:        
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    
    
    return f'{dest_path}\\{file_name}'
