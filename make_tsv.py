
# Import libraries
import os
import hashlib
import base64


# Define constants
PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
BK_DIR = '../cld_cmpt/books/'

# md5 checksum 
def md5_checksum(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.digest()


# Write file
output_file = "../cld_cmpt/books.tsv"
with open(output_file, mode='w') as tsv_file: # opens the file and mode specifies writing
    tsv_file.write("TsvHttpData-1.0\n") # writes the first line of the file
    for filename in os.listdir(BK_DIR): # for each file in the directory
        if os.path.isfile(os.path.join(BK_DIR, filename)): # if it is an existing file
            file_path = os.path.join(BK_DIR, filename) # create the path for the md5 checksum
            file_size = os.path.getsize(file_path) # get the size
            file_md5 = base64.b64encode(md5_checksum(file_path)) # get the md5 checksum and encode
            file_url = f"{PREFIX}{filename}" # combine prefix and file name for the URL
            tsv_file.write(f"{file_url}\t{file_size}\t{file_md5}\n") # combine everything and write each line of the file