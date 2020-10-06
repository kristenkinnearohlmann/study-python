# https://sdbrett.com/BrettsITBlog/2017/03/python-parsing-api-xml-response-data/
# http://www.opengis.net/wfs
# https://sv443.net/jokeapi/v2/joke/Any?format=xml

import requests

if __name__ == "__main__":
    var_name = "Kristen"
    print(f"Run {var_name}")

    # get data from endpoint
    request = requests.get('https://sv443.net/jokeapi/v2/joke/Any?format=xml')
    print(request.text)

    # check that data is XML

    # check each tag for data of type