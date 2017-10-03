import yaml
import sys
from pprint import pprint

# variables/counters declaration
in_yaml = False
content = []
counter = 0

# Read input file
with open('README.md', 'r') as f:
    lines = f.readlines()


all_lines = []
for line in lines:
    all_lines.append(line.replace("\n",""))

lines = all_lines

#print(lines)


content = []

# Loop through all the lines
for line in lines:
    counter = counter + 1

    if not in_yaml and line.startswith('```'):
        in_yaml = True
    elif in_yaml and line.startswith("```"):
        in_yaml = False
    elif in_yaml:
        content.append(line)
        
s = '\n'.join(content)

if '\t' in s:
    print("ERROR: your file contains a TAB")

try:
    d = yaml.load(s)
except Exception as e:
    print ("ERROR: you have a problem in your file")
    print (e)

pprint (d)
