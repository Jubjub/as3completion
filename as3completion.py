import os
import re

LIB_FOLDER = '../../Documents/Flash/Lib'

rclass = re.compile(r'^\s*public\s+class\s+(\w+)', re.MULTILINE)
rpvar = re.compile(r'^\s*public\s+var\s+(\w+)\s*:\s*(\w+)', re.MULTILINE)
rpfunction = re.compile(r'^\s*public\s+function\s+(\w+)\s*\(.*\):?(\w+)?', re.MULTILINE)

class Class():
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        member.owner = self
        self.members.append(member)

class Var():
    def __init__(self, name, t):
        self.name = name
        self.t = t

class Function():
    def __init__(self, name, ret):
        self.name = name
        self.ret = ret

def extract_bracket_content(text, start=0):
    level = 0
    started = False
    fstart = 0
    fend = 0
    for i in range(start, len(text)):
        if text[i] == '{':
            level += 1
            if not started:
                fstart = i
                started = True
        elif text[i] == '}':
            level -= 1
        if started and not level:
            fend = i
            break
    return text[fstart:fend]

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
            for vmatch in rpvar.finditer(content):
                v = Var(vmatch.group(1), vmatch.group(2))
                c.add_member(v)
                classes.append(c)
                print '    %s %s' % (v.t, v.name)
            for fmatch in rpfunction.finditer(content):
                f = Function(fmatch.group(1), fmatch.group(2) or 'void')
                c.add_member(f)
                print '    %s %s()' % (f.name, f.ret)

def complete(page, position):
    return [{'word' : str(position), 'kind' : 'v'}, {'word' : 'moar testing', 'kind' : 'f'}]

if __name__ == '__main__':
    print generate_tags(LIB_FOLDER)

