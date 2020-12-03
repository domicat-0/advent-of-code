import re, random
policy_list = []

with open('input_2.txt', 'r') as file:
    for line in file.readlines():
        policy_list.append(line.rstrip())

valid = 0
invalid = 0
for policy in policy_list:
    low, high, char, password = re.match(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$', policy).groups()
    low, high = int(low), int(high)
    if low <= password.count(char) <= high:
        print("valid")
        valid += 1
    elif random.random() >= 0.97:
        print("invalid", policy, low, password.count(char), high)
        invalid += 1
print(valid, invalid)