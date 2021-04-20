import json
import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs
from html.parser import HTMLParser

trees = {}
tree = {}

class ChampionParser(HTMLParser):
	steps = []
	phase = "?"
	def handle_starttag(self, tag, attrs):
		if tag == "div":
			step = "?"
			for attr in attrs:
				if attr[0] == "class":
					if attr[1] == "fusion-one-fourth fusion-layout-column fusion-spacing-yes":
						step = "description"
					if attr[1] == "table-1 bigtree" or attr[1] == "table-1 bigtree1":
						step = "stats"
			self.steps.append(step)
		elif tag == "td":
			step = "?"
			if len(self.steps) != 0:
				if self.steps[-1] == "stats":
					if self.phase == "circumference_td":
						self.phase = "?"
						step = "circumference"
					elif self.phase == "tree_height_td":
						self.phase = "?"
						step = "height"
					elif self.phase == "crown_spread_td":
						self.phase = "?"
						step = "crown_spread"
					elif self.phase == "nominated_td":
						self.phase = "?"
						step = "nominated_by"
					elif self.phase == "year_nominated_td":
						self.phase = "?"
						step = "year_nominated"
					elif self.phase == "date_crowned_td":
						self.phase = "?"
						step = "date_crowned"
					else:
						for attr in attrs:
							if attr[0] == "class":
								if attr[1] == "circumference":
									self.phase = "circumference_td"
								elif attr[1] == "tree-height":
									self.phase = "tree_height_td"
								elif attr[1] == "crow-spread":
									self.phase = "crown_spread_td"
								elif attr[1] == "nominated":
									self.phase = "nominated_td"
								elif attr[1] == "year-nominated":
									self.phase = "year_nominated_td"
								elif attr[1] == "date-crowned":
									self.phase = "date_crowned_td"
			self.steps.append(step)

	def handle_data(self, data):
		global tree
		s = "" if len(self.steps) == 0 else self.steps[-1]
		if s == "circumference" and 'circumference' not in tree:
			tree['circumference'] = int(data.strip())
		elif s == "height" and 'height' not in tree:
			tree['height'] = int(data.strip())
		elif s == "crown_spread" and 'crown_spread' not in tree:
			tree['crown_spread'] = int(data.strip())
		elif s == "nominated_by" and 'nominated_by' not in tree:
			tree['nominated_by'] = data.strip()
		elif s == "year_nominated" and 'year_nominated' not in tree:
			tree['year_nominated'] = data.strip()
		elif s == "date_crowned" and 'date_crowned' not in tree:
			tree['date_crowned'] = data.strip()
		elif s == "description" and 'description' not in tree:
			tree['description'] = data.strip()

	def handle_endtag(self, tag):
		if tag == "div" or tag == "td":
			if len(self.steps) != 0:
				self.steps.pop()


class ChampionTreesParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global tree
		if tag == "span":
			new_step = tag
			for attr in attrs:
				if attr[0] == "class":
					if attr[1] == "bigtrees_results_section":
						tree = {}
						self.steps = []
					new_step = attr[1]
			self.steps.append(new_step)
		if tag == "img" and len(self.steps) != 0 and self.steps[-1] == "tree_img_span":
			for attr in attrs:
				if attr[0] == "src":
					tree["img"] = attr[1]
		if tag == "a" and len(self.steps) != 0 and self.steps[-1] == "tree_img_span":
			for attr in attrs:
				if attr[0] == "href":
					tree["url"] = attr[1]

	def handle_endtag(self, tag):
		global tree
		global trees
		if tag == "span":
			if len(self.steps) != 0:
				if self.steps.pop() == "bigtrees_results_section":
					trees[tree['url']] = tree
					print(tree)
					tree = {}

	def handle_data(self, data):
		global tree
		s = "" if len(self.steps) == 0 else self.steps[-1]
		if s == "bigtrees_results_title":
			tree['name'] = data.strip()
		elif s == "bigtrees_results_question":
			if data == "Scientific Name:":
				self.steps_key = "scientific_name"
			elif data == "State:":
				self.steps_key = "state"
			elif data == "County:":
				self.steps_key = "county"
			elif data == "Points:":
				self.steps_key = "points"
		elif s == "bigtrees_results_ans":
			if self.steps_key == "points":
				tree[self.steps_key] = int(data.strip())
			else:
				tree[self.steps_key] = data.strip()


def flatten_trees(unflat_trees):
	flat_trees = []
	for tree_key in unflat_trees:
		url = urlparse(tree_key)
		query = parse_qs(url.query)
		tree = trees[tree_key]
		tree['id'] = int(query['page_id'][0])
		flat_trees.append(tree)
	return flat_trees

parser = ChampionTreesParser()

with open("woodland/data/champions.html", "r") as f:
		champions_html = f.read()

parser.feed(champions_html)

flat_trees = flatten_trees(trees)

with open("woodland/data/champions.json", "w") as f:
	for line in json.dumps({"trees" :  flat_trees}, indent=2).splitlines():
		f.write(line)
		f.write("\n")

print("enriching trees")

for flat_tree in flat_trees:
	# TODO get GPS
	req = requests.get(flat_tree['url'])
	tree_parser = ChampionParser()
	tree_parser.feed(req.text)
	flat_tree.update(tree)
	trees[flat_tree['url']] = flat_tree
	print(flat_tree)
	with open("woodland/data/champions.json", "w") as f:
		for line in json.dumps({"trees" :  flatten_trees(trees)}, indent=2).splitlines():
			f.write(line)
			f.write("\n")
