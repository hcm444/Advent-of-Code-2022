import re
text_file = open("Day6.txt", "r")
string = text_file.read()
#read text file
pattern = r'(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)'
#pattern for first 4
match = re.search(pattern, string)
if match:
    print(match.start() + 4)
