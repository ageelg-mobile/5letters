import re
pattern = re.compile('^a.or.$')

for i, line in enumerate(open('sgb-words.txt')):
    for match in re.finditer(pattern, line):        
        print( 'Found on line %s: %s' % (i+1, match.group()))