import os
from urllib.parse import urlsplit

# For extracting the file name
def string_extract_filename(url_link):
    # Assuming it is a url link for now
    url_path = urlsplit(url_link)
    return os.path.basename(url_path.path)