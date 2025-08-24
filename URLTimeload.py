import requests
import time


def time_url_open(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    start_time = time.time()
    requests.get(url)
    end_time = time.time()
    loading_time = end_time - start_time
    return loading_time


url = input("Enter url to test: ")
print(f"\n{url} loaded in {time_url_open(url):.2f} seconds.")
