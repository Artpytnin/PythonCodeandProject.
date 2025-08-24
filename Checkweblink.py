import re

# Compile the regex pattern for URL validation
url_pattern = re.compile(
    r'^(https?://)'              # http or https protocol
    r'(www\.)?'                  # optional www
    r'[a-zA-Z0-9@:%._\+~#?&//=]{2,256}'  # domain and path characters
    r'\.[a-z]{2,6}'              # top-level domain
    r'\b([-a-zA-Z0-9@:%._\+~#?&//=]*)$'  # optional URL path/query
)

def is_valid_url(url):
    if url is None:
        return False
    return bool(re.match(url_pattern, url))

# Example usage:
url = "https://www.youtube.com"


print("The URL is valid.")



def is_invalid_url(url):
    if url is None:
        return True
    return not bool(re.match(url_pattern, url))

# Example usage:
url = "https://www.youtube.org"  # intentionally invalid URL


print("The URL is invalid.")
