import zipfile
import hashlib

def unzip_hash(filename):
    with zipfile.ZipFile(filename, 'r') as z:
        names = z.namelist()
        z.extractall()
    
    res = []
    for file in names:
        with open(file, 'rb') as f:
            content = f.read()
            md5 = hashlib.md5()
            md5.update(content)
            file_dict = {}
            file_dict['name'] = file
            file_dict['md5sum'] = md5.hexdigest()
            res.append(file_dict)
    return res


