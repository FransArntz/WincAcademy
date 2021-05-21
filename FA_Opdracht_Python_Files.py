__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

#

import os

def clean_cache():
    cache = 'C:/Users/ingeb/files/cache'
    if os.path.exists(cache):
        folder= os.listdir(cache)
        for file in folder:
            filepath=cache+'/'+file
            os.remove(filepath)  
    else:
        os.makedirs(cache)
clean_cache()

def cache_zip(zip_file_path, cache_dir_path):
    from zipfile import ZipFile
    with ZipFile(zip_file_path, 'r') as zip:
        zip.extractall(cache_dir_path)
cache_zip('C:/Users/ingeb/files/data.zip','C:/Users/ingeb/files/cache')

def cached_files():
    from pathlib import Path
    cache = 'C:/Users/ingeb/files/cache'
    cache_folder= os.listdir(cache)
    list_abs=[]
    for file in cache_folder:
        filepath=cache+'/'+file
        path_abs=os.path.abspath(filepath)
        list_abs.append(path_abs)
    return(list_abs)
cached_files() 

def find_password(cached_files):
    for file in (cached_files):
        with open (file, 'rt') as password_file:
                for line in password_file:
                    if 'password' in line:
                        password=line.strip('password: \n')
                        return(password)
find_password(cached_files())
 
