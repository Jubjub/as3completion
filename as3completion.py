import os
import re

LIB_FOLDER = '../../Documents/Flash/Lib'

rclass = re.compile(r'^\s*public\s+class\s+(\w+)', re.MULTILINE)

class Class():
    def __init__(self, name):
        pass

def extract_bracket_content(text, start=0):
    print start

def generate_tags(folder):
    paths = []
    for root, dirnames, filenames in os.walk(folder):
        for f in filenames:
            path = os.path.join(root, f)
            if path.endswith('.as'):
                paths.append(path)
    print 'found %s as3 files' % len(paths)
    classes = []
    for path in paths:
        f = open(path, 'rb')
        text = f.read()
        f.close()
        # match classes
        for match in rclass.finditer(text):
            name = match.group(1)
            print name
            c = Class(name)
            content = extract_bracket_content(text, match.start())

if __name__ == '__main__':
    print generate_tags(LIB_FOLDER)

