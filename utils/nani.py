import requests
url = "https://raw.githubusercontent.com/demotto/my-pipeline/master/expr001/component.yaml"
resp = requests.get(url)
print(resp)
