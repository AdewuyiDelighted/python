import re

print(True if re.fullmatch(r'\d+[A-Z][a-z]*[A-Z][a-z]*', "1PreciousRuth") else False)
# tokenzation
print(re.split(r',\s*', '1, 2, 3,4,5,6,7,8'))
