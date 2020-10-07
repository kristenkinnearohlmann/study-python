# https://sdbrett.com/BrettsITBlog/2017/03/python-parsing-api-xml-response-data/
# http://www.opengis.net/wfs
# https://sv443.net/jokeapi/v2/joke/Any?format=xml
# https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-3-working-with-xml/

import requests
import xml.etree.ElementTree as et

if __name__ == "__main__":
    var_name = "Kristen"
    print(f"Run {var_name}")

    # get data from endpoint
    response = requests.get('https://sv443.net/jokeapi/v2/joke/Any?format=xml')
    # response = requests.get('https://sv443.net/jokeapi/v2/joke/Any?format=json')
    # print(response.text)

    # check that data is XML
    response_headers = response.headers
    print(response_headers["Content-Type"])
    if "application/xml" in response_headers["Content-Type"]:
        print("This is XML")

    # check each tag for data of type
    # response_xml = et.fromstring(response.content)
    # xml_tree = et.ElementTree(response_xml)
    # root = xml_tree.getroot()