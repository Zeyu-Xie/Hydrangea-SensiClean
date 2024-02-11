import json
import os

str = []

for i in range(1, 18384):
    str.append(chr(i))

json_str = json.dumps(str, ensure_ascii = False, indent = 4)

print(json_str)

print(os.path.abspath(os.path.dirname(__file__)))

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "Step_1-Unicode_Listing.json"), "w") as file:
    file.write(json_str)