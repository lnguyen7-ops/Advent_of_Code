#!/usr/bin/env python

'''
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
'''
# bag class
class Bag:
	def __init__(self, value):
		self.value = value # data
		self.children = [] # contain references to other nodes
		self.children_count = []
		self.parents = []

	def __repr__(self):
		return self.value

	def add_child(self, child, count):
		self.children.append(child)
		self.children_count.append(count)

	def add_parent(self, parent):
		self.parents.append(parent)

	def in_list(self, bags):
		'''
		Return index this bag is in a list of bags if exist.
		else return None
		'''
		for i, bag in enumerate(bags):
			if self.value == bag.value:
				return i
		return None

class solution():
	def __init__(self, input_path):
		# read input
		with open(input_path) as f:
			self.data = f.readlines()

		self.bags = [] # list of bags
		# create list of bags from input file
		for line in self.data:
			temp = [section.strip() for section in line.split("contain")]
			# list of chidren bag names
			children = [x.strip() for x in temp[1].split(",")]
			# create bag. Dont keep the word "bags"
			parent = self.get_bag(temp[0][:-5], self.bags)
			# children bags
			for name in children:
				x = name.split(" ")
				if x[0]=="no":
					continue
				else:
					child = self.get_bag(" ".join(x[1:-1]), self.bags)
				parent.add_child(child, int(x[0])) # add child to parent bag
				child.add_parent(parent) # add parent to child

	def get_bag(self, name, list_bags):
		'''
		Get bag from list. If not exist, create new bag and add to list
		-----------------------------
		name: str. Bag name
		list_bags: list of bags
		-----------------------------------
		return: bag object
		'''
		bag = Bag(name)
		bag_idx = bag.in_list(list_bags)
		if bag_idx==None:
			list_bags.append(bag)
		else:
			bag = list_bags[bag_idx]
		return bag

	# Part 1 solution
	def p1(self, name):
		bag = self.get_bag(name, self.bags)
		visited = [] # bag already checked
		stack = bag.parents.copy() # bag to be checked
		while stack:
			cur_bag = stack.pop()
			if cur_bag.in_list(visited)==None:
				visited.append(cur_bag)
				stack.extend(cur_bag.parents)
		return len(visited)

	# Part 2 solution
	def p2(self, name):
		def recur(bag):
			if len(bag.children)==0: # bag has no child bags
				return 0
			temp = []
			for i in range(len(bag.children)):
				child = bag.children[i]
				children_count = bag.children_count[i]
				temp.append(children_count + children_count * recur(child))
			return sum(temp)
		# get bag from bags list
		bag = self.get_bag(name, self.bags)
		return recur(bag)
            
######################################################
if __name__=="__main__":
	sol = solution("inputs/input_07.txt")
	print(f"Part 1 answer: {sol.p1('shiny gold')}")
	print(f"Part 2 answer: {sol.p2('shiny gold')}")