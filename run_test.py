import json
with open('issues.json', mode='r') as issues:
    data = json.load(issues)

print(data)