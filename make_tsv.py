# Import libraries

import os
import hashlib
import base64


# Define constants
PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
BK_DIR = '../Cld_Cmpt/books/'

# md5 checksum 
def md5_checksum(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.digest()

# Write file
output_file = "../Cld_Cmpt/books.tsv"
with open(output_file, mode='w') as tsv_file:
    tsv_file.write("TsvHttpData-1.0\n")
    for filename in os.listdir(BK_DIR):
        if os.path.isfile(os.path.join(BK_DIR, filename)):
            file_path = os.path.join(BK_DIR, filename)
            file_size = os.path.getsize(file_path)
            file_md5 = base64.b64encode(md5_checksum(file_path))
            file_url = f"{PREFIX}{filename}"
            tsv_file.write(f"{file_url}\t{file_size}\t{file_md5}\n")
