import requests
import json
import os

API_KEY = os.environ.get("API_KEY")
URL = os.environ.get("API_URL")
def write_into_file(msg, filename, extention="txt"):
    file1 = open(f"{filename}.{extention}","w+")
    file1.writelines(msg)
    file1.close()

def get_api_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        write_into_file(json.dumps(data), filename="data", extention="json")
        return data
    except Exception as e:
        write_into_file(str(e), filename="error", extention="txt")

get_api_data(URL, api_key=None)