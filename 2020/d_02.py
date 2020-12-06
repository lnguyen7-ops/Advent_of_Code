#!/usr/bin/env python

'''
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
'''
class solution():
	def __init__(self, input_path):
		self.data = []
		# read input
		with open(input_path) as f:
			for line in f.readlines():
				line = line.strip().split(" ")
				line[0] = [int(x) for x in line[0].split("-")]
				line[1] = line[1].strip(":")
				self.data.append(line)

	# Part 1 solution
	def p1(self):
		result = 0
		for dat in self.data:
			count = dat[2].count(dat[1])
			if (count >= dat[0][0]) and (count <= dat[0][1]):
				result += 1
		return result

	# Part 2 solution
	def p2(self):
		result = 0
		for dat in self.data:
			pw = dat[2]
			char = dat[1]
			try:
				if (pw[dat[0][0]-1]==char) != (pw[dat[0][1]-1]==char): #not using zero index
					result += 1
			except:
				continue
		return result
		
##########################################################
if __name__ == "__main__":
	sol = solution("inputs/input_02.txt")
	print(f"Part 1 answer: {sol.p1()}")
	print(f"Part 2 answer: {sol.p2()}")