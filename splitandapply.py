#! /usr/bin/env python

import sys
import re

def parse_header(s, reqs, incs):
  lines  = []
  s     += "\n"
  # cut with indent and quot.
  indent = 0
  pidt   = False
  mode   = ""
  temp   = [0, 0, ""]
  ws         = {}
  ws[' ']    = ' '
  ws['\t']   = '\t'
  nl         = {}
  nl['\n']   = '\n'
  nl['\r']   = '\r'
  quot       = {}
  quot['\''] = '\''
  quot['\"'] = '\"'
  quot['\\'] = '\\'
  for ss in range(0, len(s)):
    pp = re.split(r"([\ \t\n\r\"\'\(\)\{\}\<\>\:\,])", s[ss])
    for p in pp:
      if(0 < len(mode) and mode[- 1] in quot):
        if(p in quot and 0 < len(mode) and mode[- 1] == p):
          mode = mode[:-1]
        else:
          temp[- 1] += p
        continue
      elif(p in ws or p == ''):
        if(pidt):
          if(0 < len(temp[- 1])):
            temp.append("")
        else:
          indent += 1
          temp[1] = indent
        continue
      else:
        pidt  = True
      if(p in quot):
        mode += p
      elif(p in nl):
        if(0 < len(mode)):
          print "NG @ line:", ss + 1, " : stack: ", temp
        if(len(temp[- 1]) <= 0):
          temp = temp[:-1]
        if(2 < len(temp)):
          lines.append(temp)
        indent = 0
        pidt   = False
        mode   = ""
        temp   = [0, 0, ""]
      elif(0 < len(p)):
        temp[- 1] += p
        temp.append("")
  lines.append(temp)
  lines.append([- 1, - 1])
  # cut input to class, function, definition list.
  indent   = 0
  mode     = ""
  NAME     = 0
  CLASSTBL = 1
  DEFTBL   = 2
  VARTBL   = 3
  root     = {}
  root["root"] = ["root", {}, {}, {}, [], []]
  work     = root["root"]
  for ss in range(0, len(lines)):
    s = lines[ss]
    if(mode == "#"):
      if(indent <= s[1]):
        continue
      mode = ""
    elif(0 < len(mode) and s[1] < indent):
      mode = ""
      work = root["root"]
    if(len(s) < 3):
      continue
    elif(s[2] == "require"):
      if(not (s[3] in reqs) and mode == ""):
        f = open(s[3])
        reqs[s[3]] = s[3]
        # XXX: collidion?
        root.update(parse_header(f.readlines(), reqs, incs))
        f.close()
    elif(s[2] == "include"):
      if(s[3] in lincs):
        print "recursive includes."
        continue
      f = open(s[3])
      lincs = []
      for u in range(0, len(incs)):
        lincs.append(incs[u])
      lincs.append(s[3])
      r = parse_header(f.readlines(), reqs, lincs)
      # XXX indent and collidion?
      root.update(r)
      f.close()
    elif(s[2] == "#"):
      mode   = "#"
      indent = s[1] + 2
    elif(s[2] == "class" or s[2] == "extend"):
      if(mode != ""):
        print "internal error, class or extend must be top of scope"
        break
      mode   = "C"
      if(ss + 1 < len(lines)):
        indent = lines[ss + 1][1]
      else:
        print "internal error, class or extend with null line."
        break
      name   = []
      uu     = len(s)
      for u in range(3, len(s)):
        if(s[u] == ":"):
          uu = u
          break
        name.append(s[u])
      name2  = []
      for u in range(uu + 1, len(s)):
        if(s[u] == ":"):
          print "NG"
        name2.append(s[u])
      root["".join(name)] = ["".join(name), {}, {}, {}, name, name2]
      work = root["".join(name)]
    elif(s[2] == "using"):
      work[DEFTBL][s[3]] = s[4:]
    elif(s[2] == "def"):
      work[DEFTBL][s[3]] = s[4:]
    elif(s[2] == "var"):
      work[VARTBL][s[3]] = s[5:]
    else:
      # functions.
      print s
  print root
  return root

def parse_source(s):
  return

f = open(sys.argv[1])
reqs = {}
reqs[sys.argv[1]] = sys.argv[1]
parse_header(f.readlines(), reqs, [])
f.close()

