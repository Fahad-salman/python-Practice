import requests
from pprint import pprint
 
def geocode():
    url = "https://jsonplaceholder.typicode.com/todos/4";
    resp = requests.get(url)
    return resp.json()
 
# calling geocode function
data = geocode()

pprint(data)