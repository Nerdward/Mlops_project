import json

import requests
from deepdiff import DeepDiff

with open("input.json", "rt", encoding="utf-8") as f:
    house = json.load(f)

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
response = requests.post(url, json=house)
print("actual response: ")
print(response.json())

expected_response = {"house_price": [109631.2265625]}
diff = DeepDiff(response.json(), expected_response)
print(f"diff={diff}")

assert "type_changes" not in diff
