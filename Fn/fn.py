#! /usr/bin/env python

import sys
import re

# thanks to: https://qiita.com/hoto17296/items/e1f80fef8536a0e5e7db
flatten = lambda x: "_".join([z for y in x for z in (flatten(y) if (hasattr(y, '__iter__') and not isinstance(y, str)) else y,)])

def match_type(type, hblocks, cls = "root"):
  lnames = {}
  for names in hblocks["name"]:
    llname = hblocks["name"][names][0]
    lnames[llname] = llname
  for usesidx in hblocks["using"]:
    for idx in hblocks["using"][usesidx]:
      llname = hblocks["using"][usesidx][idx][0][0]
      lnames[llname] = llname
  lnames["def"] = "def"
  if(type[0] in lnames):
    return True
  print type
  return False

def debug_types_header(hblocks):
  for lets in hblocks["let"]:
    for ll in hblocks["let"][lets]:
      llets = hblocks["let"][lets][ll][1][0]
      if(not match_type(llets, hblocks)):
        print("NG type: ", llets)
  fnfriends = {}
  for f in hblocks["fn"]:
    fnfriends[f] = hblocks["fn"][f]
  for f in hblocks["friend"]:
    for ff in hblocks["friend"][f]:
      fnfriends[f][ff] = hblocks["friend"][f][ff]
  for fnridx in fnfriends:
    fnroot = fnfriends[fnridx]
    for fnidx in fnroot:
      fn = fnroot[fnidx]
      if(len(fn) <= 0 or len(fn[0]) <= 0 or 2 < len(fn)):
        print("NG # val: ", fn)
        continue
      idx0 = 1
      if(fn[0][0] == "operator"):
        idx0 = 2
      if(not match_type(fn[1], hblocks)):
        print("NG type: ", fn)
      if(fn[0][idx0][0] != "("):
        print("NG bracket: ", fn)
      buf = []
      for idx in range(1, len(fn[1])):
        if(fn[1][idx] == ","):
          if(not match_type(buf, hblocks)):
            print("NG type: ", fn, buf)
          buf = []
      if(0 < len(buf) and not match_type(buf, hblocks)):
        print("NG type: ", fn, buf)
  return

def header_block(blocks):
  uroot  = {}
  vroot  = {}
  droot  = {}
  froot  = {}
  frroot = {}
  nroot  = {}
  uroot["root"] = {}
  vroot["root"] = {}
  droot["root"] = {}
  froot["root"] = {}
  frroot["root"] = {}
  nroot["root"] = ["root"]
  ustack = uroot["root"]
  vstack = vroot["root"]
  dstack = droot["root"]
  fstack = froot["root"]
  frstack = froot["root"]
  chgc   = False
  indent = 0
  for a in blocks:
    if(chgc):
      indent = a[1]
      chgc   = False
    if(indent != a[1]):
      ustack = uroot["root"]
      vstack = vroot["root"]
      dstack = droot["root"]
      fstack = froot["root"]
      frstack = frroot["root"]
    if(a[0] == "class"):
      chgc   = True
      if(not (flatten(a[2]) in vroot)):
        uroot[flatten(a[2])] = {}
        vroot[flatten(a[2])] = {}
        droot[flatten(a[2])] = {}
        froot[flatten(a[2])] = {}
        frroot[flatten(a[2])] = {}
        nroot[flatten(a[2])] = a[2]
      ustack = uroot[flatten(a[2])]
      vstack = vroot[flatten(a[2])]
      dstack = droot[flatten(a[2])]
      fstack = froot[flatten(a[2])]
      frstack = frroot[flatten(a[2])]
    elif(a[0] == "let" or \
         a[0] == "fn"  or \
         a[0] == "friend" or \
         a[0] == "def" or \
         a[0] == "using"):
      # def class int
      if(flatten(a[2]) in vstack):
        print("hash collidion")
      if(a[0] == "let"):
        vstack[flatten(a[2])] = [a[2], a[3]]
      elif(a[0] == "fn"):
        fstack[flatten(a[2])] = [a[2]]
        fstack[flatten(a[2])].extend(a[3])
      elif(a[0] == "friend"):
        frstack[flatten(a[2])] = [a[2]]
        frstack[flatten(a[2])].extend(a[3])
      elif(a[0] == "def"):
        dstack[flatten(a[2])] = [a[2], a[3]]
      elif(a[0] == "using"):
        if(3 < len(a)):
          ustack[flatten(a[2])] = [a[2], a[3]]
        else:
          ustack[flatten(a[2])] = [a[2]]
  res = {}
  res["using"] = uroot
  res["let"]   = vroot
  res["def"]   = droot
  res["fn"]    = froot
  res["friend"] = frroot
  res["name"]  = nroot
  return res

# split each line.
def header_parts(a):
  b = a["cache"]
  if(len(b) <= 0 or len(b[0]) <= 0):
    return []
  term = {}
  term["let"]    = "let"
  term["fn"]     = "fn"
  term["friend"] = "friend"
  term["using"]  = "using"
  term["def"]    = "def"
  term["class"]  = "class"
  nocolon = {}
  nocolon["class"]  = "class"
  nocolon["using"]  = "using"
  if(b[0] in term):
    if((b[0] == "class") and a["indent"] != 0):
      print("NG no root class.", a["line"])
      return []
    idx = - 1
    for u in range(1, len(b)):
      if(b[u] == ":"):
        if(idx < 0):
          idx = u
        else:
          print("NG multiple colon: ", a, b)
    if(idx < 0):
      if(b[0] in nocolon):
        return [b[0], a["indent"], b[1:]]
      else:
        print("NG no colon: ", a, b)
        return []
    return [b[0], a["indent"], b[1:idx], b[idx + 1:]]
  elif(b[0] == "#" or b[0] == "//"):
    pass
  else:
    print("NG: ", b[0], ",", a["line"])
  return []

# original source to [work, ...]
# work["line"]   : line no.
# work["indent"] : indent no.
# work["cache"]  : splitted lines with no blank chars.
def cut(s):
  bra = {}
  bra[")"] = "("
  bra["}"] = "{"
  bra["]"] = "["
  braket = {}
  braket["("] = "("
  braket[")"] = ")"
  braket["{"] = "{"
  braket["}"] = "}"
  braket["["] = "["
  braket["]"] = "]"
  work   = [{}]
  work[- 1]["cache"] = []
  work[- 1]["line"]  = 1
  stack  = [work[- 1]["cache"]]
  indent = 0
  mode   = ''
  for ss in range(0, len(s)):
    pp = re.split(r"([\ \t\n\r\(\)\{\}\[\]\:\,])", s[ss])
    for p in pp:
      if(p == ' ' or p == '\t' or p == ''):
        if(indent >= 0 and p != ''):
          indent += 1
        continue
      else:
        if(indent >= 0):
          if(0 < len(work[- 1]["cache"])):
            if(work["indent"] != indent):
              print("NG indent: ", ss, " indent: ", indent)
          work[- 1]["indent"] = indent
          indent = - 1
      if(0 < len(mode) and mode[- 1] == '\\' and p != '\r' and p != '\n'):
        stack[- 1].append(p)
        mode = mode[:- 1]
        continue
      elif(0 < len(mode) and mode[- 1] == ':'):
        if(p[0] == '=' and p != '\r' and p != '\n'):
          stack[- 1].append(mode[- 1] + p)
          mode = mode[:- 1]
          continue
        stack[- 1].append(mode[- 1])
        mode = mode[:- 1]
      if(p == '\\'):
        mode += '\\'
      elif(p == ':'):
        mode += ':'
      elif(p == '\r' or p == '\n'):
        if(len(mode) > 0 and mode[- 1] == '\\'):
          mode = mode[:- 1]
        else:
          if(0 < len(mode)):
            print("NG no closed line: ", ss, " indent: ", indent, " mode: ", mode)
          work.append({})
          work[- 1]["cache"] = []
          work[- 1]["line"]  = ss + 1
          stack = [work[- 1]["cache"]]
          mode = ''
        indent = 0
      elif(p in braket):
        if(p in bra):
          if(len(mode) <= 0 or mode[- 1] != bra[p]):
            print("NG no closed modes line: ", ss, " indent: ", indent, ", mode: ", mode)
          else:
            mode  = mode[:-1]
            stack = stack[:-1]
        else:
          if(len(work[- 1]["cache"]) <= 0):
            print("NG no type line: ", ss, " indent: ", indent)
          mode += p
          stack[- 1].append([p])
          stack.append(stack[- 1][- 1])
      else:
        stack[- 1].append(p)
  return work

work   = cut(sys.stdin.readlines())
hparts = []
for w in work:
  w = header_parts(w)
  if(len(w) > 0):
    hparts.append(w)
hh     = header_block(hparts)
for h in hh:
  print h
  if(h != "name"):
    for h0 in hh[h]:
      print h0
      for h1 in hh[h][h0]:
        print h1
        print hh[h][h0][h1]
      print
  else:
    for h0 in hh[h]:
      print h0, hh[h][h0]
  print
print("type check.")
debug_types_header(hh)
print("OK")

