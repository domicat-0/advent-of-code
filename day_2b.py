import re, random
policy_list = []

with open('input_2.txt', 'r') as file:
    for line in file.readlines():
        policy_list.append(line.rstrip())

valid = 0
for policy in policy_list:
    low, high, char, password = re.match(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$', policy).groups()
    low, high = int(low), int(high)
    if (password[low-1] == char) ^ (password[high-1] == char):
        valid += 1

print(valid)