with open('input/0022_names.txt') as input:
    text = input.read()

names = [name.strip('"') for name in text.split(',')]
names.sort()

def name_score(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

name_scores = {name: i * name_score(name) for i, name in enumerate(names, start=1)}

print(sum(name_scores.values()))