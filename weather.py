import requests
import json
import os
# import pandas as pd

API_KEY = os.environ.get("API_KEY")
URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/narowal?unitGroup=us&include=current&key={API_KEY}&contentType=json"

def get_data_from_file(file_path):
    with open(file_path, "w+") as f:
        data = json.load(f)
    return data

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


def main():
    get_api_data(URL)
    data = get_data_from_file("data.json")
    days = [day for day in data["days"]]
    tem = [tem["temp"] for tem in days]
    date = [date["datetime"] for date in days]
    final_data = [(x, y) for x in date for y in tem if date.index(x) == tem.index(y)]
    return (final_data)

if __name__ == "__main__":
    print(main())
