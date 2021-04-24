import json

with open("woodland/data/champions.json", "r") as f:
		champions_json = f.read()
		champions = json.loads(champions_json)

minimum = 1000
maximum = 0

for tree in champions["trees"]:
	h = tree["height"]
	if h < minimum:
		minimum = h
	if h > maximum:
		maximum = h

print("minimum = %s" % minimum)
print("maximum = %s" % maximum)