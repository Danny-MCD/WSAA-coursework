# Assignment 03 : Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
# Author : Daniel Mc Donagh

import requests
import json

# URL for FIQ02 - Exchequer Account (Historical Series)
url= " https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Function to retrieve all data in JSON format for the url
def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":

    # Write the JSON results out to file cso.json
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)
    fp.close()